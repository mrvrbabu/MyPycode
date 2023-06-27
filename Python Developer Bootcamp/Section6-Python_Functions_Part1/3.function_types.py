# ----------------------------------------------------------------------- #
# ------------ ** Function parameters and arguments   **----------------- #


# 1 - Functions that perform a task
# 2 - Functions that calcuate and return a value


def facebook(name, status):
    return f"{name} is {status}"


user_status = facebook("William", "offline")
print(user_status)

user_status = facebook("Serena", "online")
print(user_status)
