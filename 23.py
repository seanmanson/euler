import math

def sumFactors(num):
    #end = math.ceil(math.sqrt(num))
    sumFactors = 1
    for i in range(2, num):
        if num % i == 0:
            sumFactors += i
    return sumFactors

knownAbundants = set()
knownNotAbundants = set()
def isAbundant(num):
    if num in knownAbundants:
        return True
    if num in knownNotAbundants:
        return False
    if sumFactors(num) > num:
        knownAbundants.add(num)
        return True
    else:
        knownNotAbundants.add(num)
        return False

def isSumOfAbundants(num):
    for first in knownAbundants:
        if num - first in knownAbundants:
            return True
    return False

for i in range(12, 28123 - 12 + 1):
    isAbundant(i)
    if (i % 1000 == 0):
        print("progress", i)

print("testing known abundants: ", knownAbundants)
total = 0
for num in range(1, 28124):
    #see if this is a sum of two abundants
    #print("progress",num, isSumOfAbundants(num))
    if not isSumOfAbundants(num):
        total += num
print(total)
