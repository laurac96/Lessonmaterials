class SquareDecorator:

    def __init__(self, simple_function):
        self.function = simple_function
        # self._memory = []

    def __call__(self, *args, **kwargs):
        print("something happens BEFORE function call")
        result = self.function(*args, **kwargs)
        # self._memory.append(result)
        print("something happens AFTER function call")
        return result ** 2
    
    # def memory(self):
    #     print('_' * 10)
    #     return self._memory


@SquareDecorator
def multiply(a, b):
    print("Your numbers are:", a, ' and ', b)
    return a * b


print("Result with SquareDecorator:", multiply(2, 3))
# print("Result with SquareDecorator:", multiply(2, 9))
# print("Result with SquareDecorator:", multiply(3, 0))
# print("Memory:", multiply.memory())
