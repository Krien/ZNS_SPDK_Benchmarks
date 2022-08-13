import json
import matplotlib.pyplot as plt

zone_count = 3688;

def savefig(fig, name):
    fig.savefig(name + ".png")
    fig.savefig(name + ".svg")

def parse_reset_data(filename):
    reset_data_x = [x for x in range(zone_count)]
    reset_data_y = [0 for x in reset_data_x]
    resets = []
    with open(filename, 'r') as file:
        resets = json.load(file)['resets']
    for reset in resets:
        reset_data_y[reset['zone']] = reset['count']
    return (reset_data_x, reset_data_y)

def plot_reset_data(input, output, title, istropodb=False):
    reset_data_x, reset_data_y = parse_reset_data(input)
    fig, ax = plt.subplots()
    plt.stackplot(reset_data_x, reset_data_y, colors=["red"])
    plt.xlabel("Zone number")
    plt.ylabel("Number of physical resets")
    plt.title(title)
    plt.ylim(0, 40)
    # Markers for TropoDB (hardcoded)
    if (istropodb):
        plt.plot([4,4], [0, 40], color='black', label='WALs begin')
        plt.plot([164,164], [0, 40], color='black', linestyle='dotted', label='L0 begin')
        plt.plot([264,264], [0, 40], color='black', linestyle='dashdot', label='LN begin')
        plt.legend()
    savefig(fig, "out/" + output)
    plt.close()


if __name__ == "__main__":
    plot_reset_data('./data/heat/resets_tropodb_fillrandom.json',
         'resets_per_zone_fillrandom_tropodb', 'FillRandom 1TB TropoDB: Number of resets per zone', True)
    plot_reset_data('./data/heat/resets_tropodb_filloverwrite.json',
         'resets_per_zone_filloverwrite_tropodb', 'FillOverwrite 1TB TropoDB: Number of resets per zone', True)
    plot_reset_data('./data/heat/resets_zenfs_fillrandom.json',
         'resets_per_zone_fillrandom_zenfs', 'FillRandom 1TB RocksDB + ZenFS: Number of resets per zone')
    plot_reset_data('./data/heat/resets_zenfs_filloverwrite.json',
         'resets_per_zone_filloverwrite_zenfs', 'FillOverwrite 1TB RocksDB + ZenFS: Number of resets per zone')
    plot_reset_data('./data/heat/resets_f2fs_fillrandom.json',
         'resets_per_zone_fillrandom_f2fs', 'FillRandom 1TB RocksDB + F2FS: Number of resets per zone')
    plot_reset_data('./data/heat/resets_f2fs_filloverwrite.json',
         'resets_per_zone_filloverwrite_f2fs', 'FillOverwrite 1TB RocksDB + F2FS: Number of resets per zone')
    