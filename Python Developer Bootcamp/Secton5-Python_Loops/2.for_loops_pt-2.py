# ----------------------------------------------------------------------- #
# --------------- ** For Loops part 2 **  ------------------------------------- #


status = False
for number in range(1, 4):
    print(f"Attempt {number}")

    if status:
        print("Success")
        break

else:
    print("Failed")
