# Write a function to get the maximum value from three number.

# def max_value(a,b,c):
#     """
#     This function will take max value
#     :param a,b,c: item of numbers
#      :return: max value
#     """
#     if a > b and a > c:
#         return a
#     if b > a and b > c:
#         return b
#     else:
#         return c
# print(max_value(23,45,25))
# # print(max_value.__doc__)


# Write a function which receive redious and calculate the area of a circle and return area and circumstance.

# def area_circums(redius):
#     area = 2 * 3.1416 * (redius**2)
#     circums = 2 * 3.1416 * redius
#     return area, circums
#
# circle = area_circums(7)
#
# print(circle)
# print(type(circle))

# Multiple Arguments

# def sum(*args):
#     total = 0
#     for number in args:
#         total += number
#     return total
# print(sum(23,554,254,2,3))

# print('Amiul', 'Moon', sep= '+')

# def greetings(name, msg= 'What\'s up!'):
#     text = f'Hello {name}, {msg}'
#     return text
#
# print(greetings('Moon', msg= 'kita khobor?'))

# Arbitary Argument = *agrs

# import Calculator
#
# addition = Calculator.add(3,4,56,7,8,9,)
# print(addition)
#
# sub = Calculator.subtract(443,24)
# print(sub)
#
# divite = Calculator.divition(254,5)
# print(divite)
#
# multiply = Calculator.multi(234,3245,234,23,2,2)
# print(multiply)

# from Calculator import multi
#
# multiply = multi(2,3,43,4)
# print(multiply)
#
# from Calculator import divition as vag
#
# divi = vag(435,32)
# print(divi)

# import area
#
# base = 4
# height = 2
#
# measur_area = area.triangle(base,height)
# print('The area of the triangle is', measur_area)

# from area import rectangle
#
# leng = 5
# wid = 4
# total_area = rectangle(leng, wid)
# print(total_area)

# from area import circle as cir
#
# r = 5
# total_area = cir(r)
# print(total_area)

# Change value from tuple

# fruits = ('Mango', 'Banana', 'Lichi', 'Orange', 'Berry')
# # fruits[1] = 'Melon'
#
# fruits_list = list(fruits)
# fruits_list[1] = 'Avocado'
# fruits_tuple = tuple(fruits_list)
#
# print(fruits_tuple)
# for fruite in fruits_tuple:
#     print(fruite)

# Unpack Tuple

# nums = (3,34,22)
#
# x,y,z = nums
# print(x)
# print(y)
# print(z)

# Make single element into Tuple by using 'comma'

# name = ('Apple',)
# print(type(name))

# import requests
# r = requests.get('https://www.python.org')
# # print(requests.__doc__)
# # print(r.status_code)
# print(r.content)

# Access website data from requests librery
#
# import requests
# print(requests.__doc__)
# # r = requests.get('https://www.python.org')
# print(r.status_code)
# content = r.content
# content_python = json.loads(content)
#
# print(content_python)