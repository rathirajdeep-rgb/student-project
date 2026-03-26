import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('../data/student_data.csv')

#preview
print(df.head())

#Info
print(df.info)

#stats
print(df.describe())

# Missing values
print(df.isnull().sum())

# target
df['pass'] = (df['marks']>=74).astype(int)

# Distribution
print(df['pass'].value_counts())

# Visualaization
plt.scatter(df['study_hours'], df['marks'])
plt.xlabel('study hours')
plt.ylabel('marks')
plt.title('study hours vs marks')
plt.show()

#Correlation
print(df.corr())

#Features
X = df[['age', 'study_hours', 'attendance', 'sleep_hours']]
y = df['pass']