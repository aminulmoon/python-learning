# CHALLENGE 1:
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.


# salary = int(input('Enter you salary: '))
# service_years = int(input('Enter your years of service: '))
# amount = salary + (salary * 5 / 100)
#
# if service_years > 5:
#     print('Your total salary with bonus is', amount)
# else:
#     print('You are not eligible for bonus')


# CHALLENGE 2:
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity. Suppose, one unite will cost 100. Judge and print total cost for user.

#
# unite = int(input('Please, enter how many units you have purchased: '))
# unite_price = unite * 100
# total = unite_price - (unite_price * 10 / 100)
#
# if unite_price > 1000:
#     print('Congratulations! Your total discounted price is: ', total)
# else:
#     print('Sorry! You do not get any discount. Shop more for 10% discount! \nYour total price is: ', unite_price)


# IF CONDITION LEVEL TWO:
#
# => Ask user to enter age, sex (M or F), marital status (Y or N) and then using following rules print their place of service.
#
# =>If employee is female then she will work only in urban area.
#
# =>If employee is a male and age is in between 20 to 40 then he may work in anywhere.
#
# =>If employee is male and age is in between 40 to 60 then he will work in urban areas only.
#
# => And any other input of age should print "ERROR".


# age = int(input('Enter your age: '))
# sex = input('Enter your gender (M or F): ')
# # marital_status = input('Enter your marital status (Y or N): ')
# if sex.upper() == 'F' and age >= 20 and age <= 60:
#     print('You will work only in urban area.')
# elif sex.upper() == 'M' and age >= 20 and age <= 40:
#         print('You will work in anywhere.')
# elif sex.upper() == 'M' and age >= 40 and age <= 60:
#         print('You will work only in urban area.')
# elif age > 61:
#         print('Sir, it\'s retire time. You better take rest at home: LOL')
# else:
#     print('ERROR!\nSorry! You are not eligible to work now.')



# CHALLENGE LEVEL TWO:
#
# A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of original one. E.g-
# INPUT: 1234	OUTPUT: 4322
# INPUT: 5982	OUTPUT: 2895


# number = int(input('Enter any number 2 to 16 digit: '))
# while number >= 1:
#     print(number % 10, end='')
#     number = int(number / 10)


# i = 0
# i = 0+1 = 1
# i = 1+2 = 3
# i = 3+3 = 6
# i = 6+4 = 10
# i = 10+5 = 15


# WHILE LOOP CHALLENGE:
# 1. Find the average value of first 'n' number using loop.


# number = int(input('Enter a positive number: '))
# sum = 0
# i = 1
# while i <= number:
#     sum = sum + i
#     i += 1
# average = sum / number
# print('The average value of first', number, 'is: ', average)



# 2. Write a program to check whether a number is prime or not?

number = int(input('Enter a number: '))
i = 2
while number > 1:
    if number % i != 0:
        print(number,'is a prime number')
        i += 1
        break
    else:
        print(number,'is not a prime number')
        break


# number = int(input('Enter a number: '))
# i = 2
# while 2 <= number:
#     if number % i == 0:
#         i += 1
#         print('It is not prime number')
#
#     else:
#         print('It is a prime number')
#         break


# 3. Write a program to print sum of first 10 Even number.

# sum = 0
# even_number = 0
# while even_number < 20:
#     even_number += 2
#     sum = sum + even_number
# print('Sum of first 10 Even number is:',sum)


# 4. Write a program to print the factorial of a number accepted from users.

# number = int(input('Enter a positive number: '))
# factorial = 1
# i = 1
# while i <= number:
#     factorial = factorial * i
#     i += 1
# print('The factorial of', number,'is:',factorial)
