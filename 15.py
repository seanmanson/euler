import math

knownNums = { 0 : 1 }
def numRoutesIt(rows, cols, maxCols):
    if (rows == 0) or (cols == 0):
        return 1
    if rows * maxCols + cols in knownNums:
        return knownNums[rows * maxCols + cols]
    
    total = 0
    for row in range(rows + 1):
        total += numRoutesIt(rows - row, cols - 1, maxCols)
    knownNums[rows * maxCols + cols] = total
    return total

def numRoutes(rows, cols):
    return numRoutesIt(rows, cols, cols)

print(numRoutes(20, 20))
