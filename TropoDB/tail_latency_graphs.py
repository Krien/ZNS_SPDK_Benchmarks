import matplotlib.pyplot as plt

# Log latency
fig, ax = plt.subplots()
x1 = ['50%', '75%', '99%', '99.9%', '99.99%']
y1 = [4.68,  5.84, 11.44, 22.16, 519.07]
x2 = ['50%', '75%', '99%', '99.9%', '99.99%']
y2 = [5.78,  28.39, 335.47, 915.09, 1293.34]
plt.xlabel("Percentile")
plt.ylabel("Latency (μs)")
plt.title("Tail latency")
plt.yscale('log')
plt.ylim(1, 100000)
plt.plot(x1, y1, marker='o', label='RocksDB + F2FS')
plt.plot(x2, y2, marker='D', label='RocksDB + ZenFS')
plt.legend()
fig.savefig("out/latencylog.png")
plt.close()

# Log latency up to max
fig, ax = plt.subplots()
x1 = ['50%', '75%', '99%', '99.9%', '99.99%', '100%']
y1 = [4.68,  5.84, 11.44, 22.16, 519.07, 18251]
x2 = ['50%', '75%', '99%', '99.9%', '99.99%', '100%']
y2 = [5.78,  28.39, 335.47, 915.09, 1293.34, 1073243881]
plt.xlabel("Percentile")
plt.ylabel("Latency (μs)")
plt.title("Tail latency")
plt.yscale('log')
plt.ylim(1, 1000000000)
plt.plot(x1, y1, marker='o', label='RocksDB + F2FS')
plt.plot(x2, y2, marker='D', label='RocksDB + ZenFS')
plt.legend()
fig.savefig("out/latencylogmax.png")
plt.close()

# Plain latency
fig, ax = plt.subplots()
x1 = ['50%', '75%', '99%', '99.9%', '99.99%']
y1 = [4.68,  5.84, 11.44, 22.16, 519.07]
x2 = ['50%', '75%', '99%', '99.9%', '99.99%']
y2 = [5.78,  28.39, 335.47, 915.09, 1293.34]
plt.xlabel("Percentile")
plt.ylabel("Latency (μs)")
plt.title("Tail latency")
plt.ylim(1, 3000)
plt.plot(x1, y1, marker='o', label='RocksDB + F2FS')
plt.plot(x2, y2, marker='D', label='RocksDB + ZenFS')
plt.legend()
fig.savefig("out/latency.png")
plt.close()

# Useless
fig, ax = plt.subplots()
plt.errorbar(["ZenFS"], [14.6080], [3.59], fmt='ok', lw=3)
plt.errorbar(["ZenFS"], [14.6080], [[14.6080 - 1], [13036 - 14.6080]],
             fmt='.k', ecolor='gray', lw=1)
fig.savefig("out/latency_stacked_error.png")
plt.close()

fig, ax = plt.subplots()
x = ["ZenFS", "F2FS"]
y = [14.6080, 14.6080]
colors = ["blue", "orange"]
stdev = [3.59, 3.59]
plt.ylim(0, 30)
plt.xlabel("Key-value store")
plt.ylabel("Latency (μs)")
plt.title("Average latency")
ax.bar(x, y, yerr=stdev, color=colors, capsize=10.0)
fig.savefig("out/latency_bar_error.png")
plt.close()

# latency fillrandom
x1 = ['25%', '50%', '75%', '99%', '99.9%',
      '99.99%', '99.999%', '99.9999%', '100%']
y1 = [6.31,  8.24, 10.51, 28.18, 1203.01, 1298.12, 5852.87, 13721.19, 1440106]
x2 = ['25%', '50%', '75%', '99%', '99.9%',
      '99.99%', '99.999%', '99.9999%', '100%']
y2 = [4.82,  6.51, 8.79, 27.84, 1260.93, 2677.10, 4440.59, 6504.38, 11402]
x3 = ['25%', '50%', '75%', '99%', '99.9%',
      '99.99%', '99.999%', '99.9999%', '100%']
