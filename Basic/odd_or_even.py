# Prompt the user to enter a number and store it as 'number'
number = int(input("Enter any number:\n"))

# Check if the number is odd or even using the '%' operator and print 'odd' or 'even' accordingly
if number % 2 != 0:
    print(f"Given number {number} is odd.")
else:
    print(f"Given number {number} is even.")