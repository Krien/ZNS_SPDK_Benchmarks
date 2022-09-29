#!/usr/bin/python
import sys
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def savefig(fig, name):
    fig.savefig(name + ".png")
    fig.savefig(name + ".svg")

def plotscale(scale, label, labelw):
    kiops_libaio = []
    kiops_spdk = []
    for i in range(scale):
        file_name="./out/concurrency_scaling_" + label + "_spdk_" + str(i+1) + ".json"
        file=open(file_name,'r')
        data=file.read()
        data=json.loads(data)
        kiops_spdk.append(int(data["jobs"][0][label]["iops"])/1000)
    for i in range(scale):
        file_name="./out/concurrency_scaling_" + label + "_libaio_" + str(i+1) + ".json"
        file=open(file_name,'r')
        data=file.read();
        data=json.loads(data)
        kiops_libaio.append(data["jobs"][0][label]["iops"]/1000)
    
    fig, ax = plt.subplots()
    plt.plot( [x + 1 for x in list(range(scale))], kiops_libaio, linewidth=3, label='Libaio')
    plt.plot( [x + 1 for x in list(range(scale))], kiops_spdk, linewidth=3, label='SPDK')
    plt.ylim(0, 2*10**2)
    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    plt.xlabel("Jobs per SSD")
    plt.ylabel("KIOPS")
    plt.title("KIOPS: " + labelw + " concurrently to 2 ZNS SSDs")
    plt.legend()
    savefig(plt, "out/" + label)

def main(scale):
    plotscale(scale, "write", "Writing")
    plotscale(scale, "read", "Reading")

    
if __name__ == "__main__":
   main(int(sys.argv[1]))