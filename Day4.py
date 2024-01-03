import numpy as np

f = open("data/Day4.dat")
data = f.readlines()

score = 0
for i in range(len(data)):
    d = data[i][10:-1]
    w,n = d.split('|')
    w = np.array(w.strip().split()).astype(int); n = np.array(n.strip().split()).astype(int)
    winningNums = n[np.isin(n,w)]
    if (len(winningNums)>0):
        score += 2**(len(winningNums)-1)

print("Part 1: {}".format(score))

scratchcards = {}
for i in np.array(range(len(data)))+1:
    scratchcards[i] = 1
for i in range(len(data)):
    n = i+1
    d = data[i][10:-1]
    w,m = d.split('|')
    w = np.array(w.strip().split()).astype(int); m = np.array(m.strip().split()).astype(int)
    nwins = len(m[np.isin(m,w)])
    for j in np.arange(n+1,n+1+nwins):
        scratchcards[j] += scratchcards[n]

ncards = np.sum(list(scratchcards.values()))
print("Part 2: {}".format(ncards))
    