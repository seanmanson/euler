sumf = 0
cur = 1
last = 1

while cur < 4000000:
    temp = cur
    cur = cur + last
    last = temp
    if (cur % 2 == 0):
        sumf += cur

print(sumf)
