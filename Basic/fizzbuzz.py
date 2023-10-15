# Print a welcome message.
print("Welcome to the Fizz-Buzz Game.")

# Ask the user for a number to stop counting.
target = int(input("Enter a number where you need to stop counting:\n"))

# Loop through numbers from 1 to the specified target.
for number in range(1, target + 1):
    # Check if the number is divisible by both 3 and 5.
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz-Buzz")
    # Check if the number is divisible by 3.
    elif number % 3 == 0:
        print("Fizz")
    # Check if the number is divisible by 5.
    elif number % 5 == 0:
        print("Buzz")
    # If none of the above conditions are met, print the number itself.
    else:
        print(number)
