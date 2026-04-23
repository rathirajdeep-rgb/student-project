import pandas as pd
import joblib
import os
import re

from student_ai_project.dao.student_dao import save_prediction, get_all_predictions, execute_custom_query
from student_ai_project.utils.exceptions import ValidationError



BASE_DIR = os.path.abspath(__file__)

PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../../"))
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "student_regression_model.pkl")

print(MODEL_PATH)

model = joblib.load(MODEL_PATH)

def predict_marks(data):
    student = pd.DataFrame([{
        'age': data['age'],
        'study_hours': data['study_hours'],
        'attendance': data['attendance'],
        'sleep_hours': data['sleep_hours']
    }])
    marks = float(model.predict(student)[0])
    result = "PASS" if marks >= 75 else "FAIL"

    #savet to DB
    save_prediction(data, marks, result)

    return {
        "marks": round(marks,2),
        "result": result
    }
def fetch_history(limit):
    data = get_all_predictions(limit)
    return data

# Business Rules
def validate_business_rules(data):
    age = data['age']
    study_hours = data['study_hours']
    attendance = data['attendance']
    sleep_hours = data['sleep_hours']
    if age < 18:
        raise ValidationError("Age must be >= 18 years")
    if not (0<= study_hours <= 24):
        raise ValidationError("Study hours must be between 0 ans 24")
    if not (0<=attendance<=100):
        raise ValidationError("Attendance must be between 0 and 100")
    if not (0<= sleep_hours <= 24):
        raise ValidationError("Sleep hours must be between 0 and 24")
    if sleep_hours + study_hours > 24:
        raise ValidationError("sum of Sleep hours and Study hours cannot be more than 24")
    return None # valid

def answer_student_question(question):
    if any (word in question for word in ["above", "more"]) and 'mark' in question:
        result = execute_custom_query("select AVG(marks) from student_predictions")
        return f" Average marks are {round(result[0][0],2)}"
    if any (word in question for word in ["average", "mean", "avg"]) and 'mark' in question:
        result = execute_custom_query("select AVG(marks) from student_predictions")
        return f" Average marks are {round(result[0][0],2)}"
    if any (word in question for word in ["average", "mean", "avg"]) and 'attendance' in question:
        result = execute_custom_query("select AVG(attendance) from student_predictions")
        return f" Average attendance is {round(result[0][0],2)}"
    if any (word in question for word in ["average", "mean", "avg"]) and 'study' in question:
        result = execute_custom_query("select AVG(study_hours) from student_predictions")
        return f" Average study hours are {round(result[0][0],2)}"
    if any (word in question for word in ["average", "mean", "avg"]) and 'sleep' in question:
        result = execute_custom_query("select AVG(sleep_hours) from student_predictions")
        return f" Average sleeping hours are {round(result[0][0],2)}"
    if "top student" in question or ('max' in question and 'marks' in question):
        result = execute_custom_query("select marks from student_predictions order by marks DESC limit 1")
        return f"Max marks are {result[0][0]}"
    if ("lowest" in question or 'min' in question) and 'marks' in question:
        result = execute_custom_query("select marks from student_predictions order by marks ASC limit 1")
        return f"Min marks are {result[0][0]}"

    # Dynamic filter
    base_query = "select count(*) from student_predictions"
    conditions = []

    # pass/ fail filter
    if 'pass' in question:
        conditions.append("result = 'Pass'")

    if 'fail' in question:
        conditions.append("result = 'Fail'")

    match = re.search(r"marks??\s*>\s*(\d+)", question)
    if match:
        conditions.append(f"marks >= {match.group(1)}")

    match = re.search(r"marks?\s*<\s*(\d+)", question)
    if match:
        conditions.append(f"marks <= {match.group(1)}")

    match = re.search(r"age\s*>\s*(\d+)", question)
    if match:
        conditions.append(f"age >= {match.group(1)}")

    if conditions:
        query = base_query + " where " + " AND ".join(conditions)
        result = execute_custom_query(query)
        return f"Found{result[0][0]} matching students"
    return " Sorry, I don't understand that question yet"
