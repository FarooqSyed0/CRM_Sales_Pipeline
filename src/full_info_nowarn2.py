import pandas as pd
import numpy as np
from datetime import datetime

# Load and examine the CRM data
df = pd.read_excel("CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx", sheet_name="CRM_data")

# Display basic information about the dataset
print("Dataset Overview:")
print(f"Total records: {len(df)}")
print(f"Columns: {list(df.columns)}")
print("\nFirst few rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)