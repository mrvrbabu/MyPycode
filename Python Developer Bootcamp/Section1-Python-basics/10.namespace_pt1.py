# ----------------------------------------------------------------------- #
# --------------- ** Name Space part 1  **  ----------------------------- #


# Example 1
number = 1001

print(id(number))
print(id(1001))


# Example 2
print("\n")
print("Exmple 2")

a = 2
print("a", id(a))

a = a + 1
print("a1", id(a))

print("\n")
b = 2
print("b:", id(b))
print("Two:", id(2))


# Example 3
print("\n")
print("Example 3")
something = 12
print(something)
something = "Jack"
print(something)
something = ["a", 2, True]
print(something)


# Example 4
print("\n")
print("Example 4")


# Function starts with def keyword for define

def hello():
    print("Hello world")


something = hello
something()
