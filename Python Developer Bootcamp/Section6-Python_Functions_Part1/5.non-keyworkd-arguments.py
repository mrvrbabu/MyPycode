# ----------------------------------------------------------------------- #
# ------------------- ** Non-keyword arguments (*args)  *---------------- #


def sum(x, y):
    return x + y


print(sum(89, 98))
# print(sum(55, 66, 77, 88, 99))


def num(*numbers):
    return numbers


print(num(10, 20, 30, 40, 50, 60))


def subtract(*nums):
    number = 100
    for x in nums:
        number = number - x
    return number


print(subtract(2, 4, 5, 25, -45, 120))
