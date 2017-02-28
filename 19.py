import math

daysInMonthLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

curYear = 1901
curMonth = 1
curDay = 1
curWeekday = 2 #tuesday
numSundaysOnFirst = 0

while curYear < 2001:
    if curDay == 1 and curMonth == 1:
        print(curYear, curWeekday)
    if curWeekday == 0 and curDay == 1:
        numSundaysOnFirst+=1

    #iterate
    curWeekday+=1
    if curWeekday >= 7:
        curWeekday = 0
    curDay+=1
    if isLeapYear(curYear):
        if curDay > daysInMonthLeap[curMonth-1]:
            curDay = 1
            curMonth+=1
    else:
        if curDay > daysInMonth[curMonth-1]:
            curDay = 1
            curMonth+=1
    if curMonth > 12:
        curMonth = 1
        curYear+=1

print (numSundaysOnFirst)
