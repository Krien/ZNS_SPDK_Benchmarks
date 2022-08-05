import matplotlib.pyplot as plt

def smartbytes(x): return 1000 * 512 * x

fig, ax = plt.subplots()
labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "TropoDB"]
values = [smartbytes(x)
          for x in [(292683188 - 266104226), (355291774 - 325882293)]] + [14872983864320]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 25)
ax.set_ylabel("Write amplification (avg)")
plt.title("FillRandom 1TB: Average WA for each key-value pairr")
plt.savefig("out/barplot_writes_per_put_fillrandom.png")
plt.savefig("out/barplot_writes_per_put_fillrandom.svg")
plt.close()


fig, ax = plt.subplots()
labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "TropoDB"]
values = [smartbytes(x)
          for x in [(324515798 - 292683188), (389576975 - 355291774)]] + [21261503265792]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 25)
ax.set_ylabel("Write amplification (avg)")
plt.title(
    "FillOverwrite 1TB: Average WA for each key-value pair")
plt.savefig("out/barplot_writes_per_put_overwrite.png")
plt.savefig("out/barplot_writes_per_put_overwrite.svg")
plt.close()
