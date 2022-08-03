#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Dimension to plot in square (e.g., PLOT_DIM = 40 for 40x40)
PLOT_DIM = 60
data = np.zeros(shape=(PLOT_DIM, PLOT_DIM))
datadir = "data/resets/reset_out"

plt.rc('font', size=12)          # controls default text sizes
plt.rc('axes', titlesize=12)     # fontsize of the axes title
plt.rc('axes', labelsize=12)     # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=12)    # legend fontsize

def parse():
    with open(datadir, 'r') as file: 
        limit = PLOT_DIM**2
        counter = 0
        x_index = y_index = 0

        for line in file:
            if line.split()[0] == "Reset":
                # If data file has more lines than can fit in the array, break
                if counter == limit:
                    break
                elif y_index != 0 and y_index % PLOT_DIM == 0:
                    x_index += 1
                    y_index = 0

                dat = line.split() 
                data[x_index][y_index] = float(dat[2]) 

                counter += 1
                y_index +=1 

# Not usable to fit all in 1D
def plot_1D():
    ax = sns.heatmap([np.asarray(data.flatten('C'))], linewidth=0.5, yticklabels=False, cbar_kws={'format': '%d usec'})
    plt.xlim(0,PLOT_DIM**2)
    ticks = np.arange(1,PLOT_DIM**2,PLOT_DIM)
    ax.set_xticks(np.arange(0.5,PLOT_DIM**2,PLOT_DIM))
    ax.set_xticklabels(ticks)
    plt.xlabel("Zone Number")

    plt.savefig("out/zone_reset_1D-heatmap.pdf", bbox_inches="tight")
    plt.savefig("out/zone_reset_1D-heatmap.png", bbox_inches="tight")
    plt.clf()

def plot_2D():
    ax = sns.heatmap(data, linewidth=0.5, xticklabels=False, cbar_kws={'format': '%d usec'})
    plt.ylim(0,PLOT_DIM)
    plt.xlim(0,PLOT_DIM)

    ticks = np.arange(0,PLOT_DIM)
    ax.set_yticks(np.arange(0.5,PLOT_DIM))

    ticks = [f"zones {tick*PLOT_DIM+1}-{(tick+1)*PLOT_DIM}" for tick in ticks]
    ax.set_yticklabels(ticks)
    plt.yticks(rotation=0)

    plt.savefig("out/zone_reset_2D-heatmap.pdf", bbox_inches="tight")
    plt.savefig("out/zone_reset_2D-heatmap.png", bbox_inches="tight")
    plt.clf()

def plot_simple():
    # Reparse as we drop last results to make it even 60x60 not 3688 zones
    with open(datadir, 'r') as file: 
        data = []
        for line in file:
            if line.split()[0] == "Reset":
                dat = line.split() 
                data.append(float(dat[2])) 

    plt.plot(np.arange(1,len(data) + 1), data)
    plt.ylim(0,max(data) + .1*max(data))
    plt.grid(which='major', linestyle='dashed', linewidth='1')
    plt.xlabel("Zone Number")
    plt.ylabel("Latency (usec)")
    plt.savefig("out/zone_reset_simple_plot.pdf", bbox_inches="tight")
    plt.savefig("out/zone_reset_simple_plot.png", bbox_inches="tight")
    plt.clf()

if __name__ == "__main__":
    parse()
    # plot_1D()
    plot_2D()
    plot_simple()
