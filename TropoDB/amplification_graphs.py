import matplotlib.pyplot as plt

def smartbytes(x): return 1000 * 512 * x

def savefig(fig, name):
    fig.savefig(name + ".png")
    fig.savefig(name + ".svg")

def plot_write_amplification(title, name, labs, values, number_of_vals):
    fig, ax = plt.subplots()
    plt.bar(labs, [value/number_of_vals for value in values],
        width=0.4)
    plt.ylim(0, 30)
    ax.set_ylabel("Write amplification (avg)")
    plt.title(title)
    savefig(plt, "out/" + name)
    plt.close()

def plot_write_amplification_fillrandom():
    labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "TropoDB"]
    values = [smartbytes(x)
        for x in [(1593186755 - 1566705121), (1530804210 - 1501618568)]] + [14872983864320]
    plot_write_amplification('FillRandom 1TB: Average WA for each key-value pair', 'barplot_writes_per_put_fillrandom',
        labs, values, 1000000000*1016)

def plot_write_amplification_fillrandom_L0_circular_log():
    labs = ["L0 50 zones", "L0 100 zones", "L0 200 zones"]
    values = [14641582881280, 14872983864320, 16876890434560]
    plot_write_amplification('FillRandom 1TB TropoDB: Average WA for each key-value pair', 'barplot_writes_per_put_fillrandom_tropoDB_L0',
        labs, values, 1000000000*1016)

def plot_write_amplification_fillrandom_higher_concurrency():
    labs = ["Concurrency level 1", "Concurrency level 2"]
    values = [14872983864320, 14389997264896]
    plot_write_amplification('FillRandom 1TB TropoDB: Average WA for each key-value pair', 'barplot_writes_per_put_fillrandom_tropoDB_concurrency',
        labs, values, 1000000000*1016)

def plot_write_amplification_filloverwrite():
    labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "TropoDB"]
    values = [smartbytes(x)
          for x in [(1624911408 - 1593186755), (1565335235 - 1530804210)]] + [21261503265792]
    plot_write_amplification('FillOverwrite 1TB: Average WA for each key-value pair', 'barplot_writes_per_put_overwrite',
        labs, values, 1000000000*1016)

def plot_write_amplification_filloverwrite_L0_circular_log():
    labs = ["L0 50 zones", "L0 100 zones", "L0 200 zones"]
    values = [23341811976704, 21261503265792, 28887225376768]
    plot_write_amplification('FillOverwrite 1TB TropoDB: Average WA for each key-value pair', 'barplot_writes_per_put_filloverwrite_tropoDB_L0',
        labs, values, 1000000000*1016)

def plot_write_amplification_filloverwrite_higher_concurrency():
    labs = ["Concurrency level 1", "Concurrency level 2"]
    values = [21261503265792, 22833857610752]
    plot_write_amplification('FillOverwrite 1TB TropoDB: Average WA for each key-value pair', 'barplot_writes_per_put_filloverwrite_tropoDB_concurrency',
        labs, values, 1000000000*1016)


def plot_reset_count(title, name, labs, values):
    fig, ax = plt.subplots()
    plt.bar(labs, [value/1000000000 for value in values], width=0.4)
    plt.ylim(0, 5 * 10**(-5))
    ax.set_ylabel("Resets (normalised)")
    plt.title(title)
    savefig(plt, "out/" + name)
    plt.close()

def plot_resets_fillrandom_L0():
    labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "TropoDB"]
    values = [10898, 12369, 13866]
    plot_reset_count('FillRandom 1TB: Number of resets', 'barplot_resets_per_put_fillrandom',
        labs, values)


def plot_resets_fillrandom_L0_circular_log():
    labs = ["L0 50 zones", "L0 100 zones", "L0 200 zones"]
    values = [13686, 13866, 15463]
    plot_reset_count('FillRandom 1TB TropoDB: Number of resets', 'barplot_resets_per_put_fillrandom_tropoDB_L0',
        labs, values)

def plot_resets_fillrandom_higher_concurrency():
    labs = ["Concurrency level 1", "Concurrency level 2"]
    values = [13866, 13350]
    plot_reset_count('FillRandom 1TB TropoDB: Total number of resets', 'barplot_resets_per_put_fillrandom_tropoDB_concurrency',
        labs, values)

def plot_resets_filloverwrite_L0():
    labs = ["RocksDB + F2FS", "RocksDB + ZenFS", "TropoDB"]
    values = [14101, 15698, 20826]
    plot_reset_count('FillOverwrite 1TB: Number of resets issued', 'barplot_resets_per_put_filloverwrite',
        labs, values)

def plot_resets_filloverwrite_L0_circular_log():
    labs = ["L0 50 zones", "L0 100 zones", "L0 200 zones"]
    values = [22732, 20826, 28344]
    plot_reset_count('FillOverwrite 1TB TropoDB: Number of resets', 'barplot_resets_per_put_filloverwrite_tropoDB_L0',
        labs, values)

def plot_resets_filloverwrite_higher_concurrency():
    labs = ["Concurrency level 1", "Concurrency level 2"]
    values = [20826, 22271]
    plot_reset_count('FillOverwrite 1TB TropoDB: Number of resets', 'barplot_resets_per_put_filloverwrite_tropoDB_concurrency',
        labs, values)


if __name__ == "__main__":
    plot_write_amplification_fillrandom()
    plot_write_amplification_fillrandom_L0_circular_log()
    plot_write_amplification_fillrandom_higher_concurrency()
    plot_write_amplification_filloverwrite()
    plot_write_amplification_filloverwrite_L0_circular_log()
    plot_write_amplification_filloverwrite_higher_concurrency()
    plot_resets_fillrandom_L0()
    plot_resets_fillrandom_L0_circular_log()
    plot_resets_fillrandom_higher_concurrency()
    plot_resets_filloverwrite_L0()
    plot_resets_filloverwrite_L0_circular_log()
    plot_resets_filloverwrite_higher_concurrency()
