
from pathlib import Path
from app.utils.logger import (
    LOG_FILE,
    log_student_added,
    log_student_updated,
    log_student_deleted,
    log_faculty_added,
    log_course_added,
    log_enrollment_created,
)

log_student_added("ST999")
log_student_updated("ST999")
log_student_deleted("ST999")
log_faculty_added("FC999")
log_course_added("CT999")
log_enrollment_created("ST999", "CT999")

print("Logging test completed.")
print(f"Log file: {LOG_FILE}")
print(f"Log file exists: {Path(LOG_FILE).exists()}")
