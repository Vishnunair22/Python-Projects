# Welcome the player to Treasure Island where great surprises await.
print("Welcome to the Treasure Island where great surprises await you.")

# Prompt the player to choose a direction.
print("You are at a crossroad. You can go either left or right. What do you choose?")
choice1 = input("Enter 'L' for Left or 'R' for Right:\n")

# Check the player's choice.
if choice1 == 'L':
    # Player chose 'L', and they are hit by a passing bus. Game over!
    print("You are hit by a passing bus. Game over!")
else:
    # Player chose 'R', and they move to the next round.
    print("Congratulations! You made it to the next round.")
    
    # Present the player with another choice at a river bank.
    print("You are at a river bank. You have two choices. You can either wait for a boat or swim across. What do you choose?")
    choice2 = input("Enter 'W' for Wait or 'S' for Swim:\n")
    
    # Check the player's choice at the river bank.
    if choice2 == 'W':
        # Player chose 'W' and successfully makes it to the next level.
        print("Congratulations! You made it to the next level.")
        
        # Present the player with more choices on a street.
        print("You are on a street. You see a red door, a green door, and a yellow door in front of you. Which one do you choose?")
        choice3 = input("Enter 'R' for Red door, 'G' for Green door, or 'Y' for Yellow door:\n")
        
        # Check the player's choice on the street.
        if choice3 == 'Y':
            # Player chose 'Y' and wins the game. Congrats!
            print("Congratulations! You win this game. Enjoy your victory.")
        else:
            # Player didn't choose 'Y', so they lost the game.
            print("Sorry, you lost the game. Better luck next time.")
    else:
        # Player didn't choose 'W' at the river bank, so they lost the game.
        print("Sorry, you lost the game. Better luck next time.")
