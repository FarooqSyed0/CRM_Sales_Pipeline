import pandas as pd
import numpy as np

# Load and examine the CRM dataset
df = pd.read_excel("CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx", sheet_name="CRM_data")

# Basic dataset information
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())