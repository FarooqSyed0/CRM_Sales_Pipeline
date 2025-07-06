import pandas as pd
import numpy as np

# Load the CRM data
df = pd.read_excel("CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx")

# Display basic information about the dataset
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())