import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CRM data
df = pd.read_excel("CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx", sheet_name="CRM_data")

# Display basic information about the dataset
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())

# Check data types
print("\nData Types:")
print(df.dtypes)