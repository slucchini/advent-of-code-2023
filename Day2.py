import numpy as np

class Game():
    def __init__(self,id,pulls):
        self.id = id
        self.npulls = len(pulls)
        self.ndice = np.array(pulls)
    
    def get_all_maxs(self):
        return [max(self.ndice[:,i]) for i in range(3)]

    def get_max(self,color):
        if (color == 'red'):
            return max(self.ndice[:,0])
        elif (color == 'green'):
            return max(self.ndice[:,1])
        elif (color == 'blue'):
            return max(self.ndice[:,2])

def parseLine(line):
    pulls = []
    line = line[4:]
    splitlines = line.split(':')
    id = int(splitlines[0])
    pulldata = splitlines[1].split(';')
    for pull in pulldata:
        dice = pull.split(',')
        p = [0,0,0]
        for d in dice:
            d = d.strip()
            ds = d.split(' ')
            n = int(ds[0])
            c = ds[1]
            if (c == 'red'):
                p[0] = n
            elif (c == 'green'):
                p[1] = n
            elif (c == 'blue'):
                p[2] = n
        pulls.append(p)
    return id,pulls

f = open("data/Day2.dat")
all_lines = f.readlines()

tot = 0
maxvals = np.array([12,13,14])
for line in all_lines:
    id,pulls = parseLine(line)
    cgame = Game(id,pulls)
    gamemaxs = cgame.get_all_maxs()
    fail = gamemaxs > maxvals
    if (not np.any(fail)):
        tot += id

print("Part 1: {}".format(tot))

powers = []
for line in all_lines:
    id,pulls = parseLine(line)
    cgame = Game(id,pulls)
    gamemaxs = cgame.get_all_maxs()
    powers.append(np.product(gamemaxs))

print("Part 2: {}".format(np.sum(powers)))