# Loops and Iteration
# Author: Crystal
# April 5, 2024

# Print "something" 10 times
for _ in range(10):
    print("something")

# print out every item in my grocery list
grocery_list = [
    "dishwasher tabs",
    "aluminum foil",
    "blueberry muffins",
    "RTX 4090 Super"
] 

for item in grocery_list:
    print("----")
    print(item)
    if item == "blueberry muffins":
        break

# Count from 0 to 9
for i in range(1000):
    print(i)

    # Modulo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    if i % 2 == 0:
        print(f"{i} is an even number")

# Rewrite the above for loop as a while loop
counter = 0

while counter < 1000:
    if counter % 2 == 0:
        print(f"{counter} is an even number")
    else: 
        print(counter)

    # increment counter by 1
    # counter = counter + 1
    counter +=1