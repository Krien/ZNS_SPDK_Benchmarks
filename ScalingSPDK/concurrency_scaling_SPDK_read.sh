#!/bin/bash

DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
cd $DIR

if ! command -v "$FIO_DIR/fio" &> /dev/null
then
    echo "Please add fio to your path"
    exit 1
fi

if [ -z SPDK_DIR ]; then
    echo "Please provide a path to the SPDK_DIR"
    exit 1
fi


if [[ "$#" -ne 2 ]]; then
    echo "Please add a <max_job> and a list of space-separated [device_name,namespace]"
    echo "For example: 8 \"nvme0n1,1 nvme1n1,1\""
    echo "This will start with 1 job for each device and scale up to 8 jobs for each concurrently"
    exit 1
fi

# Parse input
max_job="$1"

in=$(echo "$2"    | awk 'BEGIN{FS=" ";OFS="\n"}{$1=$1}1')
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

for job_cnt in $(seq 1 "$max_job"); do
# Create FIO test
#define job
jobname="./tmp/concurrency_read_autogenerated_spdk_$job_cnt.fio"
jobglob=$(cat <<'EOF'
# This file is autogenerated, do not alter
[global]
ioengine=spdk
thread=1
group_reporting=1
direct=1
time_based=1
ramp_time=20
runtime=180
size=128z
rw=read
iodepth=1
zonemode=zbd
bs=4096
EOF
)
jobworker=$(cat <<'EOF'
offset_increment=128z
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
    echo "numjobs=$job_cnt" >> $jobname
done
done 

# Bind SPDK
PCI_ALLOWED=""
for dev in "${devs[@]}"; do
    trid=$(ls -l "/sys/block/$dev/device/device" | awk '{split($11,dev,"/"); print dev[4]}')
    PCI_ALLOWED="$trid $PCI_ALLOWED"
done

echo "Binding SPDK to PCI addresses: $PCI_ALLOWED"
PCI_ALLOWED=$PCI_ALLOWED $SPDK_DIR/scripts/setup.sh


for job_cnt in $(seq 1 "$max_job"); do
jobname="./tmp/concurrency_read_autogenerated_spdk_$job_cnt.fio"
echo "Running fio with $job_cnt jobs for each device"
echo "job is:"
echo "$(cat $jobname)"

LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$SPDK_DIR/build/lib" LD_PRELOAD="$SPDK_DIR/build/fio/spdk_nvme" $FIO_DIR/fio "$jobname" --output="./out/concurrency_scaling_read_spdk_${job_cnt}.json" --output-format="json"
done

# Remove SPDK
echo "UNBINDING SPDK"
$SPDK_DIR/scripts/setup.sh reset
