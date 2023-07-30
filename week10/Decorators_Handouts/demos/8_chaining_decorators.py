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


# @equal_sign
# @pipe_sign
# def display_message(msg):
#     print(msg)


# display_message("Hello CFG cohort!")


# change the order of your decorators
@pipe_sign
@equal_sign
def display_message(msg):
    print(msg)


display_message("Hello CFG cohort!")