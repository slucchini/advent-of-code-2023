import numpy as np

f = open("data/Day1.dat")

nums = []
for line in f:
    linenums = []
    for char in line:
        try:
            linenums.append(int(char))
        except:
            None
    nums.append(linenums[0]*10+linenums[-1])

print(np.sum(nums))
