# Days left to live program
# Prompt user to enter their current age and store it in the variable age
age = int(input("Enter your age in numbers:\n"))

# Find the number of years left by finding the difference between the current age and the value 90 and store it as years_left
years_left = 90 - age

# Find the number of months in years_left and store it as months_left
months_left = years_left * 12

# Find the number of weeks in years_left and store it as weeks_left
weeks_left = years_left * 52

# Find the number of days in years_left, considering leap years, and store it as days_left
days_left = years_left * 365 + (years_left // 4)

# Print years_left, months_left, weeks_left, and days_left using f-strings
print(f"You have {years_left} years, {months_left} months, {weeks_left} weeks, and {days_left} days left.")
