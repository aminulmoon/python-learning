# print('Hello. Aminul is here', 'I am a Python Developer.', sep=' : ')

# # Primitive Data Types
#
# name = 'Ananta Jalil'       # str
# movie_name = 'Drama of Mariam'      # str
# movie_rating = 5.0      # float
# budget = 5000           # int
# is_it_perfect = True          # bool
#
# # Check Data Types
#
# print(type(name))
# print(type(budget))
# print(type(is_it_perfect))


# Data Casting
#
# a = int('45')
# b = float(23)
# c = str(69)
# d = int(4.50)
#
# print(type(d))

# Arithmetic Operators
# + Operator

# num1 = 30
# num2 = 20
# sumetion = num1 + num2
# print(sumetion)
#
# # - Operator
#
# cash = 20_000
# loan = 12_000
# remaining = cash - loan
# print(remaining)

# * and / Operator

# land = 40
# height = 20
# area = (land * height) / 2
# print('Tha area of the triangle is', int(area))

# Exponent, Floor Division, Modulus

# Find the result of 5 to the power 7
#
# a = 5 ** 7
# print(a)
#
# b = 30
# c = 4
# d = b // c
# print(d)
# e = b % c
# print('The Modulus of 30/4 is:', e)

# Problem Solving
# Write a program to calculate the area of a circle

# PI = 3.1416
# radius = 15
# area = PI * (radius ** 2)
# print('The area of the circle is', area)

# Write a program for Temperature Conversion (Fahrenheit to Celsius)

# fahrenheit = 94.6
# celsius = (fahrenheit - 32) * (5 / 9)
# print('The temperature of', fahrenheit, 'degree fahrenheit is:', celsius, 'Degree Celsius.')

# Round Function

# num1 = 300
# num2 = 7
# division = num1 / num2
# print(round(division,2))

# Find the area of a rectangle
# width = 3.4556
# length = 3.334
# area = round(width * length,2)
# print(area)

# Absolute, Binary, Hexa, Octal
# abs, bin, hex, oct

# x = -8
# print(abs(x))
# y = 34555
# print(bin(y))
# z = 23
# print(hex(z))
# zz = 3573
# print(oct(zz))

# String Concatenation
# 1. String can addition with another string
# 2. String can multiplication with a number

# first_name = 'Aminul '
# last_name = 'Islam '
# full_name = first_name + last_name
# print(full_name)
# print(full_name * 5)

# print('Moon' + str(2))
# print(int('5') + 4)


# Escape Character, New Line, Tab
# Escape Character= \
# New Line= \n
# Tab= \t

"""
Hello,
I'm Aminul Islam Moon. I'm a Python Developer. I want to say "Good Morning!"
"""

# print('Hello,\nI\'m Aminul Islam Moon. I\'m a Python Developer. I want to say "Good Morning!"')

"""
Twinkel Twinkel Little Star.
    How I wonder!
        What you are?
Twinkel Twinkel Little Star.
"""
# print('Twinkel Twinkel Little Star.\n\tHow I wonder!\n\t\tWhat you are?\nTwinkel Twinkel Little Star.')

# Raw String and Formated String

# print(r'Here is the folder to access the course: H:\Python Learning\02 Module-2')

# name = 'Aminul'
# profession = 'Python Developer'
# age = 27
# place = 'Manikganj'
"""
My name is Aminul. I am a Python Developer. I am 27 years old. I live in Manikganj.
"""

# print(f'My name is {name}. I am a {profession}. I am {age} years old. I live in {place}.')

# Templated Post Creation

"""
Monno Ceramic has advertised a job post on Daily Star. According to the news they have decided to recruit 53 Operation Manager on their company.
"""
# company = 'Squire Pharma'
# newspaper = 'Prothom Alo'
# number_of_post = 23
# position = 'Executive Officer'
#
#
# main_text = f'{company} has advertised a job post on {newspaper}. According to the news they have decided to recruit {number_of_post} {position} on their company.'
# print(main_text)

# Multi Line String with Formated String

"""
The Mobile is released on: 5th Octobor
The Model of the Phone is: Iphone 23
The Camera of the phone is: 440M
The price in Bangladesh: 2000 BDT
"""

#
# released_date = input('Enter release date: ')
# released_month = input('Enter release month: ')
# model = input('Enter the model: ')
# camera = input('Enter camera px: ')
# price = input('Enter price: ')
#
# template = f"""
# The Mobile is released on: {released_date}th {released_month.capitalize()}
# The Model of the Phone is: {model.capitalize()}
# The Camera of the phone is: {camera}M
# The price in Bangladesh: {price} BDT
# """
# print(template)

# a = input('Enter: ')
# b = float(a)
# c = int(b)
# print(c, type(b))

# Comparision Operators ==, !=, >, <, >=. <=

# x = 1
# y = 2
# z = 1
#
# print(x == y )
# print(x != y )
# print(y == x )
# print(y != x )
# print(y > x )
# print(y >= x )
# print(x < y )
# print(x <= y )

# Practice Day-1

# Multi variable

x, y, z = 'Apple', 'Orange', 'Mango'
print(z)