y3 = [3.63,  4.78, 5.93, 899.42, 1285.15, 1846.76, 2896.25, 16646.15, 1083071035]


# plt.yscale('log')
for i, j in enumerate([(100000, 6), (100000, 8), (10000000000, 9)]):
    plt.rcParams["figure.figsize"] = (7.5, 6)
    fig, ax = plt.subplots()
    plt.xlabel("Percentile")
    plt.ylabel("Latency (μs)")
    plt.title("Put Operation tail latency: 1TB of fillrandom")
    plt.ylim(1, j[0])
    plt.yscale('log')
    # plt.ylim(1, 500000)
    plt.plot(x1[:j[1]], y1[:j[1]], marker='o', label='RocksDB + F2FS')
    plt.plot(x2[:j[1]], y2[:j[1]], marker='D', label='RocksDB + ZenFS')
    plt.plot(x3[:j[1]], y3[:j[1]], marker='x', label='TropoDB')
    plt.legend()
    fig.savefig("out/latency_fillrandom" + str(i) + ".png")
    fig.savefig("out/latency_fillrandom" + str(i) + ".svg")
    plt.close()

fig, ax = plt.subplots()
boxes = [
    {
        'label': "F2FS",
        'whislo': 2,    # Bottom whisker position
        'q1': 6.31,    # First quartile (25th percentile)
        'med': 8.24,    # Median         (50th percentile)
        'q3': 10.51,    # Third quartile (75th percentile)
        'whishi': 16.81,    # Top whisker position
        'fliers': []        # Outliers
    },
    {
        'label': "ZenFS",
        'whislo': 1,    # Bottom whisker position
        'q1': 4.82,    # First quartile (25th percentile)
        'med':  6.51,    # Median         (50th percentile)
        'q3': 8.79,    # Third quartile (75th percentile)
        'whishi': 14.745,    # Top whisker position
        'fliers': []        # Outliers
    },
    {
        'label': "ZNSLSM",
        'whislo': 1,    # Bottom whisker position
        'q1': 4.31,    # First quartile (25th percentile)
        'med':  5.6229,    # Median         (50th percentile)
        'q3': 9.32,    # Third quartile (75th percentile)
        'whishi': 16.835,    # Top whisker position
        'fliers': []        # Outliers
    }
]
plt.ylim(0, 30)
ax.bxp(boxes, showfliers=False)
plt.title("Put operation Latency: 1TB of fillrandom")
ax.set_ylabel("Latency (μs)")
plt.savefig("out/boxplot_latency_random.png")
plt.close()

# latency filloverwrite
fig, ax = plt.subplots()
x1 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%', '100%']
y1 = [6.60,  8.63, 11.46, 33.26, 1245.00, 1617.83, 7419.67, 16785.65, 680503]
x2 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%', '100%']
y2 = [4.77,  6.43, 8.81, 42.78, 1271.51, 2523.26, 4207.22, 6261.71, 966438]
x3 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%', '100%']
y3 = [3.84,  5.00, 6.50, 1075.42, 1293.39, 1875.60, 3321.77, 16752.52, 1004201751]
plt.xlabel("Percentile")
plt.ylabel("Latency (μs)")
plt.title("Tail latency: 1TB of overwrites")
plt.yscale('log')
plt.ylim(1, 500000)
# plt.ylim(1, 20000)
plt.plot(x1, y1, marker='o', label='RocksDB + F2FS')
plt.plot(x2, y2, marker='D', label='RocksDB + ZenFS')
plt.plot(x3, y3, marker='x', label='TropoDB')
plt.legend()
fig.savefig("out/latency_filloverwrite.png")
# fig.savefig("out/latency_filloverwrite_no_log.png")
plt.close()

