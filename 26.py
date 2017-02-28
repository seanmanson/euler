import math

def cycle(denom):
    curVal = 10
    cycleDigits = []
    prevCurVals = set()
    while curVal != 0 and not curVal in prevCurVals:
        prevCurVals.add(curVal)
        cycleDigits.append(math.floor(curVal/denom))
        curVal = 10 * (curVal % denom)
    if curVal == 0:
        return []
    else:
        return cycleDigits

longest = 0
longestLen = 0
longestCycle = []
for i in range(2, 1000):
    lengthHere = len(cycle(i))
    if lengthHere > longestLen:
        longest = i
        longestLen = lengthHere
        longestCycle = cycle(i)

print (longest, longestLen, 1/longest)
