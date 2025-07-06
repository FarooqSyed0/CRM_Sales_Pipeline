import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Load the CRM data
df = pd.read_excel('CRM-and-Sales-Pipelines_C17_English-1-3-1.xlsx', sheet_name='CRM_data')

# Display basic information about the dataset
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
for i, col in enumerate(df.columns):
    print(f"{i+1}. {col}")

print("\nFirst few rows:")
df.head()