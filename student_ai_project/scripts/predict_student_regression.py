import pandas as pd
import joblib

model = joblib.load('../models/student_regression_model.pkl')

new_student = pd.DataFrame([{
    'age': 24,
'study_hours': 2.5,
'attendance': 75,
'sleep_hours': 20
}])

predicted_marks = model.predict(new_student)
print('Predicted Marks:', predicted_marks)
Result = 'Pass' if predicted_marks >= 75 else 'Fail'
print(Result)
