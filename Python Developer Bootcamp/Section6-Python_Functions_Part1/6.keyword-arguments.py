# ----------------------------------------------------------------------- #
# ------------------- ** keyword arguments (**kwargs)  *----------------- #

# Note: non-keywork agrument returns a tuple
#       A keyword argument returns a dictionary


def employee(**info):
    print(info)


employee(name="Clint", last_name="Eastwood", age=34, skill_set="Actor")


def to_do(**to_do_status):
    return to_do_status


result = to_do(morning="Wakeup and get ready to school", afternoon="Have lunch",
               evening="return home and have snacks and go to tution")

print(result)
