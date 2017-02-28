import math

test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def testPrime(num):
    for factor in test:
        if (num % factor == 0):
            return False
    test.append(num)
    return True

primes = set()
def populatePrimes(count):
    for num in range(2, count):
        if (testPrime(num)):
            primes.add(num)
    print("populated primes: ", len(primes))
    

def getCPrimes(a, b):
    cPrimes = []
    n = 1
    while True:
        curNum = n**2 + a*n + b
        if curNum <= 1 or not curNum in primes:
            return cPrimes
        cPrimes.append(curNum)
        n+=1

#populate primes
populatePrimes(20000)

longestCPrimes = []
longestA = False
longestB = False
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        cPrimes = getCPrimes(a, b)
        if len(cPrimes) > len(longestCPrimes):
            longestCPrimes = cPrimes
            longestA = a
            longestB = b

print (longestA, longestB, longestCPrimes)
