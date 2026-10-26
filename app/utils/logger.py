
import logging
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Log directory and file
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "application.log"

# Configure application logger
logger = logging.getLogger("CampusHubERP")
logger.setLevel(logging.INFO)

# Avoid adding duplicate handlers
if not logger.handlers:
    file_handler = logging.FileHandler(
        LOG_FILE, encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def log_student_added(student_id):
    logger.info("Student Added: %s", student_id)


def log_student_updated(student_id):
    logger.info("Student Updated: %s", student_id)


def log_student_deleted(student_id):
    logger.info("Student Deleted: %s", student_id)


def log_faculty_added(faculty_id):
    logger.info("Faculty Added: %s", faculty_id)


def log_course_added(course_code):
    logger.info("Course Added: %s", course_code)


def log_enrollment_created(student_id, course_code):
    logger.info(
        "Enrollment Created: Student=%s, Course=%s",
        student_id,
        course_code
    )
