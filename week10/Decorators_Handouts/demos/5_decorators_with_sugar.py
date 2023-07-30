def enhance_my_function(func):
    def inner_wrapper():
        print("Something is happening BEFORE a simple function is called ")
        func()
        print("Something is happening AFTER a simple function is called ")
    return inner_wrapper

@enhance_my_function
def simple_function():
    print("I am a simple function")

simple_function()