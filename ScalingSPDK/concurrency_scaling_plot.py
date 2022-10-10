#!/usr/bin/python
import sys
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def savefig(fig, name):
    fig.savefig(name + ".png")
    fig.savefig(name + ".svg")


def plotscale(scale, dirr, label, labelw):
    kiops_libaio = []
    kiops_spdk = []
    if label == "write":
        kiops_spdk_append = []
    for i in range(scale):
        file_name = (
            "./data/"
            + dirr
            + "/concurrency_scaling_"
            + label
            + "_spdk_"
            + str(i + 1)
            + ".json"
        )
        file = open(file_name, "r")
        data = file.read()
        data = json.loads(data)
        kiops_spdk.append(int(data["jobs"][0][label]["iops"]) / 1000)
    for i in range(scale):
        file_name = (
            "./data/"
            + dirr
            + "/concurrency_scaling_"
            + label
            + "_libaio_"
            + str(i + 1)
            + ".json"
        )
        file = open(file_name, "r")
        data = file.read()
        data = json.loads(data)
        kiops_libaio.append(data["jobs"][0][label]["iops"] / 1000)
    if label == "write":
        for i in range(scale):
            file_name = (
                "./data/"
                + dirr
                + "/concurrency_scaling_"
                + "append"
                + "_spdk_"
                + str(i + 1)
                + ".json"
            )
            file = open(file_name, "r")
            data = file.read()
            data = json.loads(data)
            kiops_spdk_append.append(int(data["jobs"][0][label]["iops"]) / 1000)

    fig, ax = plt.subplots()
    plt.plot(
        [x + 1 for x in list(range(scale))], kiops_libaio, linewidth=3, label="Libaio"
    )
    plt.plot([x + 1 for x in list(range(scale))], kiops_spdk, linewidth=3, label="SPDK")
    if label == "write":
        plt.plot(
            [x + 1 for x in list(range(scale))],
            kiops_spdk_append,
            linewidth=3,
            label="SPDK + ZNS Append",
        )
    plt.ylim(0, 4.5 * 10**2)
    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
    plt.xlabel("Jobs per SSD")
    plt.ylabel("KIOPS")
    plt.title("KIOPS: " + labelw + " concurrently to 2 ZNS SSDs")
    plt.legend()
    savefig(plt, "out/" + label + dirr)


def main(workload, dirr, scale):
    if workload[0] == "w":
        plotscale(scale, dirr, "write", "Writing")
    elif workload[0] == "r":
        plotscale(scale, dirr, "read", "Reading")
    else:
        print("unknown workload")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("not enough args")
        exit(-1)
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
