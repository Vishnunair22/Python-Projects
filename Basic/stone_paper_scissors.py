# Import the random module for generating random numbers
import random

# Print a welcome message and instructions for the game
print("Welcome to this game. Make your choice: Stone, Paper, or Scissors.")
# Get the user's choice as an integer (0 for Stone, 1 for Paper, 2 for Scissors)
user_choice = int(input("Enter 0 for Stone, 1 for Paper, or 2 for Scissors:\n"))

# Generate a random choice for the computer (0 for Stone, 1 for Paper, 2 for Scissors)
computer_choice = random.randint(0, 2)

# Determine and print the computer's choice
if computer_choice == 0:
    print("Computer chose Stone.")
elif computer_choice == 1:
    print("Computer chose Paper.")
else:
    print("Computer chose Scissors.")

# Check the game result and print the outcome
if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lost! Better luck next time.")
