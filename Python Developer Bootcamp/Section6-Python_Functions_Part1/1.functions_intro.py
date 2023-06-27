# ----------------------------------------------------------------------- #
# ----------------- ** Python functions Part 1   **----------------------- #


# Functions are samall chunks of reusuable code that we write in order keep our applictions maintainable and more manageable.

# Functions execute logic

def book():
    print("Thriller ")


# book - means were are passing the reference to this function in some other piece of code
book()


success = True


def operation():
    if success:
        print("Yay !!")


operation()


def sum():
    for x in range(4, 34, 4):
        print(x)


sum()
