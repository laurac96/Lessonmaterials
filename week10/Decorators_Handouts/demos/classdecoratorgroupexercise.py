# Using the Decorator Class file as a reference,
# try and write a class decorator that remembers the
# arguments passed to the following function. If that
# value has been given before, output an additional line
# that states how many times it's been previously called.

# EXPAND THIS CLASS
class MonitorDecorator:
    def __init__(self, function):
        self.function = function
        self.memory = []

    def __call__(self, *args, **kwargs):
        num = str(args) + str(kwargs)
        if num in self.memory:
            return "This value has already been given"
        else:
            self.memory.append(num)
        return self.function(*args, **kwargs)


@MonitorDecorator
def what_is_this_number(num):
    return f'The number entered is {num}!'


print(what_is_this_number(4))
print(what_is_this_number(4))
print(what_is_this_number(4))
print(what_is_this_number(4))
print(what_is_this_number(4))
print(what_is_this_number(4))