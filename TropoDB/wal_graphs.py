import matplotlib.pyplot as plt
import statistics

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


# Synchr
values = [24542, 24517, 24299]  # 33638, 55058, 32887
plt.bar([1, 2, 3], [value / 1000 for value in values],
        width=0.125, label="QD 1")
# 2
values = [24579, 24580, 24067]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], [value / 1000 for value in values],
        width=0.125, label="QD 2")
# 16
values = [24260, 24261, 23793]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], [value / 1000 for value in values],
        width=0.125, label="QD 4")
# 32
values = [24258, 24263, 23801]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], [value / 1000 for value in values],
        width=0.125, label="QD 16")
# 64
values = [24262, 24261, 23809]  # 61763, 60222, 32930
plt.bar([1.5, 2.5, 3.5], [value / 1000 for value in values],
        width=0.125, label="QD 64")

plt.ylim(0, 30000 / 1000)
plt.xlabel("Value size in bytes")
plt.ylabel("KIOPS)")
plt.xticks([1.25, 2.25, 3.25],
           ['200', '400', '2kB'])
plt.title("Average KIOPS while writing 10GB to the WAL")
plt.legend(ncol=2)
plt.savefig("out/barplot_wal_iops.png")
plt.savefig("out/barplot_wal_iops.svg")
plt.close()


# Synchr
values = [24542, 24517, 33638, 32887]  # 33638, 55058, 32887
plt.bar([1, 2, 3, 4], [value / 1000 for value in values],
        width=0.125, label="QD 1")
# 2
values = [24579, 24580, 56265, 31769]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125, 4.125], [value / 1000 for value in values],
        width=0.125, label="QD 2")
# 16
values = [24260, 24261, 61680, 32342]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25, 4.25], [value / 1000 for value in values],
        width=0.125, label="QD 4")
# 32
values = [24258, 24263, 61819, 31863]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375, 4.375], [value / 1000 for value in values],
        width=0.125, label="QD 16")
# 64
values = [24262, 24261, 61763, 32930]  # 61763, 60222, 32930
plt.bar([1.5, 2.5, 3.5, 4.5], [value / 1000 for value in values],
        width=0.125, label="QD 64")

plt.ylim(0, 80000 / 1000)
plt.xlabel("Value size in bytes")
plt.ylabel("KIOPS")
plt.xticks([1.25, 2.25, 3.25, 4.25],
           ['200', '400', '8000', '32000'])
plt.title("Average KIOPS while writing 10GB to the WAL")
plt.legend(ncol=1)
plt.savefig("out/barplot_wal_iops_2.png")
plt.savefig("out/barplot_wal_iops_2.svg")
plt.close()


fig, ax = plt.subplots()
# plt.figure(figsize=(12, 12))
# Synchr
stdef = [24.39, 24.40, 21.43]
values = [36.7812, 36.6876, 37.7373]  # 33638, 55058, 32887
plt.bar([1, 2, 3], values, width=0.125,
        label="QD 1", yerr=stdef)
# 4
stdef = [27.71, 27.72, 29.84]
values = [36.7517, 36.7893, 38.1423]  # 61819, 60622, 32342
plt.bar([1.125, 2.125, 3.125], values, width=0.125,
        label="QD 2", yerr=stdef)
# 16
stdef = [28.50, 28.51, 31.39]
values = [37.2091, 37.3633, 38.6141]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values, width=0.125,
        label="QD 4", yerr=stdef)
# 32
stdef = [28.53, 28.53, 31.45]
values = [37.2161, 37.3322, 38.5202]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], values, width=0.125,
        label="QD 16", yerr=stdef)
# 64
stdef = [28.66, 28.70, 31.78]
values = [36.9769, 37.2053, 38.4905]  # 61763, 60222, 32930
plt.bar([1.5, 2.5, 3.5], values, width=0.125, label="QD 64", yerr=stdef)

plt.ylim(0, 100)
plt.xlabel("Value size (bytes)")
plt.ylabel("Completion time (μs)")
plt.xticks([1.25, 2.25, 3.25],
           ['200', '400', '2kB'])
