import math

for a in range(1, 1000):
    for b in range(1, a):
        c = 1000 - b - a
        if (a*a + b*b == c*c):
            print (a, b, c, a*a + b*b, c*c, a*b*c)
