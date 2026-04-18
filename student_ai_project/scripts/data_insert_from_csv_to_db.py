import pandas as pd
from student_ai_project.dao.student_dao import save_prediction
import os

base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "data", "student_data.csv")
df = pd.read_csv(file_path)
for _, row in df.iterrows():
    data = {
        'age': float(row['age']),
        'study_hours': float(row['study_hours']),
        'attendance': float(row['attendance']),
        'sleep_hours': float(row['sleep_hours']),
    }
    marks = float(row['marks'])
    result = "Pass" if marks >= 75 else "Fail"
    save_prediction(data, marks, result)