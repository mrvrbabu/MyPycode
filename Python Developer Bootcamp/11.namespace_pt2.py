# ----------------------------------------------------------------------- #
# --------------- ** Name Space part 2  **  ----------------------------- #

# A namespace is basically a collection of names

# Built-in Namespace
# Module: Global Namespace
# Function: Local Namespace


# *** Example 1

def outer():
    outer_number = 1008765
    print(id(outer_number))
    global global_number
    global_number = 101
    print("Printing global from inside outer function", global_number)

    def inner():
        inner_number = 200
        inner_number = "Jack"
        print("Inner number is ", inner_number)

        outer_number = 50055
        print("\n")
        print(id(outer_number))
        print("Outer number", outer_number)
        print("Printing global from inside inner function", global_number)

    inner()


global_number = 300
print(global_number)

outer()

# print(global_number)
