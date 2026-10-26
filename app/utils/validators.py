
import re


def validate_email(email):
    """Validate a basic email format."""
    pattern = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))


def validate_student_id(student_id):
    """Validate student IDs such as ST101 or ST202."""
    pattern = r"^ST\d{3}$"
    return bool(re.fullmatch(pattern, student_id))


def validate_phone(phone):
    """Validate a 10-digit phone number."""
    pattern = r"^\d{10}$"
    return bool(re.fullmatch(pattern, phone))
