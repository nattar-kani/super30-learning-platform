from user import User


class Student(User):
    """Represent a student enrolled in the Super30 platform."""

    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.course_name = None
        self.completed_assignments = []

    def assign_course(self, course_name):
        """Assign a course to the student."""
        self.course_name = course_name

    def submit_assignment(self, assignment_name):
        """Mark an assignment as completed."""
        self.completed_assignments.append(assignment_name)

    def display_info(self):
        """Display student information."""
        print(f"Student: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")
        print(f"Course: {self.course_name}")
        print(
            f"Completed Assignments: {self.completed_assignments}"
        )