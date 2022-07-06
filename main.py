# SUMMARY OF BASIC PYTHON CONCEPTS

#**********************************************
# BASIC OUTPUT
# print()
#**********************************************
print("Hello World")

#**********************************************
# VARIABLES, STRING & NUMBER DATA
# Variables - variable_name = _____
# String - str - sequence of characters enclosed in " " or ' '.
# Number - int, float - integer or decimal
#**********************************************
string_var = "Hello"
int_var = 7
float_var = 3.14

#**********************************************
# STRING OPERATIONS
# String Concatenation - add strings together with +
# String Interpolation - f-strings
#**********************************************
name = "Mr. V"
time_of_day = "Morning"
greeting = "Hello " + name + ". Have a great " + time_of_day + "!"
greeting2 = f"Hello {name}. Have a great {time_of_day}!"

#**********************************************
# NUMBER OPERATIONS
# Basic math operations - +, -, *, /, //, %, **, ( )
# import math - research math library
#**********************************************
sum = 2 + 3
difference = 5 - 4
product = 2 * 3
quotient = 8 / 2
floor_division = 7 // 2
remainder = 7 % 2
power = 2 ** 8

import math
sqrt = math.sqrt(25)
circle_area = math.pi * (7) ** 2

#**********************************************
# USER INPUT
# input() function - always returns string
# Numerical input - convert with int() & float()
#**********************************************
name = input("What is your name?")
age = int(input("What is your age?"))
height = float(input("What is your height in meters?"))

#**********************************************
# RANDOM NUMBERS
# import random
# random.randrange(low, high) - random integer b/t low inclusive, high exclusive
# random.randint(low, high) - random integer b/t low inclusive, high inclusive
# random.random() - random float b/t 0 inclusive, 1 exclusive
# random.uniform(low, high) - random float b/t low inclusive, high inclusive
#**********************************************
import random
random_int = random.randrange(1, 7)
random_int2 = random.randint(1, 6)
random_float = random.random()
random_float2 = random.uniform(2.5, 10.0)

#**********************************************
# BOOLEAN EXPRESSIONS
# Comparison Operators: >, >=, <, <=, ==, !=
# Logical Operators: and, or, not
#**********************************************
num = 5
bool_exp = num > 1 and num <= 10
bool_exp2 = num == 1 or num == 20
bool_exp3 = not (num > 5 and num < 15)

#**********************************************
# IF STATEMENTS
# Binary, Unary, Chained, Nested
# Indentation!!
#**********************************************

# Binary
num = 2
if (num != 2):
  print("Num is not 2")
else:
  print("Num is 2")

# Unary
num = 2
if (num != 2):
  print("Num is not 2")

# Chained
num = 2
if num < 5:
  print("Num is < 5")
elif num < 9:
  print("Num is >= 5 and < 9")
elif num < 15:
  print("Num is >= 9 and < 15")
else:
  print("Num is >= 15")

#**********************************************
# INCREMENT OPERATORS
# +=, -=, *=, /=, %=, //=, **=
#**********************************************
num = 2
num += 5 # num = num + 5
num -= 5 # num = num - 5
num *= 5 # num = num * 5
num /= 5 # num = num / 5
num %= 5 # num = num % 5
num //= 5 # num = num // 5
num **= 5 # num = num ** 5

#**********************************************
# LOOPS
# while, for
# Indentation!!
#**********************************************


