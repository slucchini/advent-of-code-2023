import numpy as np, time

class SeedMap():
    def __init__(self,source,destination):
        self.source = source
        self.destination = destination
        self.rules = []
    
    def add_rule(self,dstart,sstart,nsteps):
        self.rules.append([dstart,sstart,nsteps])

    def map_num(self,num):
        rules = np.array(self.rules)
        ranges = np.array([[r[1],r[1]+r[2]] for r in rules])
        rval = (num > ranges[:,0]) & (num < ranges[:,1])
        if (np.sum(rval) == 0):
            return num
        else:
            rule = rules[rval][0]
            offset = num - rule[1]
            return rule[0] + offset
    
    def map_nums(self,num,nlen,output=[]):
        if nlen == 0:
            return output
        rules = np.array(self.rules)
        ranges = np.array([[r[1],r[1]+r[2]] for r in rules])
        rval = (num >= ranges[:,0]) & (num < ranges[:,1])
        if (np.sum(rval) == 0):
            if np.any(rules[:,1]>num):
                greater_rules = rules[rules[:,1]>num]
                next_rule = greater_rules[np.argmin(greater_rules[:,1]-num)][1]
                diff = next_rule - num
                if (diff > nlen):
                    output.extend([num,nlen])
                    return output
                else:
                    output.extend([num,diff])
                    return self.map_nums(next_rule,nlen-diff,output)
            else:
                output.extend([num,nlen])
                return output
        else:
            rule = rules[rval][0]
            offset = num - rule[1]
            diff = rule[2] - offset
            if (diff > nlen):
                output.extend([rule[0] + offset,nlen])
                return output
            else:
                output.extend([rule[0] + offset,diff])
                return self.map_nums(num+diff,nlen-diff,output)
        
print("Loading...",end='')
stime = time.time()

f = open("data/Day5.dat")
data = f.readlines()

datatypes = np.array(['seed','soil','fertilizer','water','light','temperature','humidity','location'])

seeds = np.array(data[0].split(':')[1].split()).astype('int64')
maps = []

for d in data[1:]:
    if (':' in d):
        info = d.split()[0]
        source_w = info.split('-')[0]
        destination_w = info.split('-')[-1]
        source = np.where(datatypes == source_w)[0][0]
        destination = np.where(datatypes == destination_w)[0][0]
        cmap = SeedMap(source,destination)
        maps.append(cmap)
    elif (len(d.split())>0):
        vals = np.array(d.split()).astype('int64')
        cmap.add_rule(*vals)

print('done ({:.4f} s)'.format(time.time()-stime))

print("")
print("Part 1...")
stime = time.time()

locvals = []
for s in seeds:
    num = s
    for m in maps:
        num = m.map_num(num)
    locvals.append(num)

print("{}".format(min(locvals)))
print('done ({:.4f} s)'.format(time.time()-stime))

print("")
print("Part 2...")
stime = time.time()

locvals = []
curList = seeds
for m in maps:
    newList = []
    for s,slen in zip(curList[::2],curList[1::2]):
        out = m.map_nums(s,slen,output=[])
        newList.extend(out)
    curList = newList

locvals = curList[::2]
nvals = curList[1::2]

print("{}".format(min(locvals)))
print("done ({:.4f} s)".format(time.time()-stime))

### gets the seed number with the lowest location
# mini = np.argmin(locvals)
# minpos = np.sum(nvals[:mini])
# seedvals = seeds[::2]
# nseeds = seeds[1::2]
# i = 0
# while (minpos > nseeds[i]):
#     i += 1
#     minpos -= nseeds[i]
# print("Part 2: {}".format(seedvals[i]+minpos))

