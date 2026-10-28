from flask import Blueprint, jsonify, request

from app.services.course_service import CourseService
from app.models.course import Course

course_api = Blueprint("course_api", __name__)
course_service = CourseService()


@course_api.route("/courses", methods=["GET"])
def get_courses():
    return jsonify([
        course.to_dict()
        for course in course_service.get_all_courses()
    ])


@course_api.route("/courses/<course_code>", methods=["GET"])
def get_course(course_code):
    course = course_service.get_course(course_code)

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    return jsonify(course.to_dict())


@course_api.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json(silent=True) or {}

    required = ["course_code", "course_name", "credits"]
    if any(field not in data for field in required):
        return jsonify({"error": "All course fields are required"}), 400

    try:
        course = Course(
            data["course_code"],
            data["course_name"],
            int(data["credits"])
        )
        course_service.create_course(course)

        return jsonify({
            "message": "Course created successfully",
            "course_code": course.course_code
        }), 201
    except (ValueError, TypeError) as error:
        return jsonify({"error": str(error)}), 400


@course_api.route("/courses/<course_code>", methods=["PUT"])
def update_course(course_code):
    data = request.get_json(silent=True) or {}
    allowed = {"course_name", "credits"}
    updates = {
        key: value for key, value in data.items()
        if key in allowed
    }

    if not updates:
        return jsonify({
            "error": "Provide at least one valid field to update"
        }), 400

    if "credits" in updates:
        try:
            updates["credits"] = int(updates["credits"])
        except (ValueError, TypeError):
            return jsonify({
                "error": "Credits must be a valid integer"
            }), 400

    if course_service.get_course(course_code) is None:
        return jsonify({"error": "Course not found"}), 404

    try:
        course_service.update_course(course_code, **updates)
        return jsonify({"message": "Course updated successfully"})
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@course_api.route("/courses/<course_code>", methods=["DELETE"])
def delete_course(course_code):
    if course_service.get_course(course_code) is None:
        return jsonify({"error": "Course not found"}), 404

    course_service.delete_course(course_code)
    return jsonify({"message": "Course deleted successfully"})
