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

    def __call__(self, num):
        value_passed_times = self.memory.count(num)
        if value_passed_times > 0:
            print(f"I have {value_passed_times} records of those arguments.")
        self.memory.append(num)
        return self.function(num)


@MonitorDecorator
def what_is_this_number(num):
    return f'The number entered is {num}!'


print(what_is_this_number(4))
print(what_is_this_number(4))
print(what_is_this_number(3))
print(what_is_this_number(4))
print(what_is_this_number(19))
print(what_is_this_number(1))