import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('students.csv')

print("📋 Student Data:\n", df)
# Calculate average marks
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Determine pass/fail (pass if average >= 60)
df['Result'] = df['Average'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
# Show top students
top_students = df.sort_values(by='Average', ascending=False).head(3)
print("\n🏅 Top 3 Students:\n", top_students[['Name', 'Average']])

# Summary statistics
print("\n📈 Average Marks by Subject:")
print(df[['Math', 'Science', 'English']].mean())

# Pass/Fail count
print("\n✅📉 Result Count:")
print(df['Result'].value_counts())

