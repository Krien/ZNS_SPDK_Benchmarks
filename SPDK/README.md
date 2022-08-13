# SPDK benchmarks
This directory contains various benchmarks for ZNS for SPDK, data that resulted from running the benchmarks and plotting tools to visualise the data.
Not all benchmarks are maintained in this directory.

## Installing and running the fio tests
Getting fio up and running with SPDK can be a bit of a hassle. In general try to follow the README for the SPDK version used, 
which is at the moment stored in the repository at https://github.com/spdk/spdk/tree/master/examples/nvme/fio_plugin.
Then the tests can be run as root with:
```bash
export PCI_ALLOWED=${PCI_ADDR} # PCI_ADDR of device to use
<SPDK_DIR>/scripts/setup.sh
# Alter then `filename` in the desired fio script to match the trid and ns.
LD_LIBRARY_PATH=<SPDK_DIR>/build/lib LD_PRELOAD=<SPDK_DIR>/build/fio/spdk_nvme fio <fio_script_to_test>.fio 
```

## Installing and running the custom reset test
The custom reset test makes use of [SZD](https://github.com/Krien/SimpleZNSDevice), which in turn uses SPDK.
Be sure to pull this repository and initialise its dependencies (SPDK) with:
```bash
git submodule update --init
```
Then built SPDK first:
```bash
pushd .
cd dependencies/spdk
# Follow SPDK built instructions as provided in the repo. Options do not matter
popd
cmake -DSZD_TOOLS="reset_perf" . # generate built tools for the reset perf tool
make -j $nprocs reset_perf
```
Then the reset tool can be run with (as root):
```bash
export PCI_ALLOWED=${PCI_ADDR} # PCI_ADDR of device to use
<SPDK_DIR>/scripts/setup.sh
LD_LIBRARY_PATH=<SPDK_DIR>/build/lib LD_PRELOAD=<SPDK_DIR>/build/fio/spdk_nvme \ 
    fio fill.fio # fill device
cd <SZD_DIR>
./bin/reset_perf 0 ${PCI_ADDR} > reset_out
cp reset_out <ZNS_SPDK_Benchmarks_dir>/SPDK/data/resets/reset_out
```

## Installing the plotting tools and generating the plots
The plotting tools require Python3. Apart from Python3 a number of dependencies are required, specified in `requirements.txt`. 
These can be installed with pip, but we recommend using venv. The dependencies can be installed with venv as follows:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
The plots can then be generated with (while in the venv):
```bash
python3 <plotfile>.py
```
Note that not all plot files automatically retrieve data from the data directory.
Most plot scripts have copied data manually. This is done as only a part of the data was needed and the plots were made at an earlier stage.
This might change in the future, but for now check the top of the file to find out how it retrieves its data.
