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