plt.title(
    "Average completion time of WAL appends")
plt.legend(loc='upper left', ncol=1)
plt.savefig("out/barplot_wal_latency.png")
plt.savefig("out/barplot_wal_latency.svg")
plt.close()


fig, ax = plt.subplots()
# plt.figure(figsize=(12, 12))
# Synchr
stdef = [24.39, 24.40, 5.13, 19.91]
values = [36.7812, 36.6876, 25.8135, 24.2820]  # 33638, 55058, 32887
plt.bar([1, 2, 3, 4], values, width=0.125,
        label="QD 1", yerr=stdef)
# 4
stdef = [27.71, 27.72, 9.38, 27.77]
values = [36.7517, 36.7893, 13.8938, 23.7364]  # 61819, 60622, 32342
plt.bar([1.125, 2.125, 3.125, 4.125], values, width=0.125,
        label="QD 2", yerr=stdef)
# 16
stdef = [28.50, 28.51, 9.92, 42.46]
values = [37.2091, 37.3633, 12.3287, 23.8656]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25, 4.25], values, width=0.125,
        label="QD 4", yerr=stdef)
# 32
stdef = [28.53, 28.53,  9.11, 35.59]
values = [37.2161, 37.3322, 12.2958, 23.8632]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375, 4.375], values, width=0.125,
        label="QD 16", yerr=stdef)
# 64
stdef = [28.66, 28.70, 10.09, 68.29]
values = [36.9769, 37.2053, 12.3650, 24.3204]  # 61763, 60222, 32930
plt.bar([1.5, 2.5, 3.5, 4.5], values, width=0.125, label="QD 64", yerr=stdef)

plt.ylim(0, 100)
plt.xlabel("Value size (bytes)")
plt.ylabel("Completion time (μs)")
plt.xticks([1.25, 2.25, 3.25, 4.25],
           ['200', '400', '8000', '32000'])
plt.title(
    "Average completion time of WAL appends")
plt.legend(loc='upper left', ncol=1)
plt.savefig("out/barplot_wal_latency_2.png")
plt.savefig("out/barplot_wal_latency_2.svg")
plt.close()


fig, ax = plt.subplots()
# plt.figure(figsize=(12, 12))
# Synchr
values = [33638, 55058, 32887]
plt.bar([1, 2, 3], [value / 1000 for value in values],
        width=0.125, label="QD 1")
# 2
values = [56265, 58221, 31769]
plt.bar([1.125, 2.125, 3.125], [value / 1000 for value in values],
        width=0.125, label="QD 2")
# 16
values = [61680, 59828, 32342]
plt.bar([1.25, 2.25, 3.25], [value / 1000 for value in values],
        width=0.125, label="QD 4")
# 32
values = [61819, 60622, 31863]
plt.bar([1.375, 2.375, 3.375], [value / 1000 for value in values],
        width=0.125, label="QD 16")
# 64
values = [61763, 60222, 32930]
plt.bar([1.5, 2.5, 3.5], [value / 1000 for value in values],
        width=0.125, label="QD 64")

plt.ylim(0, 70000/1000)
plt.xlabel("Value size (bytes)")
plt.ylabel("KIOPS")
plt.xticks([1.25, 2.25, 3.25],
           ['8kB', '16kB', '32kB'])
plt.title("Average KIOPS while writing 10GB to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_iops_high.png")
plt.savefig("out/barplot_wal_iops_high.svg")
plt.close()

fig, ax = plt.subplots()
# plt.figure(figsize=(12, 12))

# Synchr
stdef = [5.13, 4.26, 19.91]
values = [25.8135, 13.0344, 24.2820]  # 33638, 55058, 32887
plt.bar([1, 2, 3], values, width=0.125,
        label="QD 1", yerr=stdef)
