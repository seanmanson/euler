import math

digits = [2]
for i in range(1, 1000):
    carry = 0
    for index in range(len(digits)):
        carry += digits[index] * 2
        digits[index] = carry % 10
        carry = math.floor(carry/10)
    while carry > 0:
        digits.append(carry % 10)
        carry = math.floor(carry/10)

for digit in reversed(digits):
    print(digit, end="")
print(" ", sum(digits))
