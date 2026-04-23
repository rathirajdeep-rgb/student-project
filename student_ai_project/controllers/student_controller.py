from flask import Blueprint, request, jsonify
from student_ai_project.services.student_service import predict_marks, fetch_history, validate_business_rules, answer_student_question
from student_ai_project.validators.student_validator import validate_request
from student_ai_project.utils.response import success_response
import logging

logger = logging.getLogger(__name__)

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

    data = request.get_json()
    logger.info(f"Incoming Request: {data}")

     # validation steps
    validate_request(data)
    validate_business_rules(data)

    result = predict_marks(data)

    logger.info(f"Prediction success: {result}")
    return jsonify(success_response(result)), 200



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

    limit = request.args.get('limit', default=5, type=int)
    logger.info(f"Fetching history with limit: {limit}")
    data = fetch_history(limit)
    logger.info(f"Fetched {len(data)} records")
    return jsonify(success_response(data)), 200


@student_bp.route('/ask', methods=['POST'])
def ask():
    """
    Get Question Answered
    ---
    tags:
      - Question Answered
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            question:
              type: string
    responses:
      200:
        description: Answer
        schema:
          type: object
          properties:
            answer:
              type: string
    """
    data = request.get_json()
    question = data['question'].lower()
    logger.info(f"Question received: {question}")
    answer = answer_student_question(question)
    logger.info(f"Question successfully answered: {answer}")
    return jsonify(success_response({"answer": answer})), 200