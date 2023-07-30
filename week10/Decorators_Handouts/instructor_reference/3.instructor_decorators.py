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


# 2. A function can **return another function**.
#
# DEMO EXAMPLE

def outer_called():
    def inner_returned():
        print("Hello CFG cohort!")
    return inner_returned  # we return a function, we don't call it, hence not inner_returned()!


example_function = outer_called()

# Outputs "Hello CFG cohort!"
example_function()


# DEMO EXAMPLE

def pet_owner(num):
    def first_pet():
        return "Hi, I am a cat called Tigger."

    def second_pet():
        return "Hi, I am a dog called Butch."

    if num == 1:
        return first_pet
    else:
        return second_pet


# show return vs invoke returned functions
first = pet_owner(1)
second = pet_owner(2)

print(first)
print(second)

# VS

print(first())
print(second())


# 3. A decorator takes in a function, adds some functionality and returns it.

def enhance_my_fucntion(func):
    def inner_wrapper():
        print("Something is happening BEFORE a simple function is called ")
        func()
        print("Something is happening AFTER a simple function is called ")
    return inner_wrapper


def simple_function():
    print("I am a simple function")


simple_function()
decorated = enhance_my_fucntion(simple_function)
decorated()


# SPECIAL SYNTACTICAL SUGAR FOR DECORATORS

@enhance_my_fucntion
def simple_function():
    print("I am a simple function")

simple_function()

###############################################################

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


#####################################################################

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


##########################################################################

## Chain decorators together ###

def equal_sign(func):
    def inner(*args, **kwargs):
        print("=" * 30)
        func(*args, **kwargs)
        print("=" * 30)
    return inner


def pipe_sign(func):
    def inner(*args, **kwargs):
        print("|" * 30)
        func(*args, **kwargs)
        print("|" * 30)
    return inner


@equal_sign
@pipe_sign
def display_message(msg):
    print(msg)


display_message("Hello CFG cohort!")


# change the order of your decorators
@pipe_sign
@equal_sign
def display_message(msg):
    print(msg)


display_message("Hello CFG cohort!")

########################################################

# Class Decorator example with *args and **kwargs

class MyClassDecorator:
    def __init__(self, simple_function):
        self.function = simple_function

    def __call__(self, *args, **kwargs):
        print("something happens BEFORE function call")
        self.function(*args, **kwargs)
        print("something happens AFTER function call")


# adding class decorator to the function
@MyClassDecorator
def my_function(name, message):
    print("{}, {}".format(message, name))


my_function("CFG cohort", "Hello")


# EXERCISE

class SquareDecorator:

    def __init__(self, simple_function):
        self.function = simple_function

    def __call__(self, *args, **kwargs):
        print("something happens BEFORE function call")
        result = self.function(*args, **kwargs)
        print("something happens AFTER function call")
        return result ** 2


@SquareDecorator
def multiply(a, b):
    print("Your numbers are:", a, ' and ', b)
    return a * b


print("Result with SquareDecorator is:", multiply(2, 3))

######################
# Classes can keep state!


class SquareDecoratorWithMemory:

    def __init__(self, simple_function):
        self.function = simple_function
        self._memory = []

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs) ** 2
        self._memory.append(result)
        return result

    def memory(self):
        print('_' * 10)
        return self._memory


@SquareDecoratorWithMemory
def multiply(a, b):
    print("Your numbers are:", a, ' and ', b)
    return a * b


print("Result with SquareDecoratorWithMemory is:", multiply(2, 3))
print("Result with SquareDecoratorWithMemory is:", multiply(2, 2))
print("Result with SquareDecoratorWithMemory is:", multiply(3, 3))
print("Memory:", multiply.memory())


################### TIMER EXERCISE #######################
"""
Creating a @timer decorator.
It will measure the runtime a function takes to execute decorated function and print the duration to the console.
"""
import time


def timer(func):
    def inner_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('-' * 20)
        print(f"Finished {func.__name__!r} in {run_time:.8f} secs")
        return value
    return inner_wrapper


@timer
def worker_function_numbers(num):
    total_sum = 0
    for n in range(num):
        total_sum = total_sum + sum([(i/2 + 5) for i in range(1000)])
    return total_sum


@timer
def worker_function_strings(word):
    new_word = ''
    for char in word:
        new_word = new_word + ''.join('ZZZ-' + char + '-ZZZ-')
    return new_word.rstrip('-')


print(worker_function_numbers(1))
print(worker_function_numbers(80))

print(worker_function_strings('CFG'))
print(worker_function_strings('supercalifragilisticexpialidocious'))


############## CACHE EXERCISE ##############

"""
Creating a @memoize decorator.
It will cache results of a function with specific parameters and would instantaneously provide an answer instead
"""


class MemoizeDecorator:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self.cache:
            print("I did not run a function, just fetched a result for you! :)")
            return self.cache[key]

        value = self.function(*args, **kwargs)
        self.cache[key] = value
        return value


@MemoizeDecorator
def worker_function_numbers(num):
    total_sum = 0
    for n in range(num):
        total_sum = total_sum + sum([(i/2 + 5) for i in range(1000)])
    return total_sum


## run worker function many times with different arguments

for i in range(10):
    print(worker_function_numbers(i))

print(worker_function_numbers.cache)

## run again to see check a value was cached
print(worker_function_numbers(3))

