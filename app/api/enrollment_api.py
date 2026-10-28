from flask import Blueprint, jsonify, request

from app.services.enrollment_service import EnrollmentService
from app.services.student_orm_service import StudentORMService
from app.api.course_api import course_service

enrollment_api = Blueprint("enrollment_api", __name__)

student_service = StudentORMService()


enrollment_service = EnrollmentService(
    student_service=student_service,
    course_service=course_service
)


@enrollment_api.route("/enrollments", methods=["GET"])
def get_enrollments():
    return jsonify(enrollment_service.get_all_enrollments())


@enrollment_api.route("/enrollments/<enrollment_id>", methods=["GET"])
def get_enrollment(enrollment_id):
    enrollment = enrollment_service.get_enrollment(enrollment_id)

    if enrollment is None:
        return jsonify({"error": "Enrollment not found"}), 404

    return jsonify(enrollment)


@enrollment_api.route("/enrollments", methods=["POST"])
def create_enrollment():
    data = request.get_json(silent=True) or {}

    student_id = data.get("student_id")
    course_code = data.get("course_code")

    if not student_id or not course_code:
        return jsonify({
            "error": "student_id and course_code are required"
        }), 400

    try:
        enrollment = enrollment_service.create_enrollment(
            student_id, course_code
        )
        return jsonify({
            "message": "Enrollment created successfully",
            "enrollment": enrollment
        }), 201
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@enrollment_api.route("/enrollments/<enrollment_id>", methods=["PUT"])
def update_enrollment(enrollment_id):
    data = request.get_json(silent=True) or {}

    allowed = {"student_id", "course_code"}
    updates = {
        key: value for key, value in data.items()
        if key in allowed
    }

    if not updates:
        return jsonify({
            "error": "Provide student_id or course_code to update"
        }), 400

    try:
        enrollment = enrollment_service.update_enrollment(
            enrollment_id, **updates
        )
        return jsonify({
            "message": "Enrollment updated successfully",
            "enrollment": enrollment
        })
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@enrollment_api.route("/enrollments/<enrollment_id>", methods=["DELETE"])
def delete_enrollment(enrollment_id):
    try:
        enrollment_service.delete_enrollment(enrollment_id)
        return jsonify({
            "message": "Enrollment deleted successfully"
        })
    except ValueError as error:
        return jsonify({"error": str(error)}), 404

