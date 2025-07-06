import pandas as pd
import numpy as np

# Read the CSV data
df = pd.read_csv("CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx")

# Display basic information about the dataset
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())