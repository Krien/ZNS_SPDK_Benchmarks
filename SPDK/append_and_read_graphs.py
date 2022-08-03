import matplotlib.pyplot as plt

# NOTE values are copied from the data directory. This is not done automatically.

yerr = [x/1000 for x in [213.91, 492.77, 635.50, 693.18]][:4]
values = [x/1000 for x in [34049.59, 57076.92, 62346.82, 62465.23]][:4]
plt.bar([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, ][:4],
        values, width=0.1, label="Appends", yerr=yerr)
# seq
yerr = [x/1000 for x in [1548.21, 770.42, 567.71, 342.19]][:4]
values = [x/1000 for x in [55782.72, 68886.76, 70489.70, 68861.41]][:4]
plt.bar([1.1, 1.6, 2.1, 2.6, 3.1, 3.6, 4.1, 4.6, 5.1][:4],
        values, width=0.1, label="Writes", yerr=yerr)
# plt.ylim(0, 250)
plt.xlabel("Writers")
plt.ylabel("KIOPS")
plt.xticks([1.05, 1.55, 2.05, 2.55, 3.05, 3.55, 4.05, 4.55, 5.05][:4],
           ['1', '2', '3', '4', '4000', '8000', '16000', '32000', '128000'][:4])
plt.title("IOPS ")
plt.legend()
plt.savefig("out/barplot_spdk_write.png")
plt.savefig("out/barplot_spdk_write.svg")
plt.close()


fig, ax = plt.subplots()
# 1
yerr = [79.13, 213.91, 331.56]
values = [27490.97, 34049.59, 32903.73]  # 33638, 55058, 32887
plt.bar([1, 2, 3], [value / 1000 for value in values],
        width=0.125, label="QD 1", yerr=[yerr / 1000 for yerr in yerr])
# 2
yerr = [117.08, 492.77, 406.26]
values = [27433.77, 57076.92, 33072.98]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], [value / 1000 for value in values],
        width=0.125, label="QD 2", yerr=[yerr / 1000 for yerr in yerr])
# 3
yerr = [99.90, 693.18, 366.98]
values = [27231.31, 62465.23, 33202.90]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], [value / 1000 for value in values],
        width=0.125, label="QD 3", yerr=[yerr / 1000 for yerr in yerr])
# 4
yerr = [112.43, 635.50, 268.41]
values = [27208.62, 62346.82, 32779.65]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], [value / 1000 for value in values],
        width=0.125, label="QD 4", yerr=[yerr / 1000 for yerr in yerr])


plt.ylim(0, 80000 / 1000)
plt.xlabel("Block size in bytes")
plt.ylabel("KIOPS")
plt.xticks([1.187, 2.187, 3.187],
           ['1kB', '8kB', '32kB'])
plt.title(
    "Average throughput (KIOPS) for appends")
plt.legend(ncol=1)
plt.savefig("out/barplot_spdk_append.png")
plt.savefig("out/barplot_spdk_append.svg")
plt.close()

fig, ax = plt.subplots()
# 1
yerr = [18.53, 3.85, 34.19]
values = [35.93, 28.90, 29.67]  # 33638, 55058, 32887
plt.bar([1, 2, 3], values,
        width=0.125, label="QD 1", yerr=yerr)
# 2
yerr = [34.09, 12.93, 121.21]
values = [72.47, 34.52, 59.48]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], values,
        width=0.125, label="QD 2", yerr=yerr)
# 3
yerr = [40.56, 18.22, 157.88]
values = [109.78, 47.44, 89.05]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values,
        width=0.125, label="QD 3", yerr=yerr)
# 4
yerr = [43.12, 19.72, 200.55]
values = [146.59, 63.48, 120.42]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], values,
        width=0.125, label="QD 4", yerr=yerr)
plt.ylim(0, 400)
plt.xlabel("Block size in bytes")
plt.ylabel("Latency (μs)")
plt.xticks([1.187, 2.187, 3.187],
           ['1kB', '8kB', '32kB'])
plt.title(
    "Average latency (μs) for appends")
plt.legend(loc='upper left', ncol=1)
plt.savefig("out/barplot_spdk_append_lat.png")
plt.savefig("out/barplot_spdk_append_lat.svg")
plt.close()


