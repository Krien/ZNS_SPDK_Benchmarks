import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# sns.set_theme()

y = []
with open('data/heat/reset_distr.json', 'r') as file:
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

with open('data/heat/write_distr.json', 'r') as file:
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
