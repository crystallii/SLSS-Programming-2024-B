# Lists and Modules
# Author: Crystal
# 8 March 2024 

import random 

def coin_flip():
     # Return heads or tails or other?
     # Heads is any number 0 to 0.4999999999
     # Tails is any number from 0.5 to 0.999991
     # Other is any number greater than 0.999991
    roll = random.random()

    if roll < 0.5:
        return "heads"
    elif roll < 0.999999:
        return "tails"
    else:
        return "other?"
    
    def main():
        # Keep track of heads and tails
        heads = 0
        tails = 0
        other = 0
        for _ in range(100):
            result = coin_flip()
            if coin_flip() == heads:
                heads = heads + 1
            elif result == "tails":
                tails = tails + 1 
        else:
            other = other + 1

        print(f"Number of heads: {heads}")
        print(f"Number of tails: {tails}")
        print(f"Number of heads: {other}")


