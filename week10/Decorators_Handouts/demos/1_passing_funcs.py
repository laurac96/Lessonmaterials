# 1. Functions can be **passed as arguments** to another function object.
#
# DEMO EXAMPLE


def add_one(x):
    return x + 1


def substract_one(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


# invoke
print(operate(add_one, 5))
print(operate(substract_one, 5))

