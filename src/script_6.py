import pandas as pd
import numpy as np
from datetime import datetime

# Load the data
df = pd.read_excel('CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx', sheet_name='CRM_data')

# Display basic information about the dataset
print("Dataset Overview:")
print(f"Shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nFirst few rows:")
print(df.head())

print(f"\nData types:")
print(df.dtypes)

print(f"\nMissing values:")
print(df.isnull().sum())