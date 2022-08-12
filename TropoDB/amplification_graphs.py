import matplotlib.pyplot as plt

def smartbytes(x): return 1000 * 512 * x

fig, ax = plt.subplots()
labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "TropoDB"]
values = [smartbytes(x)
          for x in [(292683188 - 266104226), (355291774 - 325882293)]] + [14872983864320]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 30)
ax.set_ylabel("Write amplification (avg)")
plt.title("FillRandom 1TB: Average WA for each key-value pair")
plt.savefig("out/barplot_writes_per_put_fillrandom.png")
plt.savefig("out/barplot_writes_per_put_fillrandom.svg")
plt.close()


fig, ax = plt.subplots()
labs = ["L0 50 zones", "L0 100 zones", "L0 200 zones"]
values = [14641582881280, 14872983864320, 16876890434560]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 30)
ax.set_ylabel("Write amplification (avg)")
plt.title("FillRandom 1TB TropoDB: Average WA for each key-value pair")
plt.savefig("out/barplot_writes_per_put_fillrandom_tropoDB_L0.png")
plt.savefig("out/barplot_writes_per_put_fillrandom_tropoDB_L0.svg")
plt.close()

fig, ax = plt.subplots()
labs = ["L0 50 zones", "L0 100 zones", "L0 200 zones"]
values = [13686, 13866, 15463]
plt.bar(labs, values,
        width=0.4)
plt.ylim(0, 30000)
ax.set_ylabel("Resets")
plt.title("FillRandom 1TB TropoDB: Total number of resets issued")
plt.savefig("out/barplot_resets_per_put_fillrandom_tropoDB_L0.png")
plt.savefig("out/barplot_resets_per_put_fillrandom_tropoDB_L0.svg")
plt.close()



fig, ax = plt.subplots()
labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "TropoDB"]
values = [smartbytes(x)
          for x in [(324515798 - 292683188), (389576975 - 355291774)]] + [21261503265792]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 30)
ax.set_ylabel("Write amplification (avg)")
plt.title(
    "FillOverwrite 1TB: Average WA for each key-value pair")
plt.savefig("out/barplot_writes_per_put_overwrite.png")
plt.savefig("out/barplot_writes_per_put_overwrite.svg")
plt.close()


fig, ax = plt.subplots()
labs = ["L0 50 zones", "L0 100 zones", "L0 200 zones"]
values = [23341811976704, 21261503265792, 28887225376768]
plt.bar(labs, [value/(1000000000*1016) for value in values],
        width=0.4)
plt.ylim(0, 30)
ax.set_ylabel("Write amplification (avg)")
plt.title("FillOverwrite 1TB TropoDB: Average WA for each key-value pair")
plt.savefig("out/barplot_writes_per_put_filloverwrite_tropoDB_L0.png")
plt.savefig("out/barplot_writes_per_put_filloverwrite_tropoDB_L0.svg")
plt.close()



fig, ax = plt.subplots()
labs = ["L0 50 zones", "L0 100 zones", "L0 200 zones"]
values = [22732, 20826, 28344]
plt.bar(labs, values,
        width=0.4)
plt.ylim(0, 30000)
ax.set_ylabel("Resets")
plt.title("FillOverwrite 1TB TropoDB: Total number of resets issued")
plt.savefig("out/barplot_resets_per_put_filloverwrite_tropoDB_L0.png")
plt.savefig("out/barplot_resets_per_put_filloverwrite_tropoDB_L0.svg")
plt.close()
