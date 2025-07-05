# Task 1: Dictionary Lookup of Student Marks

# Step 1: Create a dictionary of student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 74
}

# Step 2: Ask the user for a student name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display the marks or an error message
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found in the records.")