# 4
stdef = [9.38, 19.70, 27.77]
values = [13.8938, 11.3635, 23.7364]  # 61819, 60622, 32342
plt.bar([1.125, 2.125, 3.125], values, width=0.125,
        label="QD 2", yerr=stdef)
# 16
stdef = [9.92, 25.54, 42.46]
values = [12.3287, 11.2932, 23.8656]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values, width=0.125,
        label="QD 4", yerr=stdef)
# 32
stdef = [9.11, 30.84, 35.59]
values = [12.2958, 11.20302, 23.8632]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], values, width=0.125,
        label="QD 16", yerr=stdef)
# 64
stdef = [10.09, 28.89, 68.29]
values = [12.3650, 11.3539, 24.3204]  # 61763, 60222, 32930
plt.bar([1.5, 2.5, 3.5], values, width=0.125, label="QD 64", yerr=stdef)

plt.ylim(0, 100)
plt.xlabel("Value size (bytes)")
plt.ylabel("Completion time (μs)")
plt.xticks([1.25, 2.25, 3.25],
           ['8kB', '16kB', '32kB'])
plt.title(
    "Average completion time of WAL appends")
plt.legend(loc='upper left')
plt.savefig("out/barplot_wal_latency_high.png")
plt.savefig("out/barplot_wal_latency_high.svg")
plt.close()

fig, ax = plt.subplots()
# plt.figure(figsize=(12, 12))
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
        values, width=0.1, label="queue depth 4", yerr=yerr)
# seq
yerr = [24.39, 24.40, 21.20, 21.43, 7.66, 5.13,
        4.26, 8.28, 19.91, 47.38, 45.03, 102.81]
values = [36.7812, 36.6876, 35.7627, 37.7373, 20.5750, 25.8135, 13.0344,
          29.4640, 24.2820, 40.0521, 51.4294, 115.6497]
plt.bar([1.1, 1.6, 2.1, 2.6, 3.1, 3.6, 4.1, 4.6, 5.1, 5.6, 6.1, 6.6],
        values, width=0.1, label="queue depth 1 (ordered)", yerr=yerr)
plt.ylim(0, 250)
plt.xlabel("Value size in bytes")
plt.ylabel("Average completion time (μs)")
plt.xticks([1.05, 1.55, 2.05, 2.55, 3.05, 3.55, 4.05, 4.55, 5.05, 5.55, 6.05, 6.55],
           ['200', '400', '1000', '2000', '4000', '8000', '16000', '24000', '32000', '40000', '64000', '128000'])
plt.title("Average IOPS of writing 10GB to the WAL")
plt.legend()
plt.savefig("out/barplot_wal_lat_gaps.png")
plt.close()


fig, ax = plt.subplots()
plt.figure(figsize=(12, 12))

y_unordered = [[
    43171067,
    43608040,
    43172647,
    43192477,
    43703552
], [
    46549003,
    47910537,
    47988483,
    47991897,
    48323521
], [
    28191653,
    28488281,
    27567016,
    28212795,
    28505716,
], [
    19640664,
    19726943,
    19767840,
    19625286,
    19706219
], [
    15039423,
    14731939,
    14907952,
    14925141,
    14881599
], [
    13787266,
    13706974,
    14196971,
    14208654,
    14140125
], [
    12646038,
    12666334,
    12953993,
    12965410,
    13214671
], [
    12496745,
    12298487,
    12473137,
    12316150,
    12250822
], [
    11785615,
    11648187,
    11682160,
    11757215,
    11877507
]]

y_ordered = [[
    41570512,
    42326545,
    42257784,
    42182269,
    42091044
], [
    42465667,
    43890479,
    43765310,
    44529348,
    44161847
], [
    25930732,
    25715867,
    26177273,
    25981125,
    26177085
], [
    17723918,
    17611525,
    17630803,
    17538616,
    17400160
], [
    12952033,
    12985535,
    13042471,
    13061892,
    13119968
], [
    11751736,
    11703664,
    11674258,
    11829055,
    11589770
], [
    10704553,
    10613679,
    10930267,
    10925442,
    10928569
], [
    10352240,
    10347224,
    10325567,
    10398895,
    10388718
], [
    9914162,
    9860935,
    9860935,
    9836303,
    9788460
]
]

