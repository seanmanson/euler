import math

total = 0
curspiralside = 1
for num in range(1, 1001*1001 + 1):
    if num > curspiralside**2:
        curspiralside+=2
    if curspiralside == 1 or (num - (curspiralside-2)**2) % (curspiralside - 1) == 0:
        total+=num

print (total)
