# Initialize a variable to store the sum of even numbers.
sum = 0

# Iterate through a range of numbers from 2 to 100 (inclusive) with a step of 2.
# This generates all even numbers from 2 to 100.
for num in range(2, 101, 2):
    # Add the current even number (num) to the running sum.
    sum += num

# Print the result, indicating the sum of the first 100 even numbers.
print(f"The sum of the first 100 even numbers is {sum}")
