from random import choice


# # Create a function to calculate exchance rate for mobile phone price.
#
# def mobile_price_bdt(mobile_price, exchange_rate):
#     bd_price = mobile_price * exchange_rate
#     return bd_price
#
# iphone = mobile_price_bdt(720, 104.29)
# print(iphone)
#
# # Create dynamic text with function
#
# def greetings(name):
#     text = f'Hello {name}, Good Morning. How are you doing today?'
#     return text
#
# print(greetings('Aminul'))
#
# # Create Voter or Non Voter Cheking function with age.

# def voter_check(age):
#     if age >= 18:
#         return 'You are a voter'
#     else:
#         return 'Sorry, you are still kid'
#
#
# print(voter_check(33))

# Create Function for HTML Paragraph and Heading
#
# paragraph1 = 'This is paragraph one'
# paragraph2 = 'This is paragraph two'
# paragraph3 = 'This is paragraph three'
#
# def paragraph_html(text):
#     html = f'<p>{text}</p>'
#     return html
#
# print(paragraph_html(paragraph1))
# print(paragraph_html(paragraph2))
# print(paragraph_html(paragraph3))
#
# def h2_html(text):
#     h2 = f'<h2>{text.title()}</h2>'
#     return h2
#
# print(h2_html('best laptop computer'))

# Create Function to find even number fron any list.

# number_list = [1,24,5,3,6,7,84,6,7,8,5,7,7,65,5,4,4,3,23,7,56,67,54,344,32]
#
# def find_even_number(list):
#     even_number_list = []
#     for number in list:
#         if number % 2 == 0:
#             even_number_list.append(number)
#     return even_number_list
#
# print(find_even_number(number_list))

# Create a function to multiply all numbers from the list

number_list = [3,5,56,3,7,8,6,5,6,7,89]

# def multiply_number(list):
#     total = 1
#     for number in list:
#         total *= number
#     return total
#
# multi = multiply_number(number_list)
#
# print(multi)

# Create a function to check prime number

# def prime_number(number):
#     if number == 1:
#         return f'{number} is not a prime number'
#     elif number == 2:
#         return f'{number} is a prime number'
#
#     else:
#         i = 2
#         for i in range(2, number):
#             if number % i == 0:
#                 return f'{number} is not a prime number'
#             i += number
#         else:
#             return f'{number} is a prime number'
#
# print(prime_number(39))

# Function to calculate Fahrenheit to Celsius

# def fehrenheit_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5 / 9
#     return celsius
#
# print(fehrenheit_celsius(72))

# Multiple Value Return

# def add_sub(a,b):
#     addition = a + b
#     subtraction = a - b
#     return addition, subtraction
#
# result = add_sub(20, 10)
#
# print(result)

# print(print.__doc__)

# # Change the value from the list by calling their index number.
# names = ['Moon', 'Sadriel', 'Ibrahim', 'Nayem', 'Redwan']
#
# names[0] = 'Aminul'
#
# print(names)

# Function for sentence concatenation and make paragraph tag


sentence1 = [
    'GitHub, Inc. is an Internet hosting service for software development and version control using Git.',
    'Software development and Git version control are provided by GitHub, Inc. via the Internet.',
    'Software development and version control using Git are both provided by GitHub, Inc.'
]

sentence2 = [
    'It provides the distributed version control of Git plus access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project.',
    'It offers each project access control, bug tracking, software feature requests, task management, continuous integration, and wikis in addition to Git\'s distributed version control.',
    'It offers each project wikis, access control, bug tracking, software feature requests, continuous integration, and Git\'s distributed version control.'
]

sentence3 = [
    'GitHub is where over 83 million developers shape the future of software, together.',
    'More than 83 million developers collaborate on GitHub to define the direction of software.',
    'More than 83 million developers work together on GitHub to change the software landscape.'
]


# def paragraph_concate(s1, s2, s3):
#     """
#     This function will concatenate sentence and make paragrave tag
#     :param s1: sentence list one
#     :param s2: sentence list two
#     :param s3: sentence list three
#     :return: paragraph tag from random choice sentence.
#     """
#
#     paragraph = choice(s1) + choice(s2) + choice(s3)
#     return f'<p>{paragraph}</p>'
#
# random_para = paragraph_concate(sentence1, sentence2, sentence3)
#
# print(random_para)

# Concatenate Random sentence with multiple arguments

def random_sentence(*args):
    paragraph = ''
    for sentence in args:
        paragraph += choice(sentence)
    return f'<p>{paragraph}</p>'

ptag_sentence = random_sentence(sentence1, sentence2, sentence3)
print(ptag_sentence)