# Ask the user to input a year in numbers
year = int(input("Enter a year in numbers:\n"))

# Check if the year is divisible by 4
if year % 4 == 0:
    # If it's divisible by 4, it could potentially be a leap year.
    # However, we need to check other conditions.
    
    # Check if the year is also divisible by 100
    if year % 100 == 0:
        # If it's divisible by 100, it might still be a leap year
        # but only if it's also divisible by 400.
        
        # Check if the year is divisible by 400
        if year % 400 == 0:
            # If it's divisible by 400, it is a leap year.
            print(f"Given year {year} is a leap year.")
        else:
            # If it's divisible by 100 but not by 400, it's not a leap year.
            print(f"Given year {year} is not a leap year.")
    else:
        # If it's divisible by 4 but not by 100, it is a leap year.
        print(f"Given year {year} is a leap year.")
else:
    # If it's not divisible by 4, it's not a leap year.
    print(f"Given year {year} is not a leap year.")
