# ----------------------------------------------------------------------- #
# ---------------------------- ** Scope  *------------------------------- #


# Local Variables
# Global Vairables

def message(date):
    content = "Something very cool has happened"
    # print(content)


message("May 22, 2100")

# print(date)
# print(content)


def comment(date):
    content = "amazing landscape"


comment("May 23, 2135")
# print(date)
# print(content)


content = "Just do it"


def post(date):
    content = "I am on a trip"
    print(content)


post("May 23, 2150")
print(content)


dog_name = "Hachi"


def animal_names():
    global dog_name
    dog_name = "Georgie"


animal_names()
print(dog_name)
