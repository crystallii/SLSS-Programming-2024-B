# Mcdobot excercise 
# Author: Crystal
# 21 February 2024

# Ask if they want meal with fries

fries_answer = input("Would you like your meal with fries?")

# If they say yes
if fries_answer.strip(" .?!,").lower() == "yes":
    print("Here is your meal with fries! Thank you")

# If they say no
elif fries_answer.strip(" .?!,").lower() == "no":
    print("Here is your meal without fries! Thank you")

# If they say anything else
else: 
    print("Sorry, I didn't understand that")

