from app.api.student_api import app
from app.api.faculty_api import faculty_api
from app.api.course_api import course_api
from app.api.enrollment_api import enrollment_api

app.register_blueprint(faculty_api)
app.register_blueprint(course_api)
app.register_blueprint(enrollment_api)

if __name__ == "__main__":
    app.run(debug=True)
