import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# plt.figure(figsize=(12, 12))

reswrong = [7*60 + 32, 3*60 + 49, 60 + 53, 51, 32, 22][:3]
rescor   = [7*60 + 27, 3*60+48, 60+57, 52, 34, 21][:3]
pinned2  = [8*60 + 21, 4*60+26, 2*60+19, 72, 46, 29][:3]
qemupin  = [8*60+27, 4*60+8, 2*60+1, 57, 37, 22][:3]
nocontrl = [7*60+44, 4*60+10, 60+59, 55, 34, 22][:3]
x = [1, 2, 3, 4, 5, 6][:3]
#plt.yscale('log')
plt.plot(x, reswrong, label="Wrong NUMA node pinned")
plt.plot(x, rescor, label="Correct NUMA node pinned")
plt.plot(x, pinned2, label="Both NUMA nodes pinned")
plt.plot(x, qemupin, label="NUMA pinned within VM")
plt.plot(x, nocontrl, label="No control over NUMA")
plt.xticks([1,      2,     3,     4,      5,      6][:3],
           ['100', '200', '400', '1000', '2000', '8000'][:3])
plt.legend(loc='upper right', ncol=1)
plt.xlabel("Value size in byte")
plt.ylabel("Completion time (s)")
plt.title("Completion time ZenFS 100GB of fillrandom")
plt.savefig("out/line_numa.png")
plt.savefig("out/line_numa.svg")
plt.close()

fig, ax = plt.subplots()
reswrong = [7*60 + 32, 3*60 + 49, 60 + 53, 51, 32, 22][3:]
rescor   = [7*60 + 27, 3*60+48, 60+57, 52, 34, 21][3:]
pinned2  = [8*60 + 21, 4*60+26, 2*60+19, 72, 46, 29][3:]
qemupin  = [8*60+27, 4*60+8, 2*60+1, 57, 37, 22][3:]
nocontrl = [7*60+44, 4*60+10, 60+59, 55, 34, 22][3:]
x = [1, 2, 3, 4, 5, 6][3:]
#plt.yscale('log')
plt.plot(x, reswrong, label="Wrong NUMA node pinned")
plt.plot(x, rescor, label="Correct NUMA node pinned")
plt.plot(x, pinned2, label="Both NUMA nodes pinned")
plt.plot(x, qemupin, label="NUMA pinned within VM")
plt.plot(x, nocontrl, label="No control over NUMA")
plt.xticks([1,      2,     3,     4,      5,      6][3:],
           ['100', '200', '400', '1000', '2000', '8000'][3:])
plt.legend(loc='upper right', ncol=1)
plt.xlabel("Value size in byte")
plt.ylabel("Completion time (s)")
plt.title("Completion time ZenFS 100GB of fillrandom")
plt.savefig("out/line_numa_small.png")
plt.savefig("out/line_numa_small.svg")
plt.close()
