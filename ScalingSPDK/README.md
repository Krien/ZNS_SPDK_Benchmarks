# ScalingSPDK

Various scripts to test scalibility.
Try `concurrency_scaling.sh` with a number of devices, it will test how well the CPU can keep up with libaio and SPDK.
Data and images will be generated in `/out`. The command I ran was:

```bash
sudo ./concurrency_scaling.sh w 8 "nvme1n0,1 nvme1n1,1"
sudo ./concurrency_scaling.sh r 8 "nvme1n0,1 nvme1n1,1"
# and then on a second machine (scp) that comes with Python Matplotlib stuff
python3 concurrency_scaling_plot.py 8
```
