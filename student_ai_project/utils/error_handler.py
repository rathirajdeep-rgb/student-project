from flask import jsonify
from student_ai_project.utils.response import error_response
from student_ai_project.utils.exceptions import ValidationError

def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_error(e):
        return jsonify(error_response(e.message)), 400
    @app.errorhandler(Exception)
    def handle_general_error(e):
        return jsonify(error_response("Internal Server Error")), 500