import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('students.csv')

print("📋 Student Data:\n", df)
# Calculate average marks
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Determine pass/fail (pass if average >= 60)
df['Result'] = df['Average'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

