# This is a simple Python program that generates a band name based on user input.
# It asks the user for their favorite color and the city where they grew up,
# Then combines these inputs to create a band name and displays it to the user.
print("Welcome to Band name generator")

# Prompt the user to enter their favorite color and store it in the 'color' variable.
color = input("Enter your favourite color:\n")

# Prompt the user to enter the city where they grew up and store it in the 'city' variable.
city = input("Enter the city where you grew up:\n")

# Display the generated band name to the user by combining 'color' and 'city' variables.
print("Your band name could be:\n" + (color) + " " + (city))
 
