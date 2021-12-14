 # Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Julie','color': 'Grey','breed': 'Indie', 'legs': 4, 'age': 9}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Sunny',
    'last_name' : 'NotSo',
    'gender': 'Male', 
    'age': 24, 
    'marital status': 'Single', 
    'skills':['Soft Skills','Technincal'], 
    'country':'India', 
    'city':'Hyderabad', 
    'address':'Prakash Nagar'
    }
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
SkillsOfStudent = student['skills']
print(type(SkillsOfStudent))

# Modify the skills values by adding one or two skills
SkillsOfStudent.insert(0,'Python')
SkillsOfStudent.insert(1,'Arduino')
student['skills'] = SkillsOfStudent
print(student)

# Get the dictionary keys as a list
KeysOfStudents = student.keys()
print(KeysOfStudents)

# Get the dictionary values as a list
ValuesOfStudents = student.values()
print(ValuesOfStudents)

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.pop('first_name')
print(student)

# Delete one of the dictionaries
del dogs
print(dog)