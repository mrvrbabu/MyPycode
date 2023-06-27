# ----------------------------------------------------------------------- #
# --------------------- ** Data Types Part 2 ** ------------------------- #

"""
--Data Types ---                      --Class--                        --Values--
integers                              -> int                            -> 45 
Floating Point Numbers                -> float                          -> 8.5 
booleans                              -> bool                           -> True/False
strings                               -> str                            -> "Welcome Home"
list                                  -> list                           -> [1, 2, 3]
dictionary                            -> dict                           -> {"user_name": "Ram", "user_id": 45}
tuple                                 -> tuple                          -> (10, 20, 30)
set                                   -> set                            -> {"cat", 99}

"""

# *_*_*_* -------------------------  Lists  -------------------------------
# Ordered 
list1 = [1, 3, 4.5, 7, 9]
print(list1)
print(type(list1))

mixed = [4, 6, True, ['a', 'b', 7.8]]
print(mixed)
print(type(mixed))
# *_*_*_* -------------------------  Dictionary -------------------------------
# Unordered collection of key value pairs 
dictionary1 = {"user_name": "Ajanta Super Market", "Location": "Maldives" }
print(dictionary1)
print(type(dictionary1))


# *_*_*_* -------------------------  Tuples --------------------------------
# Ordered sequence of items same as list but it is immutable(cannot be changed)
mixed_tuple = (2, 3, 4, 5, True, "Keerthi", [1, 2, 3])
print(mixed_tuple)
print(type(mixed_tuple))

# *_*_*_* -------------------------  Sets -------------------------------
# Unordered 
mixed_set = {2, 3.4, "Krishi",  4, 5, False, "Keerthi"}
print(mixed_set)
print(type(mixed_set))