fig, ax = plt.subplots()
# 1
yerr = [109.18, 193.52, 312.96]
values = [27859.90, 55782.72, 33347.62]  # 33638, 55058, 32887
plt.bar([1, 2, 3], [value / 1000 for value in values],
        width=0.125, label="1 writer", yerr=[yerr / 1000 for yerr in yerr])
# 2
yerr = [77.27, 770.42, 3219.06]
values = [27675.7, 68886.76, 36323.72]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], [value / 1000 for value in values],
        width=0.125, label="2 writers", yerr=[yerr / 1000 for yerr in yerr])
# 3
yerr = [68.43, 567.71, 364.54]
values = [27588.07, 70489.70, 48548.35]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], [value / 1000 for value in values],
        width=0.125, label="3 writers", yerr=[yerr / 1000 for yerr in yerr])
# 4
yerr = [59.16, 635.50, 2151.67]
values = [27769.88, 68861.41, 48973.57]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], [value / 1000 for value in values],
        width=0.125, label="4 writers", yerr=[yerr / 1000 for yerr in yerr])
plt.ylim(0, 80000 / 1000)
plt.xlabel("Block size in bytes")
plt.ylabel("KIOPS")
plt.xticks([1.187, 2.187, 3.187],
           ['1kB', '8kB', '32kB'])
plt.title(
    "Average throughput (KIOPS) for writes")
plt.legend(ncol=1)
plt.savefig("out/barplot_spdk_writes.png")
plt.savefig("out/barplot_spdk_writes.svg")
plt.close()


fig, ax = plt.subplots()
# 1
yerr = [21.94, 3.03, 45.82]
values = [35.48, 17.52, 29.42]  # 33638, 55058, 32887
plt.bar([1, 2, 3], values,
        width=0.125, label="1 writer", yerr=yerr)
# 2
yerr = [46.29, 15.04, 104.22]
values = [71.78, 28.50, 54.33]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], values,
        width=0.125, label="2 writers", yerr=yerr)
# 3
yerr = [66.39, 24.69, 66.22]
values = [108.20, 41.90, 61.00]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values,
        width=0.125, label="3 writers", yerr=yerr)
# 4
yerr = [86.46, 41.05, 91.36]
values = [143.52, 57.41, 80.72]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], values,
        width=0.125, label="4 writers", yerr=yerr)
plt.ylim(0, 400)
plt.xlabel("Block size in bytes")
plt.ylabel("Latency (μs)")
plt.xticks([1.187, 2.187, 3.187],
           ['1kB', '8kB', '32kB'])
plt.title(
    "Average latency (μs) for writes")
plt.legend(loc='upper left', ncol=1)
plt.savefig("out/barplot_spdk_writes_lat.png")
plt.savefig("out/barplot_spdk_writes_lat.svg")
plt.close()


fig, ax = plt.subplots()
# 1
yerr = [3655.24, 1835.50, 506.20]
values = [149793.61, 111679.39, 56645.98]  # 33638, 55058, 32887
plt.bar([1, 2, 3], [value / 1000 for value in values],
        width=0.125, label="QD 1", yerr=[yerr / 1000 for yerr in yerr])
# 2
yerr = [8742.02, 2768.35, 360.31]
values = [291532.98, 193369.15, 71788.96]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], [value / 1000 for value in values],
        width=0.125, label="QD 2", yerr=[yerr / 1000 for yerr in yerr])
# 3
yerr = [10793.87, 1987.17, 335.18]
values = [361486.87, 279214.94, 71218.15]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], [value / 1000 for value in values],
        width=0.125, label="QD 3", yerr=[yerr / 1000 for yerr in yerr])
# 4
yerr = [11425.43, 2545.25, 344.73]
values = [378477.20, 273810.92, 70719.80]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], [value / 1000 for value in values],
        width=0.125, label="QD 4", yerr=[yerr / 1000 for yerr in yerr])
plt.ylim(0, 400000 / 1000)
plt.xlabel("Block size in bytes")
plt.ylabel("KIOPS")
plt.xticks([1.187, 2.187, 3.187],
           ['1kB', '8kB', '32kB'])
plt.title(
    "Average throughput (KIOPS) for sequential reads")
plt.legend(ncol=1)
plt.savefig("out/barplot_spdk_reads.png")
plt.savefig("out/barplot_spdk_reads.svg")
plt.close()


