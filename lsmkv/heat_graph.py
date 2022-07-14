import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# sns.set_theme()

y = []
with open('data/heat_data.json', 'r') as file:
    y = json.load(file)['reset']

x = [i for i in range(len(y))]

df = pd.DataFrame(zip(x, y), columns=["x", "y"])

fig, ax = plt.subplots()
plt.stackplot(x, y, colors=["red"])
plt.xlabel("Zone")
plt.ylabel("Physical resets")
plt.title("Resets on SSD")
plt.plot()
fig.savefig("out/heat.png")
plt.close()

# In regions of 100
z = []
zx = []
ind = 0
for i in range(len(y)):
    if i % 100 == 0:
        z.append(0)
        z.append(0)
        zx.append((i // 100) * 100)
        zx.append((i // 100) * 100 + 99)
    ind = 2*(i // 100)
    z[ind] += y[i]
    z[ind+1] += y[i]
fig, ax = plt.subplots()
plt.xlabel("Zones")
plt.ylabel("Physical resets")
plt.title("Resets for each 100 zones")
plt.stackplot(zx, z, colors=["red"])
plt.plot()
fig.savefig("out/heat100.png")
plt.close()

# Check for parts
parts = [{"name": "meta", "begin": 0, "end": 31},
         {"name": "WAL", "begin": 32, "end": 47},
         {"name": "L0", "begin": 48, "end": 377},
         {"name": "LN", "begin": 378, "end": 3688}]

fig, ax = plt.subplots()
part_y = [0, 0, 0, 0]
part_col = ["blue", "blue", "blue", "blue"]
for i in range(len(y)):
    z = 0
    for part in parts:
        if part["begin"] <= i and part["end"] >= i:
            part_y[z] += y[i]
            part_col[z] = "red" if part_y[z] > 5000 else "orange" if part_y[z] > 200 else "blue"
        z += 1
plt.bar([entry["name"] for entry in parts], part_y, color=part_col,
        width=0.4)
plt.xlabel("LSM-tree structure")
plt.ylabel("Physical resets")
plt.title("Resets for each structure")
fig.savefig("out/heatbar.png")
plt.close()

for part in parts:
    part_y = []
    for i in range(len(y)):
        if part["begin"] <= i and part["end"] >= i:
            part_y.append(y[i])
    x = [i + part["begin"] for i in range(len(part_y))]
    fig, ax = plt.subplots()
    plt.ylim(0, 120)
    plt.stackplot(x, part_y, colors=["red"])
    plt.xlabel("Zone")
    plt.ylabel("Physical resets")
    plt.title("Resets for " + part["name"])
    plt.plot()
    fig.savefig("out/heat" + part["name"] + ".png")
    plt.close()

with open('data/written_data.json', 'r') as file:
    y = json.load(file)['written']

x = [i for i in range(len(y))]

df = pd.DataFrame(zip(x, y), columns=["x", "y"])


fig, ax = plt.subplots()
plt.stackplot(x, [y])
plt.plot()
fig.savefig("out/written.png")

z = []
zx = []
ind = 0
for i in range(len(y)):
    if i % 100 == 0:
        z.append(0)
        z.append(0)
        zx.append((i // 100) * 100)
        zx.append((i // 100) * 100 + 99)
    ind = 2*(i // 100)
    z[ind] += y[i]
    z[ind+1] += y[i]
fig, ax = plt.subplots()
plt.stackplot(zx, z, colors=["red"])
plt.xlabel("Zones")
plt.ylabel("Write operations")
plt.title("Write operations for each 100 zones")
plt.plot()
fig.savefig("out/written100.png")
plt.close()

# Check for parts
parts = [{"name": "meta", "begin": 0, "end": 31},
         {"name": "WAL", "begin": 32, "end": 47},
         {"name": "L0", "begin": 48, "end": 377},
         {"name": "LN", "begin": 378, "end": 3687}]

fig, ax = plt.subplots()
part_y = [0, 0, 0, 0]
part_col = ["blue", "blue", "blue", "blue"]
for i in range(len(y)):
    z = 0
    for part in parts:
        if part["begin"] <= i and part["end"] >= i:
            part_y[z] += y[i]
            part_col[z] = "red" if part_y[z] > 50000000 else "orange" if part_y[z] > 10000000 else "blue"
        z += 1
plt.bar([entry["name"] for entry in parts], part_y, color=part_col,
        width=0.4)
plt.xlabel("LSM-tree data structure")
plt.ylabel("Write operations")
plt.title("Write operations for each LSM-tree structure")
fig.savefig("out/writtenbar.png")
plt.close()

for part in parts:
    part_y = []
    for i in range(len(y)):
        if part["begin"] <= i and part["end"] >= i:
            part_y.append(y[i])
    x = [i + part["begin"] for i in range(len(part_y))]
    fig, ax = plt.subplots()
    plt.stackplot(x, part_y, colors=["red"])
    plt.xlabel("Zone")
    plt.ylabel("Write operations")
    plt.title("Writes for " + part["name"])
    plt.plot()
    fig.savefig("out/written" + part["name"] + ".png")
    plt.close()


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
y3 = [4.31,  5.62, 9.32, 355.89, 906.2, 1272.77, 1921.25, 11914.31, 1128431255]

# plt.yscale('log')
for i, j in enumerate([(100000, 6), (100000, 8), (10000000000, 9)]):
    plt.rcParams["figure.figsize"] = (6, 6)
    fig, ax = plt.subplots()
    plt.xlabel("Percentile")
    plt.ylabel("Latency (μs)")
    plt.title("Put Operation tail latency: 1TB of fillrandom")
    plt.ylim(1, j[0])
    plt.yscale('log')
    # plt.ylim(1, 500000)
    plt.plot(x1[:j[1]], y1[:j[1]], marker='o', label='RocksDB + F2FS')
    plt.plot(x2[:j[1]], y2[:j[1]], marker='D', label='RocksDB + ZenFS')
    plt.plot(x3[:j[1]], y3[:j[1]], marker='x', label='ZNSLSM')
    plt.legend()
    fig.savefig("out/latency_fillrandom" + str(i) + ".png")
# fig.savefig("out/latency_fillrandom_no_log.png")
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
x1 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%']
y1 = [6.60,  8.63, 11.46, 33.26, 1245.00, 1617.83, 7419.67, 16785.65]
x2 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%']
y2 = [4.77,  6.43, 8.81, 42.78, 1271.51, 2523.26, 4207.22, 6261.71]
plt.xlabel("Percentile")
plt.ylabel("Latency (μs)")
plt.title("Tail latency: 1TB of overwrites")
plt.yscale('log')
plt.ylim(1, 500000)
# plt.ylim(1, 20000)
plt.plot(x1, y1, marker='o', label='RocksDB + F2FS')
plt.plot(x2, y2, marker='D', label='RocksDB + ZenFS')
plt.legend()
fig.savefig("out/latency_filloverwrite.png")
# fig.savefig("out/latency_filloverwrite_no_log.png")
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
x1 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%']
y1 = [208.15,  288.56, 425.44, 1436.22, 2996.52, 9847.09, 43180.63,  485539.24]
x2 = ['25%', '50%', '75%', '99%', '99.9%', '99.99%', '99.999%', '99.9999%']
y2 = [498.92,  667.68, 835.74, 2030.84, 3053.67, 4326.67, 6182.68, 6824.24]
plt.xlabel("Percentile")
plt.ylabel("Latency (μs)")
plt.title("Tail latency: 1 hour of reads while writing")
plt.yscale('log')
plt.ylim(1, 500000)
# plt.ylim(1, 800000)
plt.plot(x1, y1, marker='o', label='RocksDB + F2FS')
plt.plot(x2, y2, marker='D', label='RocksDB + ZenFS')
plt.legend()
fig.savefig("out/latency_readwhilewriting.png")
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
plt.title("Latency: 1 hour of reads while writing")
plt.savefig("out/boxplot_latency_readwhilewriting.png")
plt.close()


def smartbytes(x): return 1000 * 512 * x


fig, ax = plt.subplots()
labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "ZNSLSM"]
values = [smartbytes(x)
          for x in [(292683188 - 266104226), (355291774 - 325882293)]] + [19690033665024]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 25)
ax.set_ylabel("Write amplification (avg)")
plt.title("FillRandom 1TB: Average total WA normalised over each key-value pair")
plt.savefig("out/barplot_writes_per_put_fillrandom.png")
plt.close()


fig, ax = plt.subplots()
labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "ZNSLSM?"]
values = [smartbytes(x)
          for x in [(324515798 - 292683188), (389576975 - 355291774)]] + [0]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 25)
ax.set_ylabel("Bytes written (avg)")
plt.title(
    "FillOverwrite 1TB: Average number of bytes written for each key-value pair")
plt.savefig("out/barplot_writes_per_put_overwrite.png")
plt.close()

fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))
# 64
values = [24262, 24261, 23809]  # 61763, 60222, 32930
plt.bar([1, 2, 3], values, width=0.125, label="64 queue depth")
# 32
values = [24258, 24263, 23801]  # 61819, 60622, 31863
plt.bar([1.125, 2.125, 3.125], values, width=0.125, label="16 queue depth")
# 16
values = [24260, 24261, 23793]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values, width=0.125, label="4 queue depth")
# 2
values = [24579, 24580, 24067]  # 56265, 58221, 31769
plt.bar([1.375, 2.375, 3.375], values, width=0.125, label="2 queue depth")
# Synchr
values = [24542, 24517, 24299]  # 33638, 55058, 32887
plt.bar([1.5, 2.5, 3.5], values, width=0.125, label="Sequential")

plt.ylim(0, 30000)
plt.xlabel("Value size in bytes")
plt.ylabel("IOPS (avg)")
plt.xticks([1.25, 2.25, 3.25],
           ['200', '400', '2000'])
plt.title("Average IOPS of writing 10GB to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_iops.png")
plt.close()


fig, ax = plt.subplots()
labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "ZNSLSM?"]
values = [smartbytes(x)
          for x in [(324515798 - 292683188), (389576975 - 355291774)]] + [0]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 25)
ax.set_ylabel("Bytes written (avg)")
plt.title(
    "FillOverwrite 1TB: Average number of bytes written for each key-value pair")
plt.savefig("out/barplot_writes_per_put_overwrite.png")
plt.close()

fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))
# 64
stdef = [28.66, 28.70, 31.78]
values = [36.9769, 37.2053, 38.4905]  # 61763, 60222, 32930
plt.bar([1, 2, 3], values, width=0.125, label="64 queue depth", yerr=stdef)
# 32
stdef = [28.53, 28.53, 31.45]
values = [37.2161, 37.3322, 38.5202]  # 61819, 60622, 31863
plt.bar([1.125, 2.125, 3.125], values, width=0.125,
        label="16 queue depth", yerr=stdef)
