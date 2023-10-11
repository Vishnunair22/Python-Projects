# Tip Calculator
print("Welcom to the Tip Calculator")
# Get the bill amount from the user as a floating-point number
bill = float(input("Enter your bill in $:\n"))

# Get the number of people to split the bill between as an integer
numver_of_people = int(input("Enter the number of people to split the bill between:\n"))

# Get the tip percentage from the user as an integer
tip = int(input("Enter the percentage of bill you would like to give as a tip. Is it 10,12 or 15 %:\n"))

# Calculate the new bill by adding the tip to the original bill
new_bill = bill + round((bill * tip / 100),2)

# Calculate the share of the bill for each person
share = new_bill / numver_of_people

# Display the new bill amount with the tip
print(f"Your bill with {tip}% tip is ${new_bill:.2f}.")

# Display the amount each person should pay
print(f"Each person should pay ${share:.2f}.")
