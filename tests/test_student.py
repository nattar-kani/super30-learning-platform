import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from student import Student


def test_student_creation():
    student = Student(
        "Test Student",
        "test@example.com",
        "S100",
    )

    assert student.name == "Test Student"
    assert student.email == "test@example.com"
    assert student.user_id == "S100"


def test_assign_course():
    student = Student(
        "Test Student",
        "test@example.com",
        "S101",
    )

    student.assign_course("Python")

    assert student.course_name == "Python"


def test_submit_assignment():
    student = Student(
        "Test Student",
        "test@example.com",
        "S102",
    )

    student.submit_assignment("OOP")

    assert "OOP" in student.completed_assignments