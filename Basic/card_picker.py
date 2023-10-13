import random

# Input: Enter the names of all the people who will pay the bill separated by a comma
names = input("Enter the names of all the people who will pay the bill separated by a comma:\n")

# Split the input names into a list
names_list = names.split(',')

# Calculate the number of people
n = len(names_list)

# Generate a random index to select a person
# Note: Random index should be in the range [0, n-1]
list_index = random.randint(0, n - 1)

# Select the person from the list using the random index
selected_person = names_list[list_index]

# Print the selected person to pay the bill
print(f"{selected_person} is selected to pay the bill.")
