# Unit 1 Activity
# Author: Crystal Li
# Date: 6 March 2024

# Greeting the user
print("Hello user, what is your name?")
name = input()

# Answering user with name
print(f"Thank you for telling me your name, {name}")

# Asking user what they like to eat
print(f"Hello {name}, what is your favourite food?")
fave_food = input()

# Answering user with fave food
print(f"Thank you for telling me that your favourite food is {fave_food}")


# Asking the user what their favourite colour is 

fave_colour = input("What is your favourite colour ")

# If they answer blue or red
if fave_colour.strip("!.?,").lower() == "blue" or fave_colour.strip("!.?,").lower()  == "red":
    print("I like that colour too!")
# If they answer yellow 
elif fave_colour.strip("!.?,").lower()  == "yellow":
    print("That is my favourite colour")

else:
    print("I don't like that colour")

# Create two variables, x and y
x = 100
y = -100

# If x is greater, equal to, or less than y, then print it out 

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("I think x is equal to y")

# Create function called say_goodbye
    # When you call it, it prints Goodbye
def say_goodbye():
    print("Goodbye!")


# Create function called say_goodbye_params
    # Paramater passed in is name of person we are saying goodbye to

def say_goodbye_params(name):
    print(f"Goodbye {name.capitalize()}!")

say_goodbye_params("Bob")
say_goodbye_params("bob")

# Create function called subtracter
# Put in two inputs
# Return the difference of the inputs
def subtracter(x:int, y:int) -> int:
    return x - y 
result = subtracter (2, 1)
print(result)   