# If Condition

# age = 17
# if age >= 18:
#     print('You can vote')
# if age < 18:
#     print('You can not vote')

# Find Leap Year

# year = 2024
# if year % 4 == 0:
#     print(year, 'is leap year')
# if year % 4 != 0:
#     print(year, 'is not leap year')

# If/Else Condition
# If you have only two option to choose use If/Else Condition

# age = 12
#
# if age >= 18:
#     print('You can vote')
# else:
#     print('You can not vote')


# Find Even or Odd number

# number = 323
#
# if number % 2 == 0:
#     print(number, 'is an even number')
# else:
#     print(number, 'is an odd number')

# If Condition with User Input Function

# age = int(input('Enter your age: '))
#
# if age >= 18:
#     print('You can vote')
# else:
#     print('You are still kid. LoL')

# If Else problem solving with user input

"""
Messi is a footballer. He is from Argentina. He is 36 years old.
"""

# name = input('Enter name: ')
# profession = input('Enter profession: ')
# country = input('Enter country: ')
# gender = input('Enter your gender (m/f): ')
# birth_year = input('Enter your birth year: ')
# age = 2022 - int(birth_year)
#
# if gender == 'm':
#     pronoun = 'He'
# else:
#     pronoun = 'She'
#
# text = f'{name} is a {profession}. {pronoun} is from {country}. {pronoun} is {age} years old.'
#
# print(text)

# If/Else/Elif

# number = 0
#
# if number > 0:
#     print('It is a positive number')
# elif number < 0:
#     print('It is a negative number')
# else:
#     print('It is ZERO')

# If/Else/Elif Problem Solving

# Write a programe to calculate grading system

# number = int(input('Enter your number: '))
#
# if number >= 80:
#     print('You got A+')
# elif number >= 70:
#     print('You got A')
# elif number >= 60:
#     print('You got A-')
# elif number > 50:
#     print('You got B')
# elif number >= 40:
#     print('You got C')
# elif number >= 33:
#     print('You got D')
# else:
#     print('Sorry! You are FAIL')

# Problem Solving

# Write a program that accepts integer (n) and compute tha value of n+nn+nnn. Eg: 5+55+555 =

# number = input('Enter a number: ')
# result = int(number) + int(number * 2) + int(number * 3)
# print(result)

# Write a Python program to sum of the first (n) positive integers.

# number = int(input('Enter any positive number: '))
# sum = number * (number + 1) / 2
# print(sum)

# Logical Operator / Multipule Condition = and/or/not

# age = int(input('Enter your age: '))
# gender = input('Enter your gender (m/f): ')
#
# if age > 35 and gender == 'm':
#     print('Hello Uncle!')
# elif age < 35 and gender == 'm':
#     print('Hello Vaia!')
# elif age > 35 and gender == 'f':
#     print('Hi Anti!')
# else:
#     print('Hi Apu!')

# x = 40
#
# if not (x > 9 or x > 10):
#     print('The condition Executed')
# else:
#     print('The condition is not Fulfilled.')

# name = input('Enter your name: ')
#
# if name == 'Koobly':
#     print('Hi, you got a baby.')
# elif name == 'Puja Cherry':
#     print('Will you be my babies father?')
# else:
#     print('You are not my Sakib Khan, Bye! Bye!')

name = input('Enter your name: ')

if name == 'Koobly' or name == 'Puja' or name == 'Aup':
    print('Hi, you got a baby.')
else:
    print('You are not my Sakib Khan, Bye! Bye!')