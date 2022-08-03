#!/bin/bash

DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
cd $DIR

if ! command -v fio &> /dev/null
then
    echo ""
    echo "Please add fio to your path"
    echo ""
    exit 1
fi 

if [ -z SPDK_DIR ]; then
    echo ""
    echo "Please provide a path to the SPDK_DIR"
    echo ""
    exit 1
fi

for bs in 512 1kB 2kB 4kB 8kB 16kB 32kB; do 
    LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$SPDK_DIR/build/lib"  LD_PRELOAD="$SPDK_DIR/build/fio/spdk_nvme" fio read_test.fio --bs=$bs > "./data/reads/out_read_$bs";
done
