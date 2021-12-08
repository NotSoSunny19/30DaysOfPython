#01 Enter the inputs
MyAge = int(input("Enter your age: "))
MyHeight = float(input("Enter your height in cm: "))
VariableComplex = complex(input("Enter a complex number: "))

#04 Program to find area of the triangle
BaseOfTriangle = float(input("Enter base of the triangle: "))
HeightOfTriangle = float(input("Enter height of the triangle: "))
#Area of the triangle
AreaOfTheTriangle = 0.5*BaseOfTriangle*HeightOfTriangle
print(AreaOfTheTriangle)

#05 Program to find perimeter of the triangle
FirstSideOfTriangle = float(input("Enter 1st side of the triangle: "))
SecondSideOfTriangle = float(input("Enter 2nd side of the triangle: "))
ThirdSideOfTriangle = float(input("Enter 3rd side of the triangle: "))
#Perimeter of the triangle
PerimeterOfTheTriangle = FirstSideOfTriangle+SecondSideOfTriangle+ThirdSideOfTriangle
print(PerimeterOfTheTriangle)

#06 Program to find perimeter of the rectangle
WidthOfRectangle = float(input("Enter width of the rectangle: "))
HeightOfRectangle = float(input("Enter height of the rectangle: "))
#Perimeter of the Rectangle
PerimeterOfRectangle = 2*(WidthOfRectangle+HeightOfRectangle)
print(PerimeterOfRectangle)

#07 Area and Perimeter of a circle
RadiusR = float(input("Enter the radius of circle: "))
FloatPi = 3.14
AreaOfTriangle = FloatPi*RadiusR*RadiusR
CircumferenceOfTriangle = 2*FloatPi*RadiusR
print(AreaOfTriangle)
print(CircumferenceOfTriangle)