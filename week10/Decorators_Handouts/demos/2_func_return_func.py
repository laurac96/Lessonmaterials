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