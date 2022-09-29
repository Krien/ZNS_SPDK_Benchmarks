#!/bin/bash

DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
cd $DIR

if ! command -v fio &> /dev/null
then
    echo "Please add fio to your path"
    exit 1
fi

if [ -z SPDK_DIR ]; then
    echo "Please provide a path to the SPDK_DIR"
    exit 1
fi


if [[ "$#" -ne 1 ]]; then
    echo "Please add a device name and namespace"
    exit 1
fi

# Parse input
in=$(echo "$1"    | awk 'BEGIN{FS=" ";OFS="\n"}{$1=$1}1')
devs=( $(echo "$in" | awk 'BEGIN{FS=","}; {print $1}') )
ns=( $(echo "$in"   | awk 'BEGIN{FS=","}; {print $2}') )

# Verify devs
for dev in "${devs[@]}"; do
 if $(ls "/sys/block/$dev/device/device" > /dev/null 2>&1 ); then
    echo "using /dev/$dev"
 else
    echo "Not a valid device: /sys/block/dev/$dev/device/device"
    exit 1
 fi
done

# Create FIO test
#define job
jobname="./concurrency_autogenerated.fio"
jobglob=$(cat <<'EOF'
# This file is autogenerated, do not alter
[global]
ioengine=spdk
thread=1
group_reporting=1
direct=1
time_based=1
ramp_time=5
runtime=60
size=128z
rw=write
iodepth=1
zonemode=zbd
max_open_zones=14
initial_zone_reset=1
bs=4096
EOF
)
jobworker=$(cat <<'EOF'
offset_increment=128z
numjobs=14
EOF
)
echo "$jobglob" > $jobname
for i in "${!ns[@]}"; do
    echo "" >> $jobname
    echo "[${devs[i]}]" >> $jobname
    trid=$(ls -l "/sys/block/${devs[i]}/device/device" | awk '{split($11,dev,"/"); print dev[4]}')
    triddot=$(echo $trid | sed 's/\:/./g')
    echo "filename=trtype=PCIe traddr=$triddot ns=${ns[i]}" >> $jobname
    echo "$jobworker" >> $jobname
done


# Bind SPDK
PCI_ALLOWED=""
for dev in "${devs[@]}"; do
    trid=$(ls -l "/sys/block/$dev/device/device" | awk '{split($11,dev,"/"); print dev[4]}')
    PCI_ALLOWED="$trid $PCI_ALLOWED"
done

echo "Binding SPDK to PCI addresses: $PCI_ALLOWED"
PCI_ALLOWED=$PCI_ALLOWED $SPDK_DIR/scripts/setup.sh

LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$SPDK_DIR/build/lib" LD_PRELOAD="$SPDK_DIR/build/fio/spdk_nvme" fio "$jobname"

# Remove SPDK
echo "UNBINDING SPDK"
$SPDK_DIR/scripts/setup.sh reset
