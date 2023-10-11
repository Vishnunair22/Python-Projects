# Prompt the user to enter a two-digit number and store it as a string
number = input("Enter a two-digit number:\n")

# Extract the individual digits from the input string and convert them to integers
# Then, calculate the sum of the two digits
sum_of_digits = int(number[0]) + int(number[1])

# Print the result, displaying the original number and its sum of digits
print(f"Sum of digits of {number} is {sum_of_digits}")
