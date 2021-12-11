# Unpack siblings and parents from family_members
family_members = ('Chotu', 'Nishu', 'Bubbly', 'Pinky', 'Mom', 'Dad')
*Siblings,mom, dad = family_members
parents = (mom,dad)
print(tuple(Siblings))
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits_products = ('Jaggery', 'Juice', 'Sugar')
vegetable_products = ('Manchuria', 'Gajar ka Halwa', 'vegetable Oil')
animal_products = ('Shawarma', 'Butter', 'Milk')
food_stuff_tp = fruits_products+vegetable_products+animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if(len(food_stuff_lt) % 2 == 1 ):
    MidIndex = int(len(food_stuff_lt)/2)
    food_stuff_lt.pop(MidIndex);
else:
    MidIndex1 = int((len(food_stuff_lt)-1)/2)
    MidIndex2 = int((len(food_stuff_lt))/2)    
    food_stuff_lt.pop(MidIndex1);
    food_stuff_lt.pop(MidIndex2);
food_stuff_tp = tuple(food_stuff_lt)
print(food_stuff_tp)

# Slice out the first three items and the last three items from food_staff_lt list
fruits_products = ('Jaggery', 'Juice', 'Sugar')
vegetable_products = ('Manchuria', 'Gajar ka Halwa', 'vegetable Oil')
animal_products = ('Shawarma', 'Butter', 'Milk')
food_stuff_tp = fruits_products+vegetable_products+animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[3:6])

# Delete the food_staff_tp tuple completely
fruits_products = ('Jaggery', 'Juice', 'Sugar')
vegetable_products = ('Manchuria', 'Gajar ka Halwa', 'vegetable Oil')
animal_products = ('Shawarma', 'Butter', 'Milk')
food_stuff_tp = fruits_products+vegetable_products+animal_products
del food_stuff_tp 
print(food_stuff_tp)

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if('Estonia'in str(nordic_countries)):
    print('Estonia is a nordic country')
if('Iceland'in str(nordic_countries)):
    print('Iceland is a nordic country')
