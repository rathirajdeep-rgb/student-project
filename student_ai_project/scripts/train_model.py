import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('../data/student_data.csv')

df['pass'] = (df['marks']>=75).astype(int)

X = df[['age', 'study_hours', 'attendance', 'sleep_hours']]
y = df['pass']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(random_state=42))
])

# train model
pipeline.fit(X_train, y_train)

joblib.dump(pipeline, '../models/student_model.pkl')

#predict
y_pred = pipeline.predict(X_test)
print(y_pred)
print(y_test.values)


#Evaluate
cm = confusion_matrix(y_test, y_pred)
print(cm)
cr = classification_report(y_test, y_pred)
print(cr)

model = pipeline.named_steps['model']
for feature, coef in zip(X.columns,
model.coef_[0]):
    print(feature, coef)

