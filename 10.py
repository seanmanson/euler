import math

test = []

def testPrime(num):
    sq = int(math.sqrt(num))
    for i, factor in enumerate(test):
        if (i > sq):
            break
        if (num % factor == 0):
            return False
    test.append(num)
    return True

sumPrimes = 2
for i in range(3, 2000000, 2):
    if not testPrime(i):
        continue
    sumPrimes+=i
    if (i % 10000 == 1):
        print("progress : ", i, sumPrimes)

print (sumPrimes)
