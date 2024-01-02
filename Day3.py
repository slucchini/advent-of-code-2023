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

def getNum(line,ii):
    if not isNum(line[ii]):
        return 0
    istart = ii; iend = ii
    if (istart > 0):
        while isNum(line[istart-1]):
            istart -= 1
            if (istart == 0):
                break
    while isNum(line[iend]):
        iend += 1
        if (iend == len(line)):
            break
    return int(line[istart:iend])

def testSurroundings(data,lineno,ii):
    vals = []
    ivals = []
    if (ii > 0):
        ivals.append(ii-1)
    if (ii < len(data[lineno])-1):
        ivals.append(ii+1)
    if (lineno > 0):
        if (data[lineno-1][ii] == '.'):
            vals.extend([getNum(data[lineno-1],i) for i in ivals])
        else:
            vals.append(getNum(data[lineno-1],ii))
    vals.extend([getNum(data[lineno],i) for i in ivals])
    if (lineno < len(data)-1):
        if (data[lineno+1][ii] == '.'):
            vals.extend([getNum(data[lineno+1],i) for i in ivals])
        else:
            vals.append(getNum(data[lineno+1],ii))
    vals = np.array(vals)
    return vals[vals > 0]

def findSymbols(line):
    indices = []
    for s in list(symbolList):
        if s in line:
            indices.extend(np.where(np.array(list(line)) == s)[0])
    return indices

symbolList = '@#$%&*-+=/'

f = open("data/Day3.dat")
data = f.readlines()

tot = 0
for l in range(len(data)):
    d = data[l]
    indices = findSymbols(d)
    for i in indices:
        nums = testSurroundings(data,l,i)
        for n in nums:
            tot += n

print("Part 1: {}".format(tot))

symbolList = '*'

tot = 0
for l in range(len(data)):
    d = data[l]
    indices = findSymbols(d)
    for i in indices:
        nums = testSurroundings(data,l,i)
        if (len(nums) == 2):
            tot += np.prod(nums)

print("Part 2: {}".format(tot))
