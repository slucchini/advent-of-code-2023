import numpy as np, matplotlib.pyplot as plt

f = open("data/Day6.dat")
data = f.readlines()

times = np.array(data[0].split(':')[1].split()).astype(int)
distances = np.array(data[1].split(':')[1].split()).astype(int)

races = np.array(list(zip(times,distances)))

nwins = []
for r in races:
    tvals = np.array(range(r[0]+1))
    dvals = tvals*tvals[::-1]
    nwins.append(np.sum(dvals>r[1]))

print("Part 1: {}".format(np.prod(nwins)))

time = int(''.join(data[0].split(':')[1].split()))
dist = int(''.join(data[1].split(':')[1].split()))

tvals = np.array(range(time+1))
dvals = tvals*tvals[::-1]
nwins = np.sum(dvals > dist)

print("Part 2: {}".format(nwins))