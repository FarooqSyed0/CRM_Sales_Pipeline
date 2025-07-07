import nbformat as nbf
import re, json
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

nb = new_notebook()

title = "# CRM & Sales Pipeline Analysis (Fixed)"
intro = ("This notebook analyzes the **CRM-and-Sales-Pipelines.csv** dataset and answers the following impact questions:\n"
         "1. **Pipeline Snapshot** – Current sales pipeline breakdown.\n"
         "2. **Sales Forecast** – Monthly forecast based on open opportunities.\n"
         "3. **Opportunity Closure Time** – Average time from lead acquisition to close (overall & by country).\n"
         "4. **Actual Win Rates** – Overall and by country.\n"
         "5. **Win Rates by Product and Region** – Heatmap of win ratios.\n")
nb.cells.append(new_markdown_cell(title))
nb.cells.append(new_markdown_cell(intro))

# 1. Load libraries & data
code1 = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

pd.set_option('display.max_columns', None)

# ---- Load dataset ----
df = pd.read_csv('CRM-and-Sales-Pipelines.csv')
print(f"Dataset shape: {df.shape}")
df.head()
"""
nb.cells.append(new_markdown_cell("## 1. Load Data"))
nb.cells.append(new_code_cell(code1))

# 2. Data cleaning
code2 = """
# ---- Data Cleaning ----
# Clean column names (alphanumeric + underscores, lower case)
df.columns = [re.sub(r'[^0-9a-zA-Z]+', '_', c).strip('_').lower() for c in df.columns]

# Convert date columns to datetime
date_cols = ['lead_acquisition_date', 'expected_close_date', 'actual_close_date']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Ensure numeric columns
df['deal_value'] = pd.to_numeric(df.get('deal_value'), errors='coerce')
df['probability'] = pd.to_numeric(df.get('probability'), errors='coerce')

# Drop duplicates
df.drop_duplicates(inplace=True)

print('Columns after cleaning:', df.columns.tolist())
print('\nMissing values (top 10):')
print(df.isna().sum().sort_values(ascending=False).head(10))
"""
nb.cells.append(new_markdown_cell("## 2. Data Cleaning"))
nb.cells.append(new_code_cell(code2))

# 3. Pipeline snapshot
code3 = """
# ---- Pipeline Snapshot ----
# Choose stage column fallback
if 'stage' in df.columns:
    df['pipeline_stage'] = df['stage'].fillna(df['status'])
else:
    df['pipeline_stage'] = df['status']

open_mask = df['actual_close_date'].isna()
pipeline_snapshot = df.loc[open_mask].groupby('pipeline_stage').size().sort_values(ascending=False)
print(pipeline_snapshot)

# Plot
plt.figure(figsize=(10,4))
ax = sns.barplot(x=pipeline_snapshot.values, y=pipeline_snapshot.index, palette='viridis')
plt.title('Open Opportunities by Pipeline Stage')
plt.xlabel('Count')
plt.ylabel('Stage')
for i, v in enumerate(pipeline_snapshot.values):
    ax.text(v+0.5, i, v, va='center')
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_markdown_cell("## 3. Pipeline Snapshot"))
nb.cells.append(new_code_cell(code3))

# 4. Sales forecast
code4 = """
# ---- Sales Forecast ----
open_ops = df[(df['actual_close_date'].isna()) & (df['expected_close_date'].notna())].copy()
open_ops['forecast_value'] = open_ops['deal_value'] * (open_ops['probability'] / 100)

open_ops['close_month'] = open_ops['expected_close_date'].dt.to_period('M')
forecast = open_ops.groupby('close_month')['forecast_value'].sum().reset_index()
forecast['close_month'] = forecast['close_month'].astype(str)
print(forecast.head())

plt.figure(figsize=(12,4))
sns.lineplot(data=forecast, x='close_month', y='forecast_value', marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Sales Forecast')
plt.ylabel('Forecasted Revenue')
plt.xlabel('Expected Close Month')
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_markdown_cell("## 4. Sales Forecast"))
nb.cells.append(new_code_cell(code4))

# 5. Opportunity closure time
code5 = """
# ---- Opportunity Closure Time ----
closed_ops = df[df['actual_close_date'].notna()].copy()
closed_ops['days_to_close'] = (closed_ops['actual_close_date'] - closed_ops['lead_acquisition_date']).dt.days

overall_avg = closed_ops['days_to_close'].mean()
print(f"Overall average days to close: {overall_avg:.1f}")

country_avg = closed_ops.groupby('country')['days_to_close'].mean().sort_values()
print(country_avg.head())

# Plot top 10 fastest
plt.figure(figsize=(10,5))
fastest = country_avg.head(10)
ax = sns.barplot(x=fastest.values, y=fastest.index, palette='mako')
plt.title('Average Days to Close (Fastest 10 Countries)')
plt.xlabel('Days')
plt.ylabel('Country')
for i, v in enumerate(fastest.values):
    ax.text(v+0.5, i, f"{v:.1f}", va='center')
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_markdown_cell("## 5. Opportunity Closure Time"))
nb.cells.append(new_code_cell(code5))

# 6. Win rates overall & by country
code6 = """
# ---- Win Rates ----
# Define win if status contains 'Customer' or stage == 'Won'
win_mask = (df['status'].str.contains('customer', case=False, na=False)) | \
           (df.get('stage', '').astype(str).str.contains('won', case=False, na=False))
df['is_won'] = win_mask

overall_win = df['is_won'].mean()
print(f"Overall win rate: {overall_win:.2%}")

country_win = df.groupby('country')['is_won'].mean().sort_values(ascending=False)
print(country_win.head())

# Plot top 10 countries
plt.figure(figsize=(10,5))
ax = sns.barplot(x=country_win.head(10).values, y=country_win.head(10).index, palette='crest')
plt.title('Win Rate by Country (Top 10)')
plt.xlabel('Win Rate')
plt.ylabel('Country')
for i, v in enumerate(country_win.head(10).values):
    ax.text(v+0.01, i, f"{v:.1%}", va='center')
plt.xlim(0,1)
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_markdown_cell("## 6. Win Rates"))
nb.cells.append(new_code_cell(code6))

# 7. Win rates by product & region
code7 = """
# ---- Win Rates by Product & Region ----
heat = df.pivot_table(index='product', columns='country', values='is_won', aggfunc='mean')
plt.figure(figsize=(12,6))
sns.heatmap(heat, cmap='YlGnBu', annot=True, fmt='.1%', cbar_kws={'label':'Win Rate'})
plt.title('Win Rate by Product & Country')
plt.xlabel('Country')
plt.ylabel('Product')
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_markdown_cell("## 7. Win Rates by Product & Region"))
nb.cells.append(new_code_cell(code7))

# Save notebook
with open('crm_sales_pipeline_analysis_fixed.ipynb', 'w') as f:
    nbf.write(nb, f)

print('Fixed notebook created: crm_sales_pipeline_analysis_fixed.ipynb')