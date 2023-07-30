# Using the Decorator Class file as a reference, 
# try and write a class decorator that remembers the 
# arguments passed to the following function. If that
# value has been given before, output an additional line
# that states how many times it's been previously called.

# EXPAND THIS CLASS
class MonitorDecorator:
    def __init__(self, function):
        self.function = function
    
    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)



@MonitorDecorator
def what_is_this_number(num):
    return f'The number entered is {num}!'

print(what_is_this_number(4))
print(what_is_this_number(4))

