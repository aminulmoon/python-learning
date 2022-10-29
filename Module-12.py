# Introduction to Function

# samsung_price = 345
# exchange_rate = 103.25
# samsung_bdt = samsung_price * exchange_rate
# print(samsung_bdt)

#DRY (Don't Repit Yourself so use function)
#
# def mobile_price_bdt(price, exchange_rate):
#     bdt_price = price * exchange_rate
#     return bdt_price
#
# samsung_price = mobile_price_bdt(345, 103.25)
# iphone_price = mobile_price_bdt(673, 102.96)
# print(samsung_price)
# print(iphone_price)

# Exploring Function

# def greetings(name):
#     # print('Hello', name)
#     return f'Hello, {name}'
#
# my_greet = greetings('Aminul Islam Moon')
# print(my_greet)

# Voter Check
#

# Add HTML tag in paragraph

# paragraph1 = 'This is paragraph one'
# paragraph2 = 'This is paragraph two'
# paragraph3 = 'This is paragraph three'
# paragraph4 = 'This is paragraph four'
#
#
# def paragraph_html(paragraph):
#     paragraph_html = f'<p>{paragraph}</p>'
#     return paragraph_html
#
# paragraph1_html = paragraph_html(paragraph1)
# paragraph2_html = paragraph_html(paragraph2)
# paragraph3_html = paragraph_html(paragraph3)
# paragraph4_html = paragraph_html(paragraph4)
#
# print(paragraph1_html)
# print(paragraph2_html)
# print(paragraph3_html)
# print(paragraph4_html)
#
# def h2(text):
#     h2 = f'<h2>{text.title()}</h2>'
#     return h2
#
# print(h2('top 10 product review'))

# Find even number from the given list using function

list_1 = [2,3,45,5,4,6,7,8,423,57,88,99,665,32,63,78,84,37,85,235,24]
list_2 = [42,43,445,45,44,56,75,86,866,6423,557,588,5499,36635,332,633,738,843,373,825,2235,224]

# even_num_list = []
# for number in list_2:
#    if number % 2 == 0:
#     even_num_list.append(number)
#
# print(even_num_list)

# def even_num_finder(list):
#     even_num_list = []
#     for number in list:
#         if number % 2 == 0:
#             even_num_list.append(number)
#     return even_num_list
#
# even_list_1 = even_num_finder(list_1)
# even_list_2 = even_num_finder(list_2)
#
# print(even_list_1)
# print(even_list_2)

# Write a python function to multiply all the number from list.

number_list = [2,3,4,6,73,7,8,3,8,3]
#
# result = 1
# for number in number_list:
#     result *= number
#
# print(result)

# def multiply_number(list):
#     result = 1
#     for number in list:
#         result *= number
#     return result
#
# multi_num_result = multiply_number(number_list)
# print(multi_num_result)

# Writh a Python function that takes a number as a parameter and check the number is prime or not.

def check_prime(number):
    if number == 1:
        return f'{number} is not prime number'
    elif number == 2:
        return f'{number} is prime number'
    else:
        for i in range(2,number):
            if number % i == 0:
                return f'{number} is not prime number'
            i += 1
        else:
            return f'{number} is prime number'

print(check_prime(7))

# Convert Fahrenheit to Celsius
# def fah_to_cel(fahrenheit):
#     celsius = (fahrenheit - 32) * 5 / 9
#     return celsius
# print(fah_to_cel(98.4))

# Multipul Value Return Function

# def add_sub(a, b):
#     """
#     This function will create addition and subtraction of two numbers.
#     :param a: number one
#     :param b: number two
#     :return: return multiple value
#     """
#     addition = a + b
#     subtraction = a - b
#     return addition, subtraction
#
# result = add_sub(34, 20)
# print(result)
#
# print(add_sub.__doc__)

# Introduce of Tuple

# name_tuple = ('Aminul', 'Sohag', 'Rajib', 'Sadriel', 'Redwan')
# name_list = ['Moon', 'Sajib', 'Ibrahim', 'Moin', 'Rini']
#
# name_list[1] = 'Ashik'
# name_tuple[2] = 'Roni' #'tuple' object does not support item assignment
# print(name_list)

# Random Paragraph Create with Function

"""
# Google LLC is an American multinational technology company that focuses on search engine technology. 
# 
# It has been referred to as the "most powerful company in the world". 
# 
# Its parent company Alphabet is considered one of the Big Five American information technology companies.
# """
#
# from random import choice
#
# sentence1 = [
#     'Google LLC is an American multinational technology company that focuses on search engine technology.',
#     'An American multinational technology business with an emphasis on search engine technology is called Google LLC.',
#     'The American multinational technology business Google LLC specializes in search engine technology.'
#              ]
#
# sentence2 = [
#     'It has been referred to as the "most powerful company in the world".',
#     'The phrase "most powerful company in the world" has been used to describe it.',
#     'The "most powerful company in the world" is how some have described it.'
# ]
#
# sentence3 = [
#     'Its parent company Alphabet is considered one of the Big Five American information technology companies.',
#     'One of the Big Five American information technology businesses is its parent corporation, Alphabet.',
#     'One of the Big Five American information technology businesses, Alphabet, is the parent company of this business.'
# ]

# def paragraph_formation(s1,s2,s3):
#     rendom_paragraph = choice(s1) + choice(s2) + choice(s3)
#     return f'<p>{rendom_paragraph}</p>'
# print(paragraph_formation(sentence1,sentence2,sentence3))
# print(paragraph_formation(sentence1,sentence2,sentence3))
# print(paragraph_formation(sentence1,sentence2,sentence3))

# Multiple Parameters in function

# def multiple_additon(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum
# sum_result = multiple_additon(3,4,23,4,5)
# print(sum_result)

# Template with multiple paramiters

# from random import choice
# sentence1 = [
#     'Google LLC is an American multinational technology company that focuses on search engine technology.',
#     'An American multinational technology business with an emphasis on search engine technology is called Google LLC.',
#     'The American multinational technology business Google LLC specializes in search engine technology.'
#              ]
#
# sentence2 = [
#     'It has been referred to as the "most powerful company in the world".',
#     'The phrase "most powerful company in the world" has been used to describe it.',
#     'The "most powerful company in the world" is how some have described it.'
# ]
#
# sentence3 = [
#     'Its parent company Alphabet is considered one of the Big Five American information technology companies.',
#     'One of the Big Five American information technology businesses is its parent corporation, Alphabet.',
#     'One of the Big Five American information technology businesses, Alphabet, is the parent company of this business.'
# ]
#
# def paragraph_html(*args):
#     paragraph = ''
#     for sentence in args:
#         paragraph += choice(sentence)
#     return f'<p>{paragraph}</p>'
#
# html_paragrahp = paragraph_html(sentence1, sentence2, sentence3)
# print(html_paragrahp)
