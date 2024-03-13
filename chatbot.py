# Chatbot
# Author: Crystal
# March 8 2024

import random 
# 1. Greets the user
print("Hello there!")

# 2. Asks them "how are you" or something like that
user_feeling = input("How are you feeling?")

# 3. Responds with a general statement that is randomly chosen
#   - create a list of possible responses
#   - randomly choose a response
#   - print that response
good_possible_resp = ["I'm really happy for you.",
                    "That's really great to hear.",
                     "That's really good news!"]

if user_feeling == "good" or user_feeling == "great":  
    # randomly choose a response
    chosen_response = random.choice(good_possible_resp)
    # print that response 
    print(chosen_response)

bad_possible_resp = ["I'm sorry you feel that way",
                     "Do you want to talk about it?", 
                     "Are you feeling okay?"]
if user_feeling == "bad" or user_feeling == "not too good":
   chosen_response = random.choice(bad_possible_resp)
print(chosen_response )


# 4. Says goodbye

print("Well, thank you for your time!")
