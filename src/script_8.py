import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Load the CRM data
df = pd.read_excel('CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx', sheet_name='CRM_data')

# Display basic information about the dataset
print("=== CRM DATASET OVERVIEW ===")
print(f"Total records: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print("\nColumn names:")
for i, col in enumerate(df.columns, 1):
    print(f"{i:2d}. {col}")

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== FIRST FEW ROWS ===")
print(df.head())