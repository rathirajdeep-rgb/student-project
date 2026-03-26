import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Validations
def validate_inputs(age, study, attendance, sleep):
    try:
        age = float(age)
        study = float(study)
        attendance = float(attendance)
        sleep = float(sleep)

        if age <=0 or age >=100:
            return 'Age must be between 0 and 100'
        if study <=0 or study >=24:
            return 'Study must be between 0 and 24'
        if attendance <=0 or attendance >=100:
            return 'Attendance must be between 0 and 100'
        if sleep <0 or sleep >=24:
            return 'Sleep must be between 0 and 24'
        if sleep + study > 24:
            return 'Sleep + study must be between 0 and 24'
        return None
    except:
        return 'Please enter a valid numeric value'



#Load trained model
model = joblib.load('../models/student_regression_model.pkl')

def predict_marks():
    age = entry_age.get()
    study = entry_study.get()
    attendance = entry_attendance.get()
    sleep = entry_sleep.get()

    #validate
    error = validate_inputs(age, study, attendance, sleep)
    if error:
        messagebox.showerror('Input Error', error)
        return

    # create data frame
    student = pd.DataFrame([{'age': float(age), 'study_hours': float(study),
                            'attendance': float(attendance),
                            'sleep_hours': float(sleep)}])
    # predict
    pass_symbol = '\u2705'
    fail_symbol = '\u274C'
    predicted_marks = model.predict(student)[0]
    result = f"PASS{pass_symbol}" if predicted_marks >= 75 else f"FAIL{fail_symbol}"

    # Show Result
    label_result.config(text= f"Marks: {predicted_marks:.2f}| Result: {result}",
    fg = 'green' if predicted_marks >= 75 else 'red')


#UI
root = tk.Tk()
root.geometry('400x300')
root.title('Student Marks Predictor')
root.resizable(False, False)


# Label & Input
tk.Label(root, text = 'Age').grid(row = 0, column = 0, padx = 10, pady = 5)
entry_age = tk.Entry(root)
entry_age.grid(row = 0, column =1)

tk.Label(root, text = 'Study Hours').grid(row = 1, column = 0, padx = 10, pady = 5)
entry_study = tk.Entry(root)
entry_study.grid(row = 1, column =1)

tk.Label(root, text = 'Attendance').grid(row = 2, column = 0, padx = 10, pady = 5)
entry_attendance = tk.Entry(root)
entry_attendance.grid(row = 2, column =1)

tk.Label(root, text = 'Sleep Hours').grid(row = 3, column = 0, padx = 10, pady = 5)
entry_sleep = tk.Entry(root)
entry_sleep.grid(row = 3, column =1)

# Button
tk.Button(root, text = 'Predict', command = predict_marks, bg = 'blue', fg = 'white').grid(row = 4, column = 0, columnspan= 2, pady = 15)

# Result label
label_result = tk.Label(root, text = "")
label_result.grid(row = 5, column = 0, columnspan= 2, pady = 5)


root.mainloop()



