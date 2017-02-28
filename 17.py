import math

oneStrings = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tenStrings = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teenStrings = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def toString(num):
    ones = num % 10
    tens = math.floor((num % 100)/10)
    hundreds = math.floor((num%1000)/100)

    string = ""
    if hundreds > 0:
        string += oneStrings[hundreds] + "hundred"
        if tens > 0 or ones > 0:
            string += "and"
    if tens == 1 and ones > 0:
        string += teenStrings[ones]
    else:
        string += tenStrings[tens] + oneStrings[ones]
    return string

count = 0
for i in range(1, 1001):
    print (toString(i))
    count += len(toString(i))
count += len("onethousand")

print (count)
    
    
