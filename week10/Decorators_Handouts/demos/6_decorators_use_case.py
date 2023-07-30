### Decorating Functions with Parameters ###

# this function accepts arguments
def divide(a, b):
    return a/b

# We know this function will give an error if we pass in b as 0.
# Make a decorator to check if an argument would cause any error.


def clever_divide(func):
    def inner_wrapper(a, b):
        print("Let's divide ", a, " by ", b)
        if b == 0:
            print("Whoops! cannot divide by zero")
            return
        return func(a, b)
    return inner_wrapper


@clever_divide
def divide(a, b):
    print(a/b)


divide(22, 2)
divide(22, 0)