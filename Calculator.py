def add(*args):
    total = 0
    for number in args:
        total += number
    return total

def subtract(num1, num2):
    result = num1 - num2
    return result

def multi(*args):
    result = 1
    for number in args:
        result *= number
    return result

def divition(num1, num2):
    result = num1 / num2
    return result

