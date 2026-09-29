import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

print("========== ORIGINAL DATASET ==========")
print(df.head())

# 2. Display dataset information
print("\n========== DATASET INFORMATION ==========")
print(df.info())

# 3. Check missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 4. Clean missing data
# Fill missing numerical values with their mean
numeric_columns = ["math score", "reading score", "writing score"]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# Fill missing categorical values with mode
categorical_columns = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# 5. Check missing values again
print("\n========== AFTER DATA CLEANING ==========")
print(df.isnull().sum())

# 6. Calculate average scores
print("\n========== AVERAGE SCORES ==========")

for column in numeric_columns:
    print(column, "Average:", round(df[column].mean(), 2))

# 7. Calculate maximum scores
print("\n========== MAXIMUM SCORES ==========")

for column in numeric_columns:
    print(column, "Maximum:", df[column].max())

# 8. Calculate minimum scores
print("\n========== MINIMUM SCORES ==========")

for column in numeric_columns:
    print(column, "Minimum:", df[column].min())

# 9. Create a summary table
summary = pd.DataFrame({
    "Subject": ["Math", "Reading", "Writing"],
    "Average": [
        df["math score"].mean(),
        df["reading score"].mean(),
        df["writing score"].mean()
    ],
    "Maximum": [
        df["math score"].max(),
        df["reading score"].max(),
        df["writing score"].max()
    ],
    "Minimum": [
        df["math score"].min(),
        df["reading score"].min(),
        df["writing score"].min()
    ]
})

print("\n========== FINAL RESULT ==========")
print(summary.round(2))