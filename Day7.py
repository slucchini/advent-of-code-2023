import numpy as np

###
# 0 : five of a kind
# 1 : four of a kind
# 2 : full house
# 3 : three of a kind
# 4 : two pair
# 5 : one pair
# 6 : high card
###
def getHandType(hand):
    ulen = len(np.unique(hand))
    ncount = [len(hand[hand == c]) for c in np.unique(hand)]
    if (ulen == 1):
        return 0
    elif (ulen == 2):
        if (4 in ncount):
            return 1
        elif (3 in ncount):
            return 2
    elif (ulen == 3):
        if (3 in ncount):
            return 3
        if (2 in ncount):
            return 4
    elif (ulen == 4):
        if (2 in ncount):
            return 5
    else:
        return 6

def alpha2Num(hand):
    hand = np.array(hand).astype('object')
    hand[hand == 'T'] = '10'
    hand[hand == 'J'] = '11'
    hand[hand == 'Q'] = '12'
    hand[hand == 'K'] = '13'
    hand[hand == 'A'] = '14'
    return np.array(hand).astype(int)

def sortHands(hands):
    hands = np.array([('{:02}'*len(h)).format(*h) for h in hands]).astype(int)
    srt = np.argsort(hands)
    return srt

f = open("data/Day7.dat")
data = f.readlines()

hands = []
bids = []
for d in data:
    h = np.array(list(d.split()[0]))
    hands.append(alpha2Num(h))
    bids.append(int(d.split()[1]))
hands = np.array(hands)
bids = np.array(bids)

types = np.array([getHandType(h) for h in hands])
sortedbids = []
sortedhands = []
for type in np.array(range(7))[::-1]:
    mask = types == type
    h = hands[mask]
    sortedbids.extend(bids[mask][sortHands(h)])
    sortedhands.extend(h[sortHands(h)])
sortedbids = np.array(sortedbids)
sortedhands = np.array(sortedhands)

rank = (np.array(range(len(sortedbids)))+1)

print("Part 1: {}".format(np.sum(rank*sortedbids)))

