# Day 2: 30 Days of python programming
# Declaring the variable names

FullName = str(input('Enter your full name: '))
MyCountry = str(input('Enter your Country: '))
MyCity = str(input('Enter your City: '))
MyAge = int(input('Enter your Age: '))
DOBYear = int(input('Enter your Year of Birth: '))
is_married = bool(input('Enter your martial status: '))
is_true = bool(input('Enter if day or night: '))
is_light_on = bool(input('Enter if your light is on: '))
FirstName = str(input('Enter your first name'))
LastName = str(input('Enter your last name'))

#printing the Values:
print(FirstName,LastName,FullName,MyCountry,MyCity,MyAge,DOBYear,is_married,is_true,is_light_on)

#finding the type of the variables defined
print(type(FirstName), type(LastName), type(FullName), type(MyCountry), type(MyCity), type(MyAge), type(DOBYear), type(is_light_on), type(is_true), type(is_married))

#Using len function
if(len(FirstName) > len(LastName)):
    print(FirstName)

else:
    print(LastName)        
 

# radiusR = 30 
radiusR = int(input("Enter the radius of circle: "))
AreaA = 3.14*(radiusR**2)
CircumferenceC = 2*3.14*radiusR
print(AreaA)
print(CircumferenceC)
