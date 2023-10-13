# Import the 'random' module to generate random numbers
import random

# Generate a random integer between 0 and 1 (inclusive)
random_side = random.randint(0, 1)

# Check if the random integer is equal to 1
if random_side == 1:
    # If it is, print "Heads"
    print("Heads")
else:
    # If it's not 1, print "Tails"
    print("Tails")
