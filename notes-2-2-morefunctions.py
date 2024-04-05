# More Functions
# Author: Crystal 
# 3 April 2024

# Implement stars function

def stars(num):
    """Returns specified number of *s"""
    value = ""  # placeholder for return value 

    if num == 0 or num == 1:
        value = "*"

    elif num > 1:
        value = "*" * num

    else:
        value = "Sorry, can't take negative numbers."

    # return "*" * num 
    return value 



# Multiply Strings
greeting = "hello" 
print(greeting * 5)

print("the quick brown fox jumps over the lazy dog" * 2)


# print(stars(10))    # "*****"
# print(stars(1000))  # "********"


# testing to see if code works
print(stars(0))
print(stars(1))
print(stars(1000))
print(stars(-1))


def biggest_of_three()