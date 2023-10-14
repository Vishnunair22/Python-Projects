# Prompt the user to enter a list of scores separated by commas.
scores_input = input("Enter the scores in any order separated by commas:\n")

# Split the input string into a list of scores.
scores = scores_input.split(',')

# Initialize a variable to keep track of the highest score.
high_score = 0

# Iterate through the list of scores.
for score in scores:
    # Convert the score to an integer.
    score = int(score)
    
    # Check if the current score is higher than the current high score.
    if score > high_score:
        # If it is, update the high score to the current score.
        high_score = score

# Print the highest score.
print(f"The highest score is {high_score}.")
