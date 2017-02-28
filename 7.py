import math

test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def testPrime(num):
    for factor in test:
        if (num % factor == 0):
            return False
    test.append(num)
    return True

numPrimes = 10
i = 27
while numPrimes < 10001:
    i+=2
    if not testPrime(i):
        continue
    numPrimes+=1
    if (numPrimes % 200 == 0):
        print("progress: ", numPrimes, i)

print(numPrimes, i)
