"""
This program tells if a number is a divisor of other big number.
"""
def module (number):
    i = 10 % number
    list1 = [1]
    while there_isnt(i, list1):
        list1.append(i)
        i = (i * 10) % number
    return list1

    
def there_isnt (number, list1):
    i = 0
    while i < len(list1) and list1[i] != number:
        i = i + 1
    return not(i < len(list1))


def extend_list (number1, list1):
    number2 = numbers(number1)
    cocient = number2 / len(list1)
    if cocient != 0:
        list1.extend ((list1) * cocient)
    return list1


def numbers (number):
    i = 1
    while number > 10:
        number = number / 10
        i = i + 1
    return i


def multiply (number1, list1):
    i = 0
    list2 = []
    list1 = extend_list(number1, list1)
    while number1 != 0:
        number3 = number1 % 10
        number1 = number1 / 10
        number4 = list1[i] * number3
        list2.append (number4)
        i = i + 1
    return list2


#This is the main program.
    
def divisor (number1, number2):
    list1 = module(number2)
    while number1 > 9:
        list2 = multiply(number1, list1)
        number1 = sum(list2)
    return number1 == number2 or (number1) % number2 == 0

