# ----------------------------------------------------------------------- #
# --------------- ** Number Methods & Operations **  -------------------- #

# https://docs.python.org/3/library/math.html

# Arithmetic Operations
import math

new_number = 5
print(new_number + 3)
print(new_number - 4)
print(new_number * 5)
print(new_number * 50 / 5)
print(new_number * 50 // 5)
print(new_number % 4)
print(new_number % 5)

print(2 ** 5)

# Augmented Assignment Operator

number = 10
number = number + 5
print("number is", number)
number += 5
print("number is ", number)

print("number += 5 is", number)

num1 = 10

num1 += 5
print(num1)

num1 *= 2
print(num1)
num1 /= 2
print(num1)

# round() method
some_num = 234.5677
print("some_num is", some_num, ",""round of some_numb is", round(some_num))

num2 = -123.987
print("num2 is ", num2, "absolute(abs) of num2 is ", abs(num2))

print(dir())
print(math.sin(180))
print(math.ceil(1.4))
print(math.ceil(1.1))
print(math.ceil(2.03))
