import pandas as pd
import numpy as np
from datetime import datetime

# Load the CRM data
df = pd.read_excel('CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx')

# First, let's examine the structure of the data
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)