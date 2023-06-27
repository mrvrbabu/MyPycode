# ----------------------------------------------------------------------- #
# ------------- ** Required and optional parameters   **----------------- #


def going_to_school(day, holiday=True):
    if day == "sunday" or day == "saturday":
        print(f"Today is {day}, and I am not going to school ?")
    else:
        print(f"Today is {day} and I am going to school")


going_to_school("saturday")


def working_condition(device, status="working"):
    return f"The {device} is {status}"


print(working_condition("Drill Press"))
print(working_condition("Welding machine", "out of order"))


def subtract(x, z, y=15):
    return x - y - z


print(subtract(20, 5, 2))
