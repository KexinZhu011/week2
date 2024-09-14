# Create an empty dictionary to store student names and grades
grades = {}

# Continuously get input for student names and grades until the user types "stop"
while True:
    student_name = input("Enter the student's name (or type 'stop' to finish): ")

    # If the user types "stop", exit the loop
    if student_name.lower() == 'stop':
        break
    
    # Get the student's grade
    grade = float(input(f"Enter {student_name}'s grade: "))
    
    # Store the name and grade in the dictionary
    grades[student_name] = grade

# Query and print the student's grade
student_name = input("Enter the student's name to check the grade: ")

if student_name in grades:
    print(f"{student_name}'s grade is: {grades[student_name]}")
else:
    print(f"No record found for {student_name}")