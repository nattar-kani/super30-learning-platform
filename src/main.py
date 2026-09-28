from mentor import Mentor
from student import Student
from user import User


def main():
    # Create multiple student objects
    student1 = Student(
        "Nattarkani",
        "nattarkani@example.com",
        "S001",
    )

    student2 = Student(
        "Arun",
        "arun@example.com",
        "S002",
    )

    # Create mentor object
    mentor1 = Mentor(
        "Priya",
        "priya@example.com",
        "M001",
        "Python and AI",
    )

    # Assign courses
    student1.assign_course("Python Programming")
    student2.assign_course("Generative AI")

    # Submit assignments
    student1.submit_assignment("Python Basics")
    student1.submit_assignment("OOP")
    student2.submit_assignment("Python Basics")

    # Assign students to mentor
    mentor1.assign_student()
    mentor1.assign_student()

    # Display information
    print("=== STUDENT 1 ===")
    student1.display_info()

    print("\n=== STUDENT 2 ===")
    student2.display_info()

    print("\n=== MENTOR ===")
    mentor1.display_info()

    # Static method
    print("\n=== EMAIL VALIDATION ===")
    print(User.validate_email(student1.email))

    # Class method
    print("\n=== TOTAL USERS ===")
    print(User.get_total_users())


if __name__ == "__main__":
    main()