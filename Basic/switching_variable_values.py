# Get the first number from the user and convert it to an integer
first_number = int(input("Enter a number:\n"))

# Get the second number from the user and convert it to an integer
second_number = int(input("Enter another number:\n"))

# Print the numbers entered by the user
print("You entered " + str(first_number) + " and " + str(second_number))

# Swap the values of first_number and second_number
new_number = first_number
first_number = second_number
second_number = new_number

# Print the numbers after swapping
print("The numbers after swapping are " + str(first_number) + " and " + str(second_number))
