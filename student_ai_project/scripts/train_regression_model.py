import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('../data/student_data.csv')
df.head()
X = df[[ 'age', 'study_hours', 'attendance', 'sleep_hours' ]]
y = df['marks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])
pipeline.fit(X_train, y_train)

joblib.dump(pipeline, '../models/student_regression_model.pkl')

# prediction
y_pred = pipeline.predict(X_test).astype(int)
print(y_pred)
print(y_test.values)
print('Mean square error:', mean_squared_error(y_test, y_pred))

# Coefficients
model = pipeline.named_steps['model']
print('\nFeature impact on Marks')
for feature, coef in zip(X.columns,
model.coef_):
    print(feature, coef)
print('Intercept:', model.intercept_)