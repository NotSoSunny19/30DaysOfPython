# # Write a code which gives grade to students according to theirs scores:
# # 80-100, A
# # 70-89, B
# # 60-69, C
# # 50-59, D
# # 0-49, F
# Gimme_score = int(input('Enter your score to calculate grade: '))
# if Gimme_score in range(80,100):
#     print("Your grade is A")
# if Gimme_score in range(70,89):
#     print("Your grade is B")
# if Gimme_score in range(60,69):
#     print("Your grade is C")
# if Gimme_score in range(50,59):
#     print("Your grade is D")
# else:
#     print("Your grade is F")

# # Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# What_month = input('What month is it : ')
# Months = ('January','February','March', 'April','May','June','July','August','September','October','November','December')
# if What_month in Months:
#     if What_month in {'September','October','November'}:
#         print('season is Autumn')
#     elif What_month  in {'December','January','February'}:
#         print('season is Winter')
#     elif What_month  in {'March', 'April','May'}:
#         print('season is Spring')
#     else:
#         print('season is Summer')
# else:
#     print('Please enter the right month')

# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
Fav_Fruit = str(input('Enter a fruit: '))
if Fav_Fruit not in fruits:
    fruits.append(Fav_Fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')