# 16
stdef = [28.50, 28.51, 31.39]
values = [37.2091, 37.3633, 38.6141]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values, width=0.125,
        label="4 queue depth", yerr=stdef)
# 4
stdef = [27.71, 27.72, 29.84]
values = [36.7517, 36.7893, 38.1423]  # 61819, 60622, 32342
plt.bar([1.375, 2.375, 3.375], values, width=0.125,
        label="2 queue depth", yerr=stdef)
# Synchr
stdef = [24.39, 24.40, 21.43]
values = [36.7812, 36.6876, 37.7373]  # 33638, 55058, 32887
plt.bar([1.5, 2.5, 3.5], values, width=0.125,
        label="Sequential", yerr=stdef)
plt.ylim(0, 80)
plt.xlabel("Value size in bytes")
plt.ylabel("Average completion time (μs)")
plt.xticks([1.25, 2.25, 3.25],
           ['200', '400', '2000'])
plt.title(
    "Average completion time of each IO operation while writing 10GB to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_latency.png")
plt.close()


fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))
# 64
values = [61763, 60222, 32930]
plt.bar([1, 2, 3], values, width=0.125, label="64 queue depth")
# 32
values = [61819, 60622, 31863]
plt.bar([1.125, 2.125, 3.125], values, width=0.125, label="16 queue depth")
# 16
values = [61680, 59828, 32342]
plt.bar([1.25, 2.25, 3.25], values, width=0.125, label="4 queue depth")
# 2
values = [56265, 58221, 31769]
plt.bar([1.375, 2.375, 3.375], values, width=0.125, label="2 queue depth")
# Synchr
values = [33638, 55058, 32887]
plt.bar([1.5, 2.5, 3.5], values, width=0.125, label="Sequential")

