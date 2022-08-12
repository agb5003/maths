import math
import array

a = int(input("Format: ax^m + bx^n + c\na = "))
m = int(input("m = "))
b = int(input("b = "))
n = int(input("n = "))
c = int(input("c = "))

checkers = [1, 2, 3, 5, 7, 11, -1, -2, -3, -5, -7, -11]

def checkEven(xVal):
    y_of_plus_x_value = a*pow(xVal, m) + b*pow(xVal, n) + c
    y_of_minus_x_value = a*pow(-xVal, m) + b*pow(-xVal, n) + c
    if y_of_plus_x_value == y_of_minus_x_value:
        return True
    else:
        return False

def checkOdd(xVal):
    y_of_minus_x_value = a*pow(-xVal, m) + b*pow(-xVal, n) + c
    minus_y_of_x_value = -(a*pow(xVal, m) + b*pow(xVal, n) + c)
    if y_of_minus_x_value == minus_y_of_x_value:
        return True
    else:
        return False

even_correct = 0
odd_correct = 0

for i in checkers:
    if checkEven(i) == True:
        even_correct += 1
    else:
        if checkOdd(i) == True:
            odd_correct += 1

if even_correct == 12:
    print("Function is even.")
elif odd_correct == 12:
    print("Function is odd.")
else:
    print("Function is neither even nor odd.")
