# # Iterate 0 to 10 using for loop, do the same using while loop.
for item in range(11):
    print(item)
item = 0
while item < 11:
    print(item)
    item = item + 1

# # Iterate 10 to 0 using for loop, do the same using while loop.
for item in range(-10,0):
    if (item < 0):
        print(abs(item))

item = 10
while item > 0:
    print(item)
    item = item - 1


# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

n = 7 
myList = []
for item1 in range(0,n+1):
    print('#'*item1)

# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

NumRows = 8
NumColm = 9
for item1 in range(0,NumRows):
    print('# '*NumColm)


# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

NumSq = int(input('Enter a range: '))
for item in range(0,NumSq+1):
    print(str(item) + ' x ' + str(item) + ' = ' + str(item*item))

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
mySkills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in mySkills:
    print(item)

# Use for loop to iterate from 0 to 100 and print only even numbers
for item in range(0,101):
    if (item%2 == 0):
        print(item)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for item in range(0,101):
    if (item%2 != 0):
        print(item)

