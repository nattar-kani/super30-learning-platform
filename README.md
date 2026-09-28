# Super30 Learning Platform

A mini Python project demonstrating Object-Oriented Programming (OOP) concepts using a simple learning platform.

## Project Overview

This application models a learning platform with three classes:

* `User` (Base Class)
* `Student` (inherits from User)
* `Mentor` (inherits from User)

The project demonstrates:

* Classes and Objects
* Constructors (`__init__`)
* Inheritance
* Instance Variables
* Instance Methods
* Class Variables
* Class Methods
* Static Methods
* Multiple Objects

## Project Structure

```text
super30-learning-platform/
│
├── src/
│   ├── main.py
│   ├── user.py
│   ├── student.py
│   ├── mentor.py
│   └── config.py
│
├── tests/
│   └── test_student.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Features

### User

* Stores name, email, and user ID
* Counts total users
* Validates email addresses

### Student

* Assign course
* Submit assignments
* Display student details

### Mentor

* Store expertise
* Assign students
* Display mentor details

## OOP Concepts Used

| Concept          | Implementation                       |
| ---------------- | ------------------------------------ |
| Class            | User, Student, Mentor                |
| Inheritance      | Student(User), Mentor(User)          |
| Constructor      | `__init__()`                         |
| Class Variable   | `total_users`                        |
| Class Method     | `get_total_users()`                  |
| Static Method    | `validate_email()`                   |
| Instance Methods | assign_course(), submit_assignment() |

## How to Run

Clone the repository:

```bash
git clone <repository-url>
cd super30-learning-platform
```

Run the application:

```bash
python src/main.py
```

Run tests:

```bash
python -m pytest
```

## Sample Output

```text
=== STUDENT 1 ===
Student: Nattarkani
Email: nattarkani@example.com
User ID: S001
Course: Python Programming
Completed Assignments: ['Python Basics', 'OOP']

=== MENTOR ===
Mentor: Priya
Email: priya@example.com
User ID: M001
Expertise: Python and AI
Students Assigned: 2

Total Users: 3
```

