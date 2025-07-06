import pandas as pd
import numpy as np
from datetime import datetime

# Load the CRM data
df = pd.read_excel('CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx', sheet_name='CRM_data')

# Display basic information about the dataset
print("Dataset Overview:")
print(f"Total records: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("\nColumn names:")
print(df.columns.tolist())

# Display first few rows to understand the structure
print("\nFirst 5 rows:")
print(df.head())

# Check data types
print("\nData types:")
print(df.dtypes)