plt.ylim(0, 70000)
plt.xlabel("Value size in bytes")
plt.ylabel("IOPS (avg)")
plt.xticks([1.25, 2.25, 3.25],
           ['8000', '16000', '32000'])
plt.title("Average IOPS of writing 10GB to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_iops_high.png")
plt.close()

fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))
# 64
stdef = [10.09, 28.89, 68.29]
values = [12.3650, 11.3539, 24.3204]  # 61763, 60222, 32930
plt.bar([1, 2, 3], values, width=0.125, label="64 queue depth", yerr=stdef)
# 32
stdef = [9.11, 30.84, 35.59]
values = [12.2958, 11.20302, 23.8632]  # 61819, 60622, 31863
plt.bar([1.125, 2.125, 3.125], values, width=0.125,
        label="16 queue depth", yerr=stdef)
# 16
stdef = [9.92, 25.54, 42.46]
values = [12.3287, 11.2932, 23.8656]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values, width=0.125,
        label="4 queue depth", yerr=stdef)
# 4
stdef = [9.38, 19.70, 27.77]
values = [13.8938, 11.3635, 23.7364]  # 61819, 60622, 32342
plt.bar([1.375, 2.375, 3.375], values, width=0.125,
        label="2 queue depth", yerr=stdef)
# Synchr
stdef = [5.13, 4.26, 19.91]
values = [25.8135, 13.0344, 24.2820]  # 33638, 55058, 32887
plt.bar([1.5, 2.5, 3.5], values, width=0.125,
        label="Sequential", yerr=stdef)
