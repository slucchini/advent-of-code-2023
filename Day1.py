
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
    for i in range(len(cl)-1):
        for j in range(len(textnumbers)):
            if (cl[i:].startswith(textnumbers[j])):
                if (len(cl[i:]) == len(textnumbers[j])):
                    cl = cl[:i]+str(j+1)
                else:
                    cl = cl[:i]+str(j+1)+cl[i+len(textnumbers[j]):]
    convertedLines.append(cl)

nums = getNumsFromLines(convertedLines)
tot = sumNumArray(nums)
print("Part 2: {}".format(tot))