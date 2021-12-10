# 08 Calculate the slope of x intercept and y intercept for y = 2x-2
CoeffOfY = float(input("Enter the y coefficient of y = mx+b: "))
CoeffOfX = float(input("Enter the x coefficient of y = mx+b: "))
CoeffOfB = float(input("Enter the constant 'b' of y = mx+b: "))
# now calculate the slope, converting the input equation to x and y intercept form
SlopeM1 = CoeffOfX/CoeffOfY
print(SlopeM1)

# 09 Calculate the slope and Euclidean distance between 2 points
# Importing numpy 
import numpy as np
pointA = np.array((2,2))
pointB = np.array((6,10))
DistanceBetweenAB = np.linalg.norm(pointA - pointB)
print(DistanceBetweenAB)
slope, intercept = np.polyfit(pointA,pointB,1)
print(slope)

# Program to find the Euclidien Distance between any 2 points
# Initializing the variables
PointA = (2,2)
PointB = (6,10)

# Process the inputs, Calculating the Euclidien Distance
SlopeM2 = (PointB[0]-PointA[0])/(PointB[1]-PointA[1])
# Print the Output, Print the Distance
print (float(SlopeM2))

# 10 Comparing the slopes of 08 and 09
if(SlopeM1 > SlopeM2):
    print("Slope M1 is greater: ",SlopeM1)
else:
    print("Slope M2 is greater: ",SlopeM2)

# 11 Calculate at what x value does y value become 0
for ValueX in range(-100,100):
    ValueY = ValueX**2 + ValueX*6 + 9
    if(ValueY == 0):
        print(ValueX)

# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a = len('python')
b = len('dragon')
if a<b:
    print("True")
else: 
    print("False")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("true, on is present in both python and dragon")
else:
    print("False,  on is not present in both python and dragon")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if 'jargon' in 'I hope this course is not full of jargon':
    print('True')

#There is no 'on' in both dragon and python
if 'on' not in 'python' and 'on' not in 'dragon':
    print('True')
else:
    print('False')

#Find the length of the text python and convert the value to float and convert it to string
ValueOfPython = str(float(len('python')))
print(ValueOfPython)
print(type(ValueOfPython))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
a= int(input('Enter the integer to be checked if it is divisible by 2: '))
CheckForDiv = a%2
if CheckForDiv == 0:
    print(a,'Divisible by 2')
else:
    print(a,'Not Divisible by 2')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
if int(2.7) == (7//3):
    print('True')
else:
    print('False')

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Hours = int(input('Enter hours: '))
Rate = int(input('Enter rate per hour: '))
print('Your weekly earning is ',Hours*Rate)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Years = int(input('Enter number of years you have lived: '))
print('You have lived for ',Years*365*24*60*60,' seconds.')

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for a in range(1,6):
    print(a,a**0,a**1,a**2,a**3)


