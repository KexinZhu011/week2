"""Users can add, search, update, and delete students' grades."""
class Student:
    # constructor
    def __init__(self, name, grade):
        """Initialize the student with a name and grade."""
        self.name = name
        self.grade = grade
        
    # method
    def get_info(self):
        """Return a string with the student's name and grade."""
        return f"{self.name}'s grade is: {self.grade}"


class StudentManager:
    def __init__(self):
        """Initialize an empty dictionary to store students."""
        self.students = {}

    def add_student(self, student):
        """Add a student to the dictionary, using the student's name as the key."""
        self.students[student.name] = student

    def get_student_grade(self, name):
        """Return the grade for the given student name, or a message if not found."""
        if name in self.students:
            return self.students[name].get_info()
        else:
            return f"No record found for {name}"

    def delete_student(self, name):
        """Delete a student from the dictionary by name."""
        if name in self.students:
            del self.students[name]
            print(f"Deleted student record for {name}.")
        else:
            print(f"No record found for {name}")

    def update_student(self, name):
        """Update a student's grade by name."""
        if name in self.students:
            try:
                new_grade = float(input(f"Enter the new grade for {name}: "))
                self.students[name].grade = new_grade
                print(f"Updated {name}'s grade to {new_grade}.")
            except ValueError:
                print("Invalid grade. Please enter a valid number.")
        else:
            print(f"No record found for {name}")

    def input_students(self):
        """Continuously get input for student names and grades until the user types 'stop'."""
        while True:
            student_name = input("Enter the student's name (or type 'stop' to finish): ")

            # If the user types "stop", exit the loop
            if student_name.lower() == 'stop':
                break

            # Get the student's grade
            try:
                grade = float(input(f"Enter {student_name}'s grade: "))
                student = Student(student_name, grade)
                self.add_student(student)
            except ValueError:
                print("Invalid grade. Please enter a valid number.")

    def query_student(self):
        """Prompt the user to enter a student's name and display their grade."""
        student_name = input("Enter the student's name to check the grade: ")
        print(self.get_student_grade(student_name))


def main():
    """Main function to drive the student grade management system."""
    student_manager = StudentManager()

    while True:
        action = input("Do you want to add, search, delete, update a student, or quit? (add/search/delete/update/quit): ").lower()

        if action == 'add':
            student_manager.input_students()

        elif action == 'search':
            student_manager.query_student()

        elif action == 'delete':
            student_name = input("Enter the student's name to delete: ")
            student_manager.delete_student(student_name)

        elif action == 'update':
            student_name = input("Enter the student's name to update the grade: ")
            student_manager.update_student(student_name)

        elif action == 'quit':
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


# Run the main function
if __name__ == "__main__":
    main()