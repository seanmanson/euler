import math

def numFactors(num, end):
    count = 2
    for i in range(2, end + 1):
        if num % i == 0:
            count += 2
    return count

lastCount = 0
curInd = 0
curNum = 1
while lastCount < 500:
    curInd+=1
    curNum = int((curInd**2 + curInd)/2)
    if (curInd % 2 == 0):
        lastCount = numFactors(curNum, int(curInd/2))
    else:
        lastCount = numFactors(curNum, int((curInd + 1)/2))
    

print (curInd, curNum, lastCount)
