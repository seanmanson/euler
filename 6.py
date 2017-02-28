import math

sumsquare = 0
sumnorm = 0

for i in range(1, 101):
    sumnorm += i
    sumsquare += i*i

big = sumnorm*sumnorm
print(big, sumsquare, big - sumsquare)
