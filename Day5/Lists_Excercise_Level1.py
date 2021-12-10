# Declare an empty list
EmptyList = []
print(EmptyList)

# Declare a list with more than 5 items
NotSoEmptyList = [2,5,'Nope', {'well1stIndex':'You are', 'well2ndIndex':'pretty good'},'Yes','Yeah']
print(NotSoEmptyList)

# Find the length of your list
print(len(NotSoEmptyList))

# Get the first item, the middle item and the last item of the list
NotSoEmptyList = ['2','5','Nope','well1stIndex','You are', 'well2ndIndex','pretty good','Yes','Yeah']
# first_item, second_item, third_item , fourth_item, *rest , last_item = NotSoEmptyList
print(len(NotSoEmptyList))
# print(first_item)
# print(third_item)
# print(fourth_item)
# print(last_item)
print(NotSoEmptyList[0:9:4])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Suhith', 23, 5.6, 'Single', 'Hyderabad']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0:7:3])

# Print the list after modifying one of the companies
it_companies[0] = 'Capgemini'
print(it_companies)

# Add an IT company to it_companies
it_companies.insert(0,'Facebook')
print(it_companies)

# Change one of the it_companies names to uppercase
UCIT = it_companies[2].upper()
print(UCIT)

# Join the it_companies with a string '#;  '
StringToBeJoined = ['#;  ']
it_companies = it_companies + StringToBeJoined
print(it_companies)

# Check if a certain company exists in the it_companies list.
Does_exists = 'Capgemini' in it_companies
print(Does_exists) 

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies[0:3]
print(it_companies)

# Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop()
it_companies.pop()
it_companies.pop()
print(it_companies)

# Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(2)
print(it_companies)
it_companies.pop(2)
print(it_companies)
it_companies.pop(2)
print(it_companies)

# Remove the first IT company from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
print(it_companies)

# Remove all IT companies from the list
del it_companies[0:6]
print(it_companies)

# Destroy the IT companies list
it_companies.clear()
print(it_companies)

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.insert(full_stack.index('Redux')+1,'Python')
full_stack.insert(full_stack.index('Python')+1,'SQL')
print(full_stack)