for i, j in enumerate([(100000, 6), (100000, 8), (10000000000, 9)]):
    plt.rcParams["figure.figsize"] = (7.5, 6)
    fig, ax = plt.subplots()
    plt.xlabel("Percentile")
    plt.ylabel("Latency (μs)")
    plt.title("Put Operation tail latency: 1TB of filloverwrite")
    plt.ylim(1, j[0])
    plt.yscale('log')
    # plt.ylim(1, 500000)
    plt.plot(x1[:j[1]], y1[:j[1]], marker='o', label='RocksDB + F2FS')
    plt.plot(x2[:j[1]], y2[:j[1]], marker='D', label='RocksDB + ZenFS')
    plt.plot(x3[:j[1]], y3[:j[1]], marker='x', label='TropoDB')
    plt.legend()
    fig.savefig("out/latency_filloverwrite" + str(i) + ".png")
    fig.savefig("out/latency_filloverwrite" + str(i) + ".svg")
    plt.close()


fig, ax = plt.subplots()
boxes = [
    {
        'label': "F2FS",
        'whislo': 2,    # Bottom whisker position
        'q1': 6.60,    # First quartile (25th percentile)
        'med': 8.63,    # Median         (50th percentile)
        'q3': 11.64,    # Third quartile (75th percentile)
        'whishi': 19.2,    # Top whisker position
        'fliers': []        # Outliers
    },
    {
        'label': "ZenFS",
        'whislo': 1,    # Bottom whisker position
        'q1': 4.77,    # First quartile (25th percentile)
        'med':  6.43,    # Median         (50th percentile)
        'q3': 8.81,    # Third quartile (75th percentile)
        'whishi': 10.83,    # Top whisker position
        'fliers': []        # Outliers
    }
]
plt.ylim(0, 30)
ax.bxp(boxes, showfliers=False)
ax.set_ylabel("Latency (μs)")
plt.title("Latency: 1TB of overwrites")
plt.savefig("out/boxplot_latency_overwrite.png")
plt.close()

# latency readwhilewriting
fig, ax = plt.subplots()
x1 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%', '100%']
y1 = [208.15,  288.56, 425.44, 1436.22, 2996.52, 9847.09, 43180.63,  485539.24, 0]
x2 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%', '100%']
y2 = [498.92,  667.68, 835.74, 2030.84, 3053.67, 4326.67, 6182.68, 6824.24, 24820]
plt.xlabel("Percentile")
plt.ylabel("Latency (μs)")
plt.title("Put operation tail latency: 1 hour of reads while writing")
plt.yscale('log')
plt.ylim(1, 500000)
# plt.ylim(1, 800000)
plt.plot(x1[:-1], y1[:-1], marker='o', label='RocksDB + F2FS')
plt.plot(x2[:-1], y2[:-1], marker='D', label='RocksDB + ZenFS')
plt.legend()
fig.savefig("out/latency_readwhilewriting.png")
fig.savefig("out/latency_readwhilewriting.svg")
# fig.savefig("out/latency_readwhilewriting_no_log.png")
plt.close()

fig, ax = plt.subplots()
boxes = [
    {
        'label': "F2FS",
        'whislo': 3,    # Bottom whisker position
        'q1': 498.92,    # First quartile (25th percentile)
        'med':  667.68,    # Median         (50th percentile)
        'q3': 835.74,    # Third quartile (75th percentile)
        'whishi': 1340.97,    # Top whisker position
        'fliers': []        # Outliers
    },
    {
        'label': "ZenFS",
        'whislo': 3,    # Bottom whisker position
        'q1': 208.15,    # First quartile (25th percentile)
        'med': 288.56,    # Median         (50th percentile)
        'q3': 425.44,    # Third quartile (75th percentile)
        'whishi': 751.375,    # Top whisker position
        'fliers': []        # Outliers
    }
]
plt.ylim(0, 1500)
ax.bxp(boxes, showfliers=False)
ax.set_ylabel("Latency (μs)")
plt.title("Put operation tail latency: 1 hour of reads while writing")
plt.savefig("out/boxplot_latency_readwhilewriting.png")
plt.close()
