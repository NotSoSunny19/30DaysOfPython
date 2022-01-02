# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.

total = 0
SumList = []
for item1 in range(101):
    SumList.append(item1)
for item2 in range(0, len(SumList)):
    total = total + SumList[item2]
print(total)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
totalEven = 0
totalOdd = 0
ev_li = []
od_li = []
for item3 in SumList:
    if (item3 % 2 == 0):
        ev_li.append(item3)
    else:
        od_li.append(item3)
for item4 in ev_li:
    totalEven = totalEven + SumList[item4]
for item5 in od_li:
    totalOdd = totalOdd + SumList[item5]
print(od_li)
print(ev_li)
print(totalEven)
print(totalOdd)

