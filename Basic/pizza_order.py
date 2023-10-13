# Display a welcome message
print("Welcome to Pizza Order Program.")

# Prompt the user for their preferred pizza size
size = input("Enter your preferred pizza size. Enter 'S' for Small, 'M' for Medium, or 'L' for Large pizza:\n")

# Prompt the user for the choice of pepperoni
pepperoni = input("Do you want pepperonis with your pizza? Enter 'Y' for Yes or 'N' for No:\n")

# Prompt the user for the choice of cheese
cheese = input("Do you want cheese with your pizza? Enter 'Y' for Yes or 'N' for No:\n")

# Initialize the bill amount to zero
bill = 0

# Calculate the cost based on the selected pizza size
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

# Calculate the additional cost for pepperoni, if selected
if size == 'S' and pepperoni == 'Y':
    bill += 1
elif size == 'M' or size == 'L' and pepperoni == 'Y':
    bill += 2
else:
    bill += 0

# Calculate the additional cost for cheese, if selected
if cheese == 'Y':
    if size == 'S':
        bill += 1
    else:
        bill += 2

# Display the total bill amount to the user
print(f"Your total bill amount is {bill} $.")