plt.ylim(0, 80)
plt.xlabel("Value size in bytes")
plt.ylabel("Average completion time (μs)")
plt.xticks([1.25, 2.25, 3.25],
           ['8000', '16000', '32000'])
plt.title(
    "Average completion time of each IO operation while writing 10GB to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_latency_high.png")
plt.close()

fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))
# 64
values = [226572, 230292, 185178]  # 61763, 60222, 32930
plt.bar([1, 2, 3], values, width=0.125, label="64 queue depth")
# 32
values = [221859, 228010, 182036]  # 61819, 60622, 31863
plt.bar([1.125, 2.125, 3.125], values, width=0.125, label="16 queue depth")
# 16
values = [219887, 226360, 177611]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values, width=0.125, label="4 queue depth")
# 2
values = [227383, 229885, 184373]  # 56265, 58221, 31769
plt.bar([1.375, 2.375, 3.375], values, width=0.125, label="2 queue depth")
# Synchr
values = [222425, 220285, 157666]  # 33638, 55058, 32887
plt.bar([1.5, 2.5, 3.5], values, width=0.125, label="Sequential")

plt.ylim(0, 300000)
plt.xlabel("Value size in bytes")
plt.ylabel("IOPS (avg)")
plt.xticks([1.25, 2.25, 3.25],
           ['200', '400', '2000'])
