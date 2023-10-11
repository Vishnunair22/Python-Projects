# Get the bill amount from the user as a floating-point number
bill = float(input("Enter your bill in $: "))

# Get the number of people to split the bill between as an integer
numver_of_people = int(input("Enter the number of people to split the bill between: "))

# Get the tip percentage from the user as an integer
tip = int(input("Enter the percentage: "))

# Calculate the new bill by adding the tip to the original bill
new_bill = bill + (bill * tip / 100)

# Calculate the share of the bill for each person
share = new_bill / numver_of_people

# Display the new bill amount with the tip
print(f"Your bill with {tip}% tip is ${new_bill:.2f}.")

# Display the amount each person should pay
print(f"Each person should pay ${share:.2f}.")
