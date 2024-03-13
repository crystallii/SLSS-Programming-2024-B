# Strings Practice
# Author: Crystal Li
# Date: 14 February 2024

name = "Crystal"
grade = "grade 11"
user_name = input
age = input
hobby = input

# Greet the user
print("Hello user!")
print()

# Asking for name

print("What's your name?")
user_name = input()

# Greeting user with name
print(f"Hello {user_name}")
print()

# Asking them grade
print(f"I have a question, what grade is {user_name} in?")
grade = input()

# Respond specifically to grade question
print("Wow, thanks for sharing your grade!")
print()

# Second question: How old they are

print("I have another question, how old are you?")
age = input()
print()

# Responding to second question

print(f"Thank you for sharing your age, {user_name}")
print()

# Asking what their favourite colour is
print("One last question, what is your favourite hobby?")
hobby = input()
print()
# Responding to third question
print(f"Thank you for sharing that your favourite hobby is {hobby}")

# Saying goodbye using user's name
print()
print(f"It was nice talking to you {user_name}, have a nice day!")
