# Prompt the user to enter their height in centimetres and store the value as 'height'
height = float(input("Enter your height in centimetres:\n"))

# Check if the user's height is greater than or equal to 120 centimeters
if height >= 120:
    # If the height is 120 centimeters or more, print 'allowed' message
    print("You are allowed to take this ride.")
    
    # Prompt the user to enter their age in numbers and store it as 'age'
    age = int(input("Enter your age in numbers:\n"))
    
    # Check the user's age
    if age <= 18:
        # If the age is 18 or less, print the ticket price
        print("Your ticket is 7 $.")
    else:
        # If the age is over 18, print the bill amount
        print("Your bill is 12 $.")
else:
    # If the height is less than 120 centimeters, print 'not allowed' message
    print("You are not allowed to take this ride.")
