# ----------------------------------------------------------------------- #
# ------------ ** Function parameters and arguments   **----------------- #


def arithmetic_operations(x, y):
    print(f"{x} * {y} = {x * y}")
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} % {y} = {x % y}")


# arithmetic_operations(3, 4)
arithmetic_operations(20, 5)


# def legal_age(name, age, allowed_age):
#     if age < 18:
#         print("You don't get license")
#     else:
#         print("You can drive")


# legal_age("Ram", 19, 18)


def legal_age(name, age, allowed_age):
    if age >= allowed_age:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")


legal_age("Ramu", 17, 18)
legal_age("Sarah", 18, 21)
