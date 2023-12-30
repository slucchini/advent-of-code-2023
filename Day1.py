import numpy as np

def isNum(s):
    try:
        n = int(s)
    except:
        return False
    return True

def getNumsFromLines(lines):
    nums = []
    for line in lines:
        linenums = []
        for char in line:
            try:
                linenums.append(int(char))
            except:
                None
        nums.append(linenums[0]*10+linenums[-1])
    return nums

def sumNumArray(nums):
    tot = 0
    for n in nums:
        tot += n
    return tot

f = open("data/Day1.dat")
all_lines = f.readlines()

nums = getNumsFromLines(all_lines)
tot = sumNumArray(nums)
print("Part 1: {}".format(tot))

convertedLines = []
textnumbers = ['one','two','three','four','five','six','seven','eight','nine']
for line in all_lines:
    cl = line
    swaps = []
    for j in range(len(textnumbers)):
        indices = [i for i in range(len(cl)) if cl.startswith(textnumbers[j], i)]
        for i in indices:
            swaps.append([i,len(textnumbers[j]),j+1])
    swaps = np.array(swaps)
    for s in swaps:
        cl = cl[:s[0]]+str(s[2])+cl[s[0]+1:]
    for si in range(len(swaps)):
        s = swaps[si]
        for k in range(s[1]-1):
            if isNum(cl[s[0]+1]):
                break
            cl = cl[:s[0]+1]+cl[s[0]+2:]
            shiftmask = swaps[:,0] > s[0]
            swaps[shiftmask,0] -= 1
    convertedLines.append(cl)


nums = getNumsFromLines(convertedLines)
tot = sumNumArray(nums)
print("Part 2: {}".format(tot))

f2 = open("data/Day1_test.dat",'w')
for i in range(len(convertedLines)):
    f2.write(convertedLines[i][:-1]+'  :  {}\n'.format(nums[i]))
f2.close()