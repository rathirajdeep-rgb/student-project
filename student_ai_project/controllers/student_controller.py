from flask import Blueprint, request, jsonify
from student_ai_project.services.student_service import predict_marks, fetch_history, validate_business_rues
from student_ai_project.validators.student_validator import validate_request
from student_ai_project.utils.response import success_response, error_response
import logging
logger = logging.getLogger()

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/predict', methods=['POST'])
def predict():
    """
    Predict student result
    ---
    tags:
      - Student
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            age:
              type: number
            study_hours:
              type: number
            attendance:
              type: number
            sleep_hours:
              type: number
    responses:
      200:
        description: student result
        schema:
          type: object
          properties:
            marks:
              type: number
            result:
              type: string
    """

    try:
        data = request.get_json()
        logger.info(f"Incoming Request: {data}")
        # validation steps
        error = validate_request(data)
        if error:
            logger.error(f"Validation_failed: {error}")
            return jsonify(error_response(error)), 400

        error = validate_business_rues(data)
        if error:
            logger.error(f"Validation_failed: {error}")
            return jsonify(error_response(error)), 400
        result = predict_marks(data)
        logger.info(f"Prediction success: {result}")
        return jsonify(success_response(result)), 200
    except Exception as e:
      logger.error("Exception in /predict")
      return jsonify(error_response(str(e))), 500

@student_bp.route('/history', methods=['GET'])
def get_history():
    """
    Get student history
    ---
    tags:
      - Student
    parameters:
      - name: limit
        in: query
        type: integer
        required: false
        default: 5
    responses:
      200:
        description: list of predictions
    """
    try:
        limit = request.args.get('limit', default=5, type=int)
        logger.info(f"Fetching history with limit: {limit}")
        data = fetch_history(limit)
        logger.info(f"Fetched {len(data)} records")
        return jsonify(success_response(data)), 200
    except Exception as e:
        logger.error("Exception in /history")
        return jsonify(error_response(str(e))), 500


