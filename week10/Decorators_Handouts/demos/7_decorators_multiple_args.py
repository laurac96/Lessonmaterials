## Here lay monsters.

## 3. Make general decorators that work with any number of parameters.

## EXAMPLE

def universal_decorator(func):
    def inner_wrapper(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner_wrapper

#####################################################################


def run_func_twice_decorator(func):
    def wrapper_run_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_run_twice


@run_func_twice_decorator
def divide(a, b):
    print(a/b)


divide(10, 5)


@run_func_twice_decorator
def divide_three(a, b, c):
    print(a/b/c)


divide_three(300, 3, 2)