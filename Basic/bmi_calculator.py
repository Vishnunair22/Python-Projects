# Prompt the user to enter their weight in kilograms and store it in the 'weight' variable.
weight = float(input("Enter your weight in kilograms:\n"))

# Prompt the user to enter their height in meters and store it in the 'height' variable.
height = float(input("Enter your height in meters:\n"))

# Calculate the Body Mass Index (BMI) using the formula: weight / (height * height)
# Round the result to 2 decimal places and store it in the 'bmi' variable.
bmi = round((weight / (height * height), 2)

# Print the calculated BMI with an informative message.
print(f"Your body mass index is {bmi}")
