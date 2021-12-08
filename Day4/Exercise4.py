# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty" +" "+ "Days" +" "+ "Of" +" "+ "Python")
 
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding" +" "+ "For" +" "+ "All")

# Declare a variable named company and assign it to an initial value "Coding For All".
Company = str('Coding For All')

# Print the variable company using print().
print(Company)

# Print the length of the company string using len() method and print().
print(len(Company))

# Change all the characters to uppercase letters using upper() method.
Company = Company.upper()
print(Company)

# Change all the characters to lowercase letters using lower() method.
Company = Company.lower()
print(Company)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# Capitalize()
Company = Company.capitalize()
print(Company)

# title()
Company = Company.title()
print(Company)

# swapcase()
Company = Company.swapcase()
print(Company)

# Cut(slice) out the first word of Coding For All string.
Company = str('Coding For All')
Coding = Company[7:14]
print(Coding)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
Company = 'Coding For All'
pos = Company.find('Coding')
if (pos != -1):
    pos = ("present")
    print(pos)
else:
    pos = ("absent")    
    print(pos)

# Replace the word coding in the string 'Coding For All' to Python.
Company = 'Coding For All'
Company2 = Company.replace('Coding', 'Python')
print(Company2)

# Change Python for Everyone to Python for All using the replace method or other methods.
Company3 = Company2.replace('All', 'Everyone')
print(Company3)

# Split the string 'Coding For All' using space as the separator (split()) .
Company4 = Company.split(' ')
print(Company4)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
Company5 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
vCompany5 = Company5.split(',')
print(Company5)

# What is the character at index 0 in the string Coding For All.
Company = "Coding for All"
print(Company[0])

# What character is at index 10 in "Coding For All" string.
Company = "Coding for All"
print(Company[10])

# What is the last index of the string Coding For All.
Company = "Coding for All"
LastIndex = int(len(Company))-1
print(LastIndex)
print(Company[LastIndex])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
string1 = "Python For Everyone"
CreateAbbreviation = string1[0] + string1[7] + string1[11] 
print(CreateAbbreviation)

# Create an acronym or an abbreviation for the name 'Coding For All'.
string1 = "Coding For All"
CreateAbbreviation = string1[0] + string1[7] + string1[11] 
print(CreateAbbreviation)

# Use index to determine the position of the first occurrence of C in Coding For All.
my_string = 'Coding For All'
print(my_string.find('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
my_string = 'Coding For All'
print(my_string.find('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
my_string = 'Coding For All'
print(my_string.rfind('i'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
TheSentence = 'You cannot end a sentence with because because because is a conjunction'
print(TheSentence.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
TheSentence = 'You cannot end a sentence with because because because is a conjunction'
str1 = slice(TheSentence.index('because'), TheSentence.rindex('because'))
print(str1)

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
TheSentence = 'You cannot end a sentence with because because because is a conjunction'
print(TheSentence.find('because'))

# Does 'Coding For All' start with a substring Coding?
TheSentence = 'Coding For All'
if(TheSentence.find('Coding')==0):
    print('Yes,Coding For All start with a substring Coding'+TheSentence.find('Coding'))
else:
    print('No,Coding For All does not start with a substring Coding')

# Does 'Coding For All' end with a substring coding?
TheSentence = 'Coding For All'
lastIndex = len(TheSentence)-1
if(TheSentence.find('Coding')==lastIndex):
    print('Yes,Coding For All start with a substring Coding'+TheSentence.find('Coding'))
else:
    print('No,Coding For All does not start with a substring Coding')