fig, ax = plt.subplots()
# 1
yerr = [1.28, 3.21, 7.02]
values = [6.34, 8.63, 17.27]  # 33638, 55058, 32887
plt.bar([1, 2, 3], values,
        width=0.125, label="QD 1", yerr=yerr)
# 2
yerr = [2.07, 5.15, 31.46]
values = [6.53, 10.02, 27.51]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], values,
        width=0.125, label="QD 2", yerr=yerr)
# 3
yerr = [2.75, 11.29, 46.55]
values = [7.98, 10.41, 41.78]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values,
        width=0.125, label="QD 3", yerr=yerr)
# 4
yerr = [3.66, 32.31, 60.66]
values = [10.23, 14.29, 56.22]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], values,
        width=0.125, label="QD 4", yerr=yerr)
plt.ylim(0, 150)
plt.xlabel("Block size in bytes")
plt.ylabel("Latency (μs)")
plt.xticks([1.187, 2.187, 3.187],
           ['1kB', '8kB', '32kB'])
plt.title(
    "Average latency (μs) for sequential reads")
plt.legend(loc='upper left', ncol=1)
plt.savefig("out/barplot_spdk_reads_lat.png")
plt.savefig("out/barplot_spdk_reads_lat.svg")
plt.close()


fig, ax = plt.subplots()
# 1
yerr = [45.92, 32.13, 29.20]
values = [12436.92, 10767.85, 6238.05]  # 33638, 55058, 32887
plt.bar([1, 2, 3], [value / 1000 for value in values],
        width=0.125, label="1 reader", yerr=[yerr / 1000 for yerr in yerr])
# 2
yerr = [37.44, 30.81, 28.93]
values = [24643.39, 21268.68, 12154.39]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], [value / 1000 for value in values],
        width=0.125, label="2 readers", yerr=[yerr / 1000 for yerr in yerr])
# 3
yerr = [44.05, 32.09, 29.11]
values = [36619.62, 31518.47, 17775.61]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], [value / 1000 for value in values],
        width=0.125, label="3 readers", yerr=[yerr / 1000 for yerr in yerr])
# 4
yerr = [41.64, 35.69, 28.31]
values = [48382.50, 41537.04, 23089.27]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], [value / 1000 for value in values],
        width=0.125, label="4 readers", yerr=[yerr / 1000 for yerr in yerr])
plt.ylim(0, 100000 / 1000)
plt.xlabel("Block size in bytes")
plt.ylabel("KIOPS")
plt.xticks([1.187, 2.187, 3.187],
           ['1kB', '8kB', '32kB'])
plt.title(
    "Average throughput (KIOPS) for random reads among threads (QD=1)")
plt.legend(ncol=1)
plt.savefig("out/barplot_spdk_reads_random.png")
plt.savefig("out/barplot_spdk_reads_random.svg")
plt.close()


fig, ax = plt.subplots()
# 1
yerr = [13.87, 5.61, 35.33]
values = [79.85, 92.33, 159.82]  # 33638, 55058, 32887
plt.bar([1, 2, 3], values,
        width=0.125, label="1 reader", yerr=yerr)
# 2
yerr = [7.09, 7.91, 38.03]
values = [80.55, 93.44, 163.94]  # 56265, 58221, 31769
plt.bar([1.125, 2.125, 3.125], values,
        width=0.125, label="2 readers", yerr=yerr)
# 3
yerr = [10.20, 10.94, 41.22]
values = [81.25, 94.52, 168.06]  # 61680, 59828, 31863
plt.bar([1.25, 2.25, 3.25], values,
        width=0.125, label="3 readers", yerr=yerr)
# 4
yerr = [10.39, 11.32, 43.90]
values = [82.01, 95.68, 172.47]  # 61819, 60622, 31863
plt.bar([1.375, 2.375, 3.375], values,
        width=0.125, label="4 readers", yerr=yerr)
plt.ylim(0, 250)
plt.xlabel("Block size in bytes")
plt.ylabel("Latency (μs)")
plt.xticks([1.187, 2.187, 3.187],
           ['1kB', '8kB', '32kB'])
plt.title(
    "Average latency (μs) for random reads among threads (QD=1)")
plt.legend(loc='upper left', ncol=1)
plt.savefig("out/barplot_spdk_reads_random_lat.png")
plt.savefig("out/barplot_spdk_reads_random_lat.svg")
plt.close()
