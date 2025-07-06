import pandas as pd
import numpy as np

# Load the CRM data
df = pd.read_excel('CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx', sheet_name='CRM_data')

# Display basic information about the dataset
print("Dataset Overview:")
print(f"Total records: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("\nColumn names:")
for i, col in enumerate(df.columns):
    print(f"{i+1}. {col}")

print(f"\nFirst few rows:")
df.head()