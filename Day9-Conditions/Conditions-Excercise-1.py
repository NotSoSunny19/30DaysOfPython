#     Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.

age = int(input('Enter your age: '))
if age >= 18:
    print(' You are old enough to drive')
else:
    missing_years = str(18 - age)
    print('You need '+ missing_years +' more years  to learn to drive')

#     Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#     Enter your age: 30
#     You are 5 years older than me.
my_age = int(input('Enter my age: '))
your_age = int(input('Enter your age: '))
if my_age > your_age:
    diff_in_age = abs(my_age-your_age)
    if diff_in_age == 1:
        print('Youre an year younger to me')
    else:
        print('Youre '+ str(diff_in_age) +' years younger to me')
elif my_age == your_age:
    print('You and I are of the same age')
else:
    diff_in_age = abs(my_age-your_age)
    if diff_in_age == 1:
        print('Youre an year elder to me')
    else:
        print('Youre '+ str(diff_in_age) +' years elder to me')

#     Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a_num = int(input('Enter 1st number: '))
b_num = int(input('Enter 2st number: '))
if a_num > b_num:
    print(str(a_num) + ' greater than ' + str(b_num))
elif a_num == b_num:
    print(str(a_num) + ' equal to ' + str(b_num))
else:
    print(str(a_num) + ' less than ' + str(b_num))