y_unordered = [[yy / 1000 for yy in y] for y in y_unordered]
y_ordered = [[yy / 1000 for yy in y] for y in y_ordered]

# 16
yerr = [statistics.stdev(sample) for sample in y_unordered]
values = [statistics.mean(sample) for sample in y_unordered]
plt.bar([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, ],
        values, width=0.1, label="Unordered WAL (queue depth 4)", yerr=yerr)
# seq
yerr = [statistics.stdev(sample) for sample in y_ordered]
values = [statistics.mean(sample) for sample in y_ordered]
plt.bar([1.1, 1.6, 2.1, 2.6, 3.1, 3.6, 4.1, 4.6, 5.1],
        values, width=0.1, label="Ordered WAL", yerr=yerr)
# plt.ylim(0, 250)
plt.xlabel("Value size in bytes for each entry in the WAL")
plt.ylabel("Average replay time (ms)")
plt.xticks([1.05, 1.55, 2.05, 2.55, 3.05, 3.55, 4.05, 4.55, 5.05],
           ['200', '400', '1000', '2000', '4000', '8000', '16000', '32000', '128000'])
plt.title("Average latency replaying 3GB of WAL data")
plt.legend()
plt.savefig("out/barplot_wal_recover.png")
plt.savefig("out/barplot_wal_recover.svg")
plt.close()


# 16
yerr = [statistics.stdev(sample) for sample in y_unordered][:4]
values = [statistics.mean(sample) for sample in y_unordered][:4]
plt.bar([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, ][:4],
        values, width=0.1, label="Unordered WAL (queue depth 4)", yerr=yerr)
# seq
yerr = [statistics.stdev(sample) for sample in y_ordered][:4]
values = [statistics.mean(sample) for sample in y_ordered][:4]
plt.bar([1.1, 1.6, 2.1, 2.6, 3.1, 3.6, 4.1, 4.6, 5.1][:4],
        values, width=0.1, label="Ordered WAL", yerr=yerr)
# plt.ylim(0, 250)
plt.xlabel("Value size in bytes for each entry in the WAL")
plt.ylabel("Average replay time (ms)")
plt.xticks([1.05, 1.55, 2.05, 2.55, 3.05, 3.55, 4.05, 4.55, 5.05][:4],
           ['200', '400', '1000', '2000', '4000', '8000', '16000', '32000', '128000'][:4])
plt.title("Average latency replaying 3GB of WAL data")
plt.legend()
plt.savefig("out/barplot_wal_recover_lower.png")
plt.savefig("out/barplot_wal_recover_lower.svg")
plt.close()


yerr = [statistics.stdev(sample) for sample in y_unordered][4:]
values = [statistics.mean(sample) for sample in y_unordered][4:]
plt.bar([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, ][4:],
        values, width=0.1, label="Unordered WAL (queue depth 4)", yerr=yerr)
# seq
yerr = [statistics.stdev(sample) for sample in y_ordered][4:]
values = [statistics.mean(sample) for sample in y_ordered][4:]
plt.bar([1.1, 1.6, 2.1, 2.6, 3.1, 3.6, 4.1, 4.6, 5.1][4:],
        values, width=0.1, label="Ordered WAL", yerr=yerr)
# plt.ylim(0, 250)
plt.xlabel("Value size in bytes for each entry in the WAL")
plt.ylabel("Average replay time (ms)")
plt.xticks([1.05, 1.55, 2.05, 2.55, 3.05, 3.55, 4.05, 4.55, 5.05][4:],
           ['200', '400', '1000', '2000', '4000', '8000', '16000', '32000', '128000'][4:])
plt.title("Average latency replaying 3GB of WAL data")
plt.legend()
plt.savefig("out/barplot_wal_recover_higher.png")
plt.savefig("out/barplot_wal_recover_higher.svg")
plt.close()
