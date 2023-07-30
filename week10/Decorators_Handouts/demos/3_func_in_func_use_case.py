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

print(first) # There are extensions in here...
print(second)

# VS

print(first()) # We're actually calling the function here.
print(second())