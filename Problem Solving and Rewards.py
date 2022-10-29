"""
ইউজার থেকে একটা সংখ্যা ইনপুট নিতে হবে (১০,২০, ২৫, ৩০ ইত্যাদি যেকোনো সংখ্যা হতে পারে )। এবং প্রিন্ট করে দেখাতে হবে ঐ সংখ্যার ভিতর কত গুলা, প্রাইম সংখ্যা আছে এবং সংখ্যা গুলা কি কি ।
"""

# num = int(input('Enter Your Number Here: '))
# i = 2
# print("Prime numbers between", num, "and", i, "are:")
# for num in range(i, num + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#             else:
#                 print(num)

# number = int(input('Enter a number: '))
# i = 2
# while number > i:
#     if number % i != 0:
#         print(number,'is a prime number')
#         i += 1
#         break
#     else:
#         print(number,'is not a prime number')
#         break


number = int(input('Enter any number: '))
is_prime = False

i = 2
while i < number:
    if number % i == 0:
        is_prime = True
        break
    i += 1

if is_prime == True:
    print(number, 'is not prime number')
else:
    print(number, 'is prime number')