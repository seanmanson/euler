import math

largest = 0

def isPalindrome(x):
    pal = str(x)
    for i in range(math.ceil(len(pal) / 2)):
        if pal[i] != pal[-(i + 1)]:
            return False
    return True


for i in range(100, 999):
    for j in range(100, 999):
        num = i * j
        if (isPalindrome(num) and num > largest):
            largest = num
print("done", largest)
