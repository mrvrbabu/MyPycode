# ----------------------------------------------------------------------- #
# --------------- ** Nested Loops **  ----------------------------------- #


# Example 1

for x in range(3):
    for y in range(4):
        print(f"Point({x},{y})")


print("\n")


print("Example 2")

for x in range(1):
    for y in range(2):
        for z in range(3):
            print(f"Point({x}, {y}, {z})")
