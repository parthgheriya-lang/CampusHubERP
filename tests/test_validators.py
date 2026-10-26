
from app.utils.validators import (
    validate_email,
    validate_student_id,
    validate_phone
)


def main():
    print("EMAIL VALIDATION:")
    print("Valid email:", validate_email("rahul@example.com"))
    print("Invalid email:", validate_email("rahulexample.com"))

    print("\nSTUDENT ID VALIDATION:")
    print("Valid ID:", validate_student_id("ST101"))
    print("Invalid ID:", validate_student_id("ST1"))

    print("\nPHONE VALIDATION:")
    print("Valid phone:", validate_phone("9876543210"))
    print("Invalid phone:", validate_phone("98765"))


if __name__ == "__main__":
    main()
