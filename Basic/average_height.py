# Prompt the user to enter student heights as a comma-separated string
student_height = input("Enter student heights in centimeters separated by commas:\n")

# Split the input string into a list of individual heights
student_height = student_height.split(',')

# Initialize variables to keep track of the number of students, total height, and average height
number_of_students = 0
total_height = 0

# Iterate through the list of student heights
for student in student_height:
    total_height += int(student)  # Convert each height to an integer and add it to the total height
    number_of_students += 1  # Increment the student count

# Calculate the average height by dividing the total height by the number of students
average_height = total_height / number_of_students

# Print the results
print(f"The total height of {number_of_students} students is {total_height} centimeters.")
print(f"The average height of {number_of_students} students is {average_height} centimeters.")
