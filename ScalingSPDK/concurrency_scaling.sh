#!/bin/bash
DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
cd $DIR

mkdir -p out
mkdir -p tmp

if [[ "$#" -ne 3 ]]; then
    echo "Please add a <workload>, <max_job> and a list of space-separated [device_name,namespace]"
    echo "<Workload> can be either r or w"
    echo "<max_job> is a number (be aware of your maximum cores)"
    echo "[device_name,namespace] is ONE string where devices are paired with their ns with a \",\" and separated with a  \" \""
    echo "For example: r 8 \"nvme0n1,1 nvme1n1,1\""
    echo "This will start with 1 job for each device and scale up to 8 jobs for each concurrently"
    exit 1
fi

# Run the tests
if [[ "$1" == "r" ]]; then
    ./concurrency_scaling_libaio_read.sh "$2" "$3" || exit 1;
    ./concurrency_scaling_SPDK_read.sh "$2" "$3" || exit 1;
elif [[ "$1" == "w" ]]; then
    ./concurrency_scaling_libaio_write.sh "$2" "$3" || exit 1;
    ./concurrency_scaling_SPDK_write.sh "$2" "$3" || exit 1;
fi 
