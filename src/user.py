class User:
    """Base class for users of the Super30 Learning Platform."""

    total_users = 0

    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id
        User.total_users += 1

    def display_info(self):
        """Display basic user information."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")

    @classmethod
    def get_total_users(cls):
        """Return the total number of registered users."""
        return cls.total_users

    @staticmethod
    def validate_email(email):
        """Validate the basic structure of an email address."""
        return "@" in email and "." in email.split("@")[-1]