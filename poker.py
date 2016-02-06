from deck import *

d = Deck()
vals = []

def points() :
    global vals
    for i in xrange(len(vals)) :
        if vals[i] == 1 :
            vals[i] = 14
    vals = sorted(vals, key = int)
    return vals

def hands() :
    print points()
    flush = True
    for i in xrange(len(vals) - 1) :
        if not vals[i + 1] == vals[i] + 1 :
            flush = False
            break
    straight = True
    suit = d.getDealt()[0].getSuit()
    for i in xrange(len(d.getDealt())) :
        if not d.getDealt()[i].getSuit == suit :
            straight = False
            break
    kinds = []
    bases = []
    for i in xrange(len(vals)) :
        if vals[i] in bases :
            kinds[bases.index(vals[i])] += 1
        else :
            bases.append(vals[i])
            kinds.append(1)
    if flush and straight :
        return 'Straight Flush!'
    elif flush :
        return 'Flush!'
    elif straight :
        return 'Straight!'
    elif max(kinds) > 1 :
        if sorted(kinds, key = int) == [2,3] :
            return 'Full house!'
        elif kinds.count(max(kinds)) == 2 :
            return 'Two pair!'
        elif max(kinds) == 2 :
            return 'One pair!'
        return str(max(kinds)) + ' of a kind!'
    return 'High card!'

for i in xrange(5) :
    print d.dealCard()

hand = d.getDealt()

for i in hand :
    vals.append(i.getValue())

print hands()