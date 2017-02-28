import math

knownLengths = {1 : 1}
def collatzLen(num):
    if num in knownLengths:
        return knownLengths[num]
    length = 1
    if num % 2 == 0:
        length += collatzLen(num/2)
    else:
        length += collatzLen(3*num+1)
    knownLengths[num] = length
    return length

longest = 1
longestLen = 0
for i in range(1, 1000000):
    lenHere = collatzLen(i)
    if lenHere > longestLen:
        longest = i
        longestLen = lenHere

print(longest, longestLen)
