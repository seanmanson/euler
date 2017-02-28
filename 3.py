import math

test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27]

def testPrime(num):
    for factor in test:
        if (num % factor == 0):
            return False
    return True
        
num = 600851475143
for i in range(27, int(math.sqrt(600851475143)), 2):
    if i > math.sqrt(num) or not testPrime(i):
        continue
    test.append(i)
    if (num % i == 0):
        num = int(num/i)

print("done", num)
