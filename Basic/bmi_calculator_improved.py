# Prompt the user to enter weight in kilograms and height in meters
weight = float(input("Enter your weight in kilograms:\n"))
height = float(input("Enter your height in meters:\n"))

# Calculate BMI and round it to 2 decimal places
bmi = round(weight / (height * height), 2)

# Check the BMI category and display the result
if bmi < 18.5:
    print(f"Your BMI value is {bmi}. You are underweight.")
elif 18.5 <= bmi <= 24.9:
    print(f"Your BMI value is {bmi}. You are normal weight.")
elif 25.0 <= bmi <= 29.9:
    print(f"Your BMI value is {bmi}. You are overweight.")
else:
    print(f"Your BMI value is {bmi}. You are obese.")