plt.title("Average IOPS of writing 10GB (with ZASL buffer) to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_iops_buffering.png")
plt.close()

fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))
# 64
values = [103324, 59999, 31540]
plt.bar([1, 2, 3], values, width=0.125, label="64 queue depth")
# 32
values = [104591, 57909, 28711]
plt.bar([1.125, 2.125, 3.125], values, width=0.125, label="16 queue depth")
# 16
values = [105171, 60276, 28191]
plt.bar([1.25, 2.25, 3.25], values, width=0.125, label="4 queue depth")
# 2
values = [105515, 56667, 31611]
plt.bar([1.375, 2.375, 3.375], values, width=0.125, label="2 queue depth")
# Synchr
values = [82947, 41459, 22375]
plt.bar([1.5, 2.5, 3.5], values, width=0.125, label="Sequential")
plt.ylim(0, 120000)
plt.xlabel("Value size in bytes")
plt.ylabel("IOPS (avg)")
plt.xticks([1.25, 2.25, 3.25],
           ['8000', '16000', '32000'])
plt.title("Average IOPS of writing 10GB (with ZASL buffer) to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_iops_high_buffering.png")
plt.close()


fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))
# 16
values = [24260, 24261, 25188, 23793, 48555,
          61680, 59828, 34432, 32342, 23160, 15893, 7553]
plt.bar([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5],
        values, width=0.1, label="4 queue depth")
# seq
values = [24542, 24517, 25548, 24299, 41530,
          33638, 55058, 28235, 32887, 21401, 15895, 7430]
plt.bar([1.1, 1.6, 2.1, 2.6, 3.1, 3.6, 4.1, 4.6, 5.1, 5.6, 6.1, 6.6],
        values, width=0.1, label="Sequential")
plt.ylim(0, 80000)
plt.xlabel("Value size in bytes")
plt.ylabel("IOPS (avg)")
plt.xticks([1.05, 1.55, 2.05, 2.55, 3.05, 3.55, 4.05, 4.55, 5.05, 5.55, 6.05, 6.55],
           ['200', '400', '1000', '2000', '4000', '8000', '16000', '24000', '32000', '40000', '64000', '128000'])
plt.title("Average IOPS of writing 10GB to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_iops_gaps.png")
plt.close()


fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))
# 16
yerr = [28.50, 28.51, 28.84, 31.39, 11.62, 9.92,
        25.54, 46.13, 42.46, 87.28, 68.33, 111.51]
values = [37.2091, 37.3633, 36.2462, 38.6141, 16.8991, 12.3287, 11.2932,
          22.1261, 23.8656, 36.0827, 50.8736, 112.2216]
plt.bar([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5],
        values, width=0.1, label="4 queue depth", yerr=yerr)
# seq
yerr = [24.39, 24.40, 21.20, 21.43, 7.66, 5.13,
        4.26, 8.28, 19.91, 47.38, 45.03, 102.81]
values = [36.7812, 36.6876, 35.7627, 37.7373, 20.5750, 25.8135, 13.0344,
          29.4640, 24.2820, 40.0521, 51.4294, 115.6497]
plt.bar([1.1, 1.6, 2.1, 2.6, 3.1, 3.6, 4.1, 4.6, 5.1, 5.6, 6.1, 6.6],
        values, width=0.1, label="Sequential", yerr=yerr)
plt.ylim(0, 250)
plt.xlabel("Value size in bytes")
plt.ylabel("Average completion time (μs)")
plt.xticks([1.05, 1.55, 2.05, 2.55, 3.05, 3.55, 4.05, 4.55, 5.05, 5.55, 6.05, 6.55],
           ['200', '400', '1000', '2000', '4000', '8000', '16000', '24000', '32000', '40000', '64000', '128000'])
plt.title("Average IOPS of writing 10GB to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_lat_gaps.png")
plt.close()
