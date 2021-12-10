# Create an empty tuple
from typing import List


EmptyTuple  = ()
print(EmptyTuple)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Brothers = ('Chotu', 'Nishu')
Sisters = ('Bubbly','Pinky')
print(Brothers)
print(Sisters)

# Join brothers and sisters tuples and assign it to siblings
Siblings = Brothers + Sisters
print(Siblings)

# How many siblings do you have?
print(len(Siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
SiblingsList = list(Siblings)
SiblingsList.append('Mom')
SiblingsList.append('Dad')
family_members = tuple(SiblingsList)
print(family_members)
