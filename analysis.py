"""
Mindrift Data Analysis Portfolio Project
Educational Student Performance Analysis

The dataset in this project is synthetic and created for demonstration.
It contains no real student personal information.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_dataset.csv")

subjects = ["reading_score", "math_score", "english_score", "science_score"]
df["overall_score"] = df[subjects].mean(axis=1)

print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())

print("\nDescriptive statistics:")
print(df[["attendance_pct", "weekly_study_hours"] + subjects + ["overall_score"]].describe())

print("\nAverage score by learning area:")
print(df[subjects].mean().sort_values(ascending=False))

print("\nAverage score by grade:")
print(df.groupby("grade")["overall_score"].mean().sort_values(ascending=False))

print("\nCorrelation with overall score:")
print("Attendance:", df["attendance_pct"].corr(df["overall_score"]))
print("Study hours:", df["weekly_study_hours"].corr(df["overall_score"]))

# Example visualization
df.groupby("grade")["overall_score"].mean().plot(kind="bar")
plt.title("Average Overall Score by Grade")
plt.ylabel("Average score (%)")
plt.tight_layout()
plt.show()
