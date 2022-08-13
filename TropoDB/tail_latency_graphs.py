import matplotlib.pyplot as plt

def savefig(fig, name):
    fig.savefig(name + ".png")
    fig.savefig(name + ".svg")

def plot_latency(title, name, data):
    for i, j in enumerate([(100000, 6), (1000000, 8), (10000000000, 9)]):
        plt.rcParams["figure.figsize"] = (7.5, 6)
        fig, _ = plt.subplots()
        plt.xlabel("Percentile")
        plt.ylabel("Latency (μs)")
        plt.title(title)
        plt.ylim(1, j[0])
        plt.yscale('log')
        for entry in data:
            plt.plot(entry['x'][:j[1]], entry['y'][:j[1]], marker=entry['marker'],label=entry['label'])
        plt.legend()
        savefig(fig, "out/" + name + str(i))
        plt.close()

def plot_latency_fillrandom():
    x = ['25%', '50%', '75%', '99%', '99.9%',
        '99.99%', '99.999%', '99.9999%', '100%']
    latency_random_f2fs = {
        'x': x,
        'y':  [6.07, 8.02, 9.97, 28.01, 1206.57, 1298.66, 6052.33, 14284.02, 8142003],
        'marker': 'o',
        'label': 'RocksDB + F2FS'
    }
    latency_random_zenfs = {
        'x': x,
        'y':  [4.21, 5.44, 7.72, 25.98, 1253.44, 2528.35, 4337.39, 6415.86, 11371],
        'marker': 'D',
        'label': 'RocksDB + ZenFS'
    }
    latency_random_tropodb = {
        'x': x,
        'y':  [3.63,  4.78, 5.93, 899.42, 1285.15, 1846.76, 2896.25, 16646.15, 1083071035],
        'marker': 'x',
        'label': 'TropoDB'
    }
    plot_latency('Put Operation tail latency: 1TB of fillrandom', 'latency_fillrandom', 
    [latency_random_f2fs, latency_random_zenfs, latency_random_tropodb])

def plot_latency_fillrandom_L0_circular_log():
    x = ['25%', '50%', '75%', '99%', '99.9%',
        '99.99%', '99.999%', '99.9999%', '100%']
    latency_random_L050 = {
        'x': x,
        'y':  [3.80,  4.96, 6.30, 13.86, 1257.25, 1820.63, 2508.78, 15393.26, 1033125768],
        'marker': 'o',
        'label': 'L0  50 zones'
    }
    latency_random_L0100 = {
        'x': x,
        'y':  [3.63,  4.78, 5.93, 899.42, 1285.15, 1846.76, 2896.25, 16646.15, 1083071035],
        'marker': 'D',
        'label': 'L0 100 zones'
    }
    latency_random_L0200 = {
        'x': x,
        'y':  [4.02,  5.26, 7.30, 1095.63, 1292.34, 1861.48, 3453.07, 17038.38, 833132106],
        'marker': 'x',
        'label': 'L0 200 zones'
    }
    plot_latency('Put Operation tail latency TropoDB: 1TB of fillrandom', 'latency_fillrandom_tropodb_l0', 
    [latency_random_L050, latency_random_L0100, latency_random_L0200])

def plot_latency_filloverwrite():
    x = ['25%', '50%', '75%', '99%', '99.9%',
        '99.99%', '99.999%', '99.9999%', '100%']
    latency_overwrite_f2fs = {
        'x': x,
        'y':  [6.60, 8.61, 11.57, 33.26, 1243.88, 1640.76, 7533.95, 17533.39, 3659887],
        'marker': 'o',
        'label': 'RocksDB + F2FS'
    }
    latency_overwrite_zenfs = {
        'x': x,
        'y':  [4.21, 5.47, 7.86, 47.90, 1269.01, 2476.85, 4176.50, 6258.87, 9579],
        'marker': 'D',
        'label': 'RocksDB + ZenFS'
    }
    latency_overwrite_tropodb = {
        'x': x,
        'y':  [3.84,  5.00, 6.50, 1075.42, 1293.39, 1875.60, 3321.77, 16752.52, 1004201751],
        'marker': 'x',
        'label': 'TropoDB'
    }
    plot_latency('Put Operation tail latency: 1TB of filloverwrite', 'latency_filloverwrite', 
    [latency_overwrite_f2fs, latency_overwrite_zenfs, latency_overwrite_tropodb])

def plot_latency_filloverwrite_L0_circular_log():
    x = ['25%', '50%', '75%', '99%', '99.9%',
        '99.99%', '99.999%', '99.9999%', '100%']
    latency_overwrite_L050 = {
        'x': x,
        'y':  [3.96,  5.12, 6.83, 16.02, 1279.15, 1832.70, 2701.47, 10997.47, 1556650243],
        'marker': 'o',
        'label': 'L0  50 zones'
    }
    latency_overwrite_L0100 = {
        'x': x,
        'y':  [3.84,  5.00, 6.50, 1075.42, 1293.39, 1875.60, 3321.77, 16752.52, 1004201751],
        'marker': 'D',
        'label': 'L0 100 zones'
    }
    latency_overwrite_L0200 = {
        'x': x,
        'y':  [3.99,  5.20, 7.22, 1192.54, 1297.31, 2304.20, 4005.62, 20924.09, 1242891603],
        'marker': 'x',
        'label': 'L0 200 zones'
    }
    plot_latency('Put Operation tail latency TropoDB: 1TB of filloverwrite', 'latency_filloverwrite_tropodb_l0', 
    [latency_overwrite_L050, latency_overwrite_L0100, latency_overwrite_L0200])

def plot_latency_readwhilewriting():
    x = ['25%', '50%', '75%', '99%', '99.9%',
        '99.99%', '99.999%', '99.9999%', '100%']
    latency_readwhilewriting_f2fs = {
        'x': x,
        'y':  [208.37, 289.43, 428.76, 1470.19, 3208.86, 11016.65, 39730.77, 412516.18, 976044],
        'marker': 'o',
        'label': 'RocksDB + F2FS'
    }
    latency_readwhilewriting_zenfs = {
        'x': x,
        'y':  [497.16, 664.92, 835.20, 2046.31, 2955.92, 4302.63, 5992.83, 6567.97, 13783],
        'marker': 'D',
        'label': 'RocksDB + ZenFS'
    }
    plot_latency('Put operation tail latency: 1 hour of reads while writing', 'latency_readwhilewriting', 
    [latency_readwhilewriting_f2fs, latency_readwhilewriting_zenfs])

if __name__ == "__main__":
    plot_latency_fillrandom()
    plot_latency_fillrandom_L0_circular_log()
    plot_latency_filloverwrite()
    plot_latency_filloverwrite_L0_circular_log()
    plot_latency_readwhilewriting()
