#!/bin/bash
DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
cd $DIR

mkdir -p out
mkdir -p tmp

if [[ "$#" -ne 2 ]]; then
    echo "Please add a <max_job> and a list of space-separated [device_name,namespace]"
    echo "For example: 8 \"nvme0n1,1 nvme1n1,1\""
    echo "This will start with 1 job for each device and scale up to 8 jobs for each concurrently"
    exit 1
fi

# Run the tests
./concurrency_scaling_libaio_write.sh $1 $2 || exit 1;
./concurrency_scaling_SPDK_write.sh $1 $2 || exit 1;
