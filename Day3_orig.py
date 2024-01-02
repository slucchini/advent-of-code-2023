import numpy as np

def isNum(s):
    try:
        n = int(s)
    except:
        return False
    return True

def findNextNum(lineinfo,istart):
    i = istart
    while (lineinfo[i] not in list(str(1234567890))):
        if (i == len(lineinfo)-1):
            return None,0,0
        i += 1
    i1 = i
    while (lineinfo[i] in list(str(1234567890))):
        if (i == len(lineinfo)-1):
            i += 1
            break
        i += 1
    i2 = i
    return int(lineinfo[i1:i2]),i1,i2

def testSurroundings(data,lineno,i1,i2):
    lvals = []
    if (lineno > 0):
        lvals.append(lineno-1)
    lvals.append(lineno)
    if (lineno < len(data)-1):
        lvals.append(lineno+1)
    istart = max(0,i1-1)
    iend = min(i2+1,len(data[lineno]))
    for l in lvals:
        for i in np.arange(istart,iend):
            if (data[l][i] in list(symbolList)):
                return True
    return False

symbolList = '@#$%&*-+=/'

f = open("data/Day3.dat")
data = f.readlines()

tot = 0
for l in range(len(data)):
    d = data[l]
    n,i1,i2 = findNextNum(d,0)
    subtot = 0
    while n is not None:
        if testSurroundings(data,l,i1,i2):
            subtot += n
        if (i2 >= len(d)-1):
            break
        n,i1,i2 = findNextNum(d,i2+1)
    tot += subtot

print("Part 1: {}".format(tot))
