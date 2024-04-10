#  Unit 2 Midunit activity 
# Author: Crystal Li
# Date: April 10, 2024

# Find the longest word in a sentence
def find_longest_word(word_sentence):
    longest_word = ""
    for word in word_sentence:
        # len = returning the number of items in the list 
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Using function
def main():
    words = input("Put in sentence separated by spaces: ").split()
    longest = find_longest_word(words)
    print(f"The longest word in the sentence is:", longest)
    
# Check if the code is being run as the "main program"
if __name__ == "__main__":
    main()