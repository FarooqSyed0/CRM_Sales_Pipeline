**Data Import for Analysis**

The cleaned CRM sales pipeline data is loaded for analysis.  
This DataFrame (`df_cleaned`) will be used for all subsequent exploration and insights.

*Rows: 3,000 | Columns: 17*


```python
# --- Clean CRM-and-Sales-Pipelines.csv ---
import pandas as pd
import numpy as np
import os

# Define file paths
input_path = 'CRM-and-Sales-Pipelines.csv'
output_path = 'CRM-and-Sales-Pipelines_cleaned.csv'

# Read the CSV file
# Note: encoding and delimiter can be adjusted if needed
print('Reading the original CSV file...')
df = pd.read_csv(input_path)

# 1. Remove duplicate rows
print('Removing duplicate rows...')
df = df.drop_duplicates()

# 2. Strip whitespace from headers and string columns
print('Stripping whitespace from headers and string columns...')
df.columns = df.columns.str.strip()
str_cols = df.select_dtypes(include='object').columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# 3. Standardize column names (remove spaces, fix typos)
print('Standardizing column names...')
col_rename = { 'Lattitude': 'Latitude', 'Deal Value, $': 'Deal_Value_USD', 'Probability, %': 'Probability_Pct' }
df = df.rename(columns=col_rename)
df.columns = df.columns.str.replace(' ', '_')

# 4. Handle missing values (example: fill with NaN, or drop if all NaN)
print('Handling missing values...')
df = df.replace({'': np.nan, 'NA': np.nan, 'N/A': np.nan})
# Optionally, drop rows where all values are NaN
df = df.dropna(how='all')

# 5. Ensure numeric columns are properly typed
print('Converting columns to appropriate dtypes...')
numeric_cols = ['Latitude', 'Longitude', 'Deal_Value_USD', 'Probability_Pct']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Save the cleaned file
print('Saving cleaned file as', output_path)
df.to_csv(output_path, index=False)

print('File has been cleaned.')
print(f'New file has been created: {output_path}')

```

    Reading the original CSV file...
    Removing duplicate rows...
    Stripping whitespace from headers and string columns...
    Standardizing column names...
    Handling missing values...
    Converting columns to appropriate dtypes...
    Saving cleaned file as CRM-and-Sales-Pipelines_cleaned.csv
    File has been cleaned.
    New file has been created: CRM-and-Sales-Pipelines_cleaned.csv


**Load Cleaned Data**

The cleaned CRM sales pipeline data is loaded for analysis and previewed.  
This DataFrame will be used for all further exploration.


```python
import pandas as pd

cleaned_path = 'CRM-and-Sales-Pipelines_cleaned.csv'
df_cleaned = pd.read_csv(cleaned_path)
print('Loaded cleaned data from', cleaned_path)
print('This DataFrame will be used for future analysis.')
print('Shape:', df_cleaned.shape)
df_cleaned.head()
```

    Loaded cleaned data from CRM-and-Sales-Pipelines_cleaned.csv
    This DataFrame will be used for future analysis.
    Shape: (3000, 17)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Organization</th>
      <th>Country</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Industry</th>
      <th>Organization_size</th>
      <th>Owner</th>
      <th>Lead_acquisition_date</th>
      <th>Product</th>
      <th>Status</th>
      <th>Status_sequence</th>
      <th>Stage</th>
      <th>Stage_sequence</th>
      <th>Deal_Value_USD</th>
      <th>Probability_Pct</th>
      <th>Expected_close_date</th>
      <th>Actual_close_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Thoughtblab</td>
      <td>Netherlands</td>
      <td>52.370216</td>
      <td>4.895168</td>
      <td>Banking and Finance</td>
      <td>Small (11-200)</td>
      <td>John Smith</td>
      <td>4/20/2024</td>
      <td>SAAS</td>
      <td>Churned Customer</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>833</td>
      <td>90</td>
      <td>8/7/2024</td>
      <td>6/27/2024</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jaxnation</td>
      <td>Spain</td>
      <td>40.416775</td>
      <td>-3.703790</td>
      <td>Energy &amp; Utilities</td>
      <td>Small (11-200)</td>
      <td>Emily Johnson</td>
      <td>5/28/2024</td>
      <td>SAAS</td>
      <td>Churned Customer</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1623</td>
      <td>30</td>
      <td>10/25/2024</td>
      <td>9/11/2024</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mybuzz</td>
      <td>Italy</td>
      <td>41.902782</td>
      <td>12.496366</td>
      <td>Education &amp; Science</td>
      <td>Small (11-200)</td>
      <td>Michael Brown</td>
      <td>3/17/2024</td>
      <td>SAAS</td>
      <td>Churned Customer</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1928</td>
      <td>20</td>
      <td>3/17/2025</td>
      <td>5/11/2024</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kare</td>
      <td>Germany</td>
      <td>52.520008</td>
      <td>13.404954</td>
      <td>Government Administration Healthcare</td>
      <td>Small (11-200)</td>
      <td>Michael Brown</td>
      <td>1/18/2024</td>
      <td>SAAS</td>
      <td>Churned Customer</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>303</td>
      <td>50</td>
      <td>8/7/2024</td>
      <td>5/6/2024</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Skaboo</td>
      <td>Germany</td>
      <td>52.520008</td>
      <td>13.404954</td>
      <td>Energy &amp; Utilities</td>
      <td>Small (11-200)</td>
      <td>Michael Brown</td>
      <td>4/6/2024</td>
      <td>SAAS</td>
      <td>Churned Customer</td>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1911</td>
      <td>30</td>
      <td>10/11/2024</td>
      <td>7/25/2024</td>
    </tr>
  </tbody>
</table>
</div>



**Sales Pipeline Overview**

A snapshot of our CRM data shows the number of opportunities at each sales stage. While many records lack a defined stage (2,133), the remainder are distributed as follows:

- Initial contact: 298
- Nurturing: 220
- Proposal sent: 140
- Won: 83
- Opened: 65
- Lost: 61

This highlights both the current pipeline distribution and a significant gap in stage data.


```python
# Pipeline Snapshot: Count of opportunities at each sales stage
stage_counts = df_cleaned['Stage'].value_counts(dropna=False).reset_index()
stage_counts.columns = ['Stage', 'Opportunity_Count']
print(stage_counts)
```

                 Stage  Opportunity_Count
    0              NaN               2133
    1  Initial contact                298
    2        Nurturing                220
    3    Proposal sent                140
    4              Won                 83
    5           Opened                 65
    6             Lost                 61


**Opportunities by Sales Stage**

This chart visualizes the distribution of opportunities across each sales stage, with a note on records missing stage information.


```python
# Exclude NaN from the bar chart
stage_counts_no_nan = stage_counts[stage_counts['Stage'].notna()]

# Plot the bar chart without NaN
plt.figure(figsize=(10, 6))
plt.bar(stage_counts_no_nan['Stage'].astype(str), stage_counts_no_nan['Opportunity_Count'], color='skyblue')
plt.xlabel('Sales Stage')
plt.ylabel('Number of Opportunities')
plt.title('Number of Opportunities at Each Sales Stage')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Indicate the number of NaN stages
nan_count = stage_counts.loc[stage_counts['Stage'].isna(), 'Opportunity_Count'].sum()
if nan_count > 0:
    print(f"Note: {nan_count} opportunities have a missing (NaN) sales stage.")
```


    
![png](sales_pipeline_analysis_files/sales_pipeline_analysis_7_0.png)
    


    Note: 2133 opportunities have a missing (NaN) sales stage.


**Monthly Sales Forecast**

This section forecasts expected sales revenue by month, using deal values weighted by their probability of closing. The results are presented in a formatted table and a bar chart, providing a clear view of projected sales trends over time.


```python
import matplotlib.pyplot as plt
from IPython.display import display

# Ensure date column is datetime
df_cleaned['Expected_close_date'] = pd.to_datetime(df_cleaned['Expected_close_date'], errors='coerce')

# Calculate expected value
df_cleaned['Expected_Value'] = df_cleaned['Deal_Value_USD'] * (df_cleaned['Probability_Pct'] / 100)

# Group by month
monthly_forecast = (
    df_cleaned
    .dropna(subset=['Expected_close_date'])
    .groupby(df_cleaned['Expected_close_date'].dt.to_period('M'))['Expected_Value']
    .sum()
    .sort_index()
)

# Create neat table
monthly_forecast_df = monthly_forecast.reset_index()
monthly_forecast_df['Expected_close_date'] = monthly_forecast_df['Expected_close_date'].astype(str)
monthly_forecast_df.columns = ['Month', 'Expected Sales ($)']

styled_table = (
    monthly_forecast_df
    .style
    .format({'Expected Sales ($)': '${:,.2f}'})
    .set_properties(**{'text-align': 'center'})
    .set_table_styles([{
        'selector': 'th',
        'props': [('text-align', 'center'), ('background-color', '#f2f2f2')]
    }])
)

display(styled_table)

# Plot the graph
plt.figure(figsize=(10,6))
monthly_forecast.plot(kind='bar', color='skyblue')
plt.title('Sales Forecast by Month')
plt.xlabel('Month')
plt.ylabel('Expected Sales ($)')
plt.tight_layout()
plt.show()
```


<style type="text/css">
#T_88765 th {
  text-align: center;
  background-color: #f2f2f2;
}
#T_88765_row0_col0, #T_88765_row0_col1, #T_88765_row1_col0, #T_88765_row1_col1, #T_88765_row2_col0, #T_88765_row2_col1, #T_88765_row3_col0, #T_88765_row3_col1, #T_88765_row4_col0, #T_88765_row4_col1, #T_88765_row5_col0, #T_88765_row5_col1, #T_88765_row6_col0, #T_88765_row6_col1, #T_88765_row7_col0, #T_88765_row7_col1, #T_88765_row8_col0, #T_88765_row8_col1, #T_88765_row9_col0, #T_88765_row9_col1, #T_88765_row10_col0, #T_88765_row10_col1, #T_88765_row11_col0, #T_88765_row11_col1, #T_88765_row12_col0, #T_88765_row12_col1, #T_88765_row13_col0, #T_88765_row13_col1, #T_88765_row14_col0, #T_88765_row14_col1, #T_88765_row15_col0, #T_88765_row15_col1, #T_88765_row16_col0, #T_88765_row16_col1 {
  text-align: center;
}
</style>
<table id="T_88765">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_88765_level0_col0" class="col_heading level0 col0" >Month</th>
      <th id="T_88765_level0_col1" class="col_heading level0 col1" >Expected Sales ($)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_88765_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_88765_row0_col0" class="data row0 col0" >2024-01</td>
      <td id="T_88765_row0_col1" class="data row0 col1" >$2,638.50</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_88765_row1_col0" class="data row1 col0" >2024-02</td>
      <td id="T_88765_row1_col1" class="data row1 col1" >$37,000.40</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_88765_row2_col0" class="data row2 col0" >2024-03</td>
      <td id="T_88765_row2_col1" class="data row2 col1" >$123,439.90</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_88765_row3_col0" class="data row3 col0" >2024-04</td>
      <td id="T_88765_row3_col1" class="data row3 col1" >$177,385.80</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_88765_row4_col0" class="data row4 col0" >2024-05</td>
      <td id="T_88765_row4_col1" class="data row4 col1" >$265,802.70</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_88765_row5_col0" class="data row5 col0" >2024-06</td>
      <td id="T_88765_row5_col1" class="data row5 col1" >$328,054.50</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row6" class="row_heading level0 row6" >6</th>
      <td id="T_88765_row6_col0" class="data row6 col0" >2024-07</td>
      <td id="T_88765_row6_col1" class="data row6 col1" >$353,634.90</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row7" class="row_heading level0 row7" >7</th>
      <td id="T_88765_row7_col0" class="data row7 col0" >2024-08</td>
      <td id="T_88765_row7_col1" class="data row7 col1" >$287,667.10</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row8" class="row_heading level0 row8" >8</th>
      <td id="T_88765_row8_col0" class="data row8 col0" >2024-09</td>
      <td id="T_88765_row8_col1" class="data row8 col1" >$285,378.00</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row9" class="row_heading level0 row9" >9</th>
      <td id="T_88765_row9_col0" class="data row9 col0" >2024-10</td>
      <td id="T_88765_row9_col1" class="data row9 col1" >$320,319.00</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row10" class="row_heading level0 row10" >10</th>
      <td id="T_88765_row10_col0" class="data row10 col0" >2024-11</td>
      <td id="T_88765_row10_col1" class="data row10 col1" >$334,254.90</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row11" class="row_heading level0 row11" >11</th>
      <td id="T_88765_row11_col0" class="data row11 col0" >2024-12</td>
      <td id="T_88765_row11_col1" class="data row11 col1" >$387,509.50</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row12" class="row_heading level0 row12" >12</th>
      <td id="T_88765_row12_col0" class="data row12 col0" >2025-01</td>
      <td id="T_88765_row12_col1" class="data row12 col1" >$283,998.00</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row13" class="row_heading level0 row13" >13</th>
      <td id="T_88765_row13_col0" class="data row13 col0" >2025-02</td>
      <td id="T_88765_row13_col1" class="data row13 col1" >$226,325.00</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row14" class="row_heading level0 row14" >14</th>
      <td id="T_88765_row14_col0" class="data row14 col0" >2025-03</td>
      <td id="T_88765_row14_col1" class="data row14 col1" >$166,087.30</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row15" class="row_heading level0 row15" >15</th>
      <td id="T_88765_row15_col0" class="data row15 col0" >2025-04</td>
      <td id="T_88765_row15_col1" class="data row15 col1" >$92,766.10</td>
    </tr>
    <tr>
      <th id="T_88765_level0_row16" class="row_heading level0 row16" >16</th>
      <td id="T_88765_row16_col0" class="data row16 col0" >2025-05</td>
      <td id="T_88765_row16_col1" class="data row16 col1" >$33,379.90</td>
    </tr>
  </tbody>
</table>




    
![png](sales_pipeline_analysis_files/sales_pipeline_analysis_9_1.png)
    


**Sales Cycle Duration by Country**

This section analyzes the average time taken to close sales opportunities across different countries. The summary table is sorted from highest to lowest by opportunity count, showing the number of opportunities, as well as the mean and median closure times (in days) for each country. This helps identify regions with the most sales activity and compare sales cycle efficiency.


```python
import pandas as pd
import matplotlib.pyplot as plt

# Ensure date columns are datetime
df_cleaned['Lead_acquisition_date'] = pd.to_datetime(df_cleaned['Lead_acquisition_date'], errors='coerce')
df_cleaned['Actual_close_date'] = pd.to_datetime(df_cleaned['Actual_close_date'], errors='coerce')

# Calculate closure time in days
df_cleaned['Closure_Time_Days'] = (df_cleaned['Actual_close_date'] - df_cleaned['Lead_acquisition_date']).dt.days

# Drop rows with missing closure time
closure_df = df_cleaned.dropna(subset=['Closure_Time_Days', 'Country'])

# Show summary table by country
closure_summary = (
    closure_df.groupby('Country')['Closure_Time_Days']
    .agg(['count', 'mean', 'median'])
    .reset_index()
)
closure_summary.columns = ['Country', 'Opportunity Count', 'Mean Closure Time (days)', 'Median Closure Time (days)']

# Sort by Opportunity Count, descending
closure_summary = closure_summary.sort_values('Opportunity Count', ascending=False)

# Style and display the table without index
styled_closure = (
    closure_summary
    .style
    .format({'Mean Closure Time (days)': '{:.1f}', 'Median Closure Time (days)': '{:.1f}'})
    .set_properties(**{'text-align': 'center'})
    .set_table_styles([{
        'selector': 'th',
        'props': [('text-align', 'center'), ('background-color', '#f2f2f2')]
    }])
    .hide(axis='index')  # Hide the index
)
from IPython.display import display
display(styled_closure)
```


<style type="text/css">
#T_2d0ec th {
  text-align: center;
  background-color: #f2f2f2;
}
#T_2d0ec_row0_col0, #T_2d0ec_row0_col1, #T_2d0ec_row0_col2, #T_2d0ec_row0_col3, #T_2d0ec_row1_col0, #T_2d0ec_row1_col1, #T_2d0ec_row1_col2, #T_2d0ec_row1_col3, #T_2d0ec_row2_col0, #T_2d0ec_row2_col1, #T_2d0ec_row2_col2, #T_2d0ec_row2_col3, #T_2d0ec_row3_col0, #T_2d0ec_row3_col1, #T_2d0ec_row3_col2, #T_2d0ec_row3_col3, #T_2d0ec_row4_col0, #T_2d0ec_row4_col1, #T_2d0ec_row4_col2, #T_2d0ec_row4_col3, #T_2d0ec_row5_col0, #T_2d0ec_row5_col1, #T_2d0ec_row5_col2, #T_2d0ec_row5_col3, #T_2d0ec_row6_col0, #T_2d0ec_row6_col1, #T_2d0ec_row6_col2, #T_2d0ec_row6_col3, #T_2d0ec_row7_col0, #T_2d0ec_row7_col1, #T_2d0ec_row7_col2, #T_2d0ec_row7_col3, #T_2d0ec_row8_col0, #T_2d0ec_row8_col1, #T_2d0ec_row8_col2, #T_2d0ec_row8_col3 {
  text-align: center;
}
</style>
<table id="T_2d0ec">
  <thead>
    <tr>
      <th id="T_2d0ec_level0_col0" class="col_heading level0 col0" >Country</th>
      <th id="T_2d0ec_level0_col1" class="col_heading level0 col1" >Opportunity Count</th>
      <th id="T_2d0ec_level0_col2" class="col_heading level0 col2" >Mean Closure Time (days)</th>
      <th id="T_2d0ec_level0_col3" class="col_heading level0 col3" >Median Closure Time (days)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_2d0ec_row0_col0" class="data row0 col0" >Italy</td>
      <td id="T_2d0ec_row0_col1" class="data row0 col1" >80</td>
      <td id="T_2d0ec_row0_col2" class="data row0 col2" >65.5</td>
      <td id="T_2d0ec_row0_col3" class="data row0 col3" >64.0</td>
    </tr>
    <tr>
      <td id="T_2d0ec_row1_col0" class="data row1 col0" >Portugal</td>
      <td id="T_2d0ec_row1_col1" class="data row1 col1" >51</td>
      <td id="T_2d0ec_row1_col2" class="data row1 col2" >65.8</td>
      <td id="T_2d0ec_row1_col3" class="data row1 col3" >69.0</td>
    </tr>
    <tr>
      <td id="T_2d0ec_row2_col0" class="data row2 col0" >France</td>
      <td id="T_2d0ec_row2_col1" class="data row2 col1" >42</td>
      <td id="T_2d0ec_row2_col2" class="data row2 col2" >64.0</td>
      <td id="T_2d0ec_row2_col3" class="data row2 col3" >60.5</td>
    </tr>
    <tr>
      <td id="T_2d0ec_row3_col0" class="data row3 col0" >Germany</td>
      <td id="T_2d0ec_row3_col1" class="data row3 col1" >40</td>
      <td id="T_2d0ec_row3_col2" class="data row3 col2" >56.2</td>
      <td id="T_2d0ec_row3_col3" class="data row3 col3" >54.5</td>
    </tr>
    <tr>
      <td id="T_2d0ec_row4_col0" class="data row4 col0" >Switzerland</td>
      <td id="T_2d0ec_row4_col1" class="data row4 col1" >38</td>
      <td id="T_2d0ec_row4_col2" class="data row4 col2" >68.2</td>
      <td id="T_2d0ec_row4_col3" class="data row4 col3" >78.5</td>
    </tr>
    <tr>
      <td id="T_2d0ec_row5_col0" class="data row5 col0" >Netherlands</td>
      <td id="T_2d0ec_row5_col1" class="data row5 col1" >27</td>
      <td id="T_2d0ec_row5_col2" class="data row5 col2" >58.7</td>
      <td id="T_2d0ec_row5_col3" class="data row5 col3" >51.0</td>
    </tr>
    <tr>
      <td id="T_2d0ec_row6_col0" class="data row6 col0" >Belgium</td>
      <td id="T_2d0ec_row6_col1" class="data row6 col1" >25</td>
      <td id="T_2d0ec_row6_col2" class="data row6 col2" >58.6</td>
      <td id="T_2d0ec_row6_col3" class="data row6 col3" >61.0</td>
    </tr>
    <tr>
      <td id="T_2d0ec_row7_col0" class="data row7 col0" >Spain</td>
      <td id="T_2d0ec_row7_col1" class="data row7 col1" >25</td>
      <td id="T_2d0ec_row7_col2" class="data row7 col2" >59.6</td>
      <td id="T_2d0ec_row7_col3" class="data row7 col3" >58.0</td>
    </tr>
    <tr>
      <td id="T_2d0ec_row8_col0" class="data row8 col0" >Austria</td>
      <td id="T_2d0ec_row8_col1" class="data row8 col1" >20</td>
      <td id="T_2d0ec_row8_col2" class="data row8 col2" >66.0</td>
      <td id="T_2d0ec_row8_col3" class="data row8 col3" >70.5</td>
    </tr>
  </tbody>
</table>



**Win Rate by Country**

This section calculates and displays the sales win rate for each country. The summary table shows the total number of opportunities, number of wins, and the win rate (as a percentage), sorted from highest to lowest win rate. This provides insight into which regions have the most successful sales performance.


```python
import pandas as pd
from IPython.display import display

# Filter for rows where Status is not null and Country is not null
df_valid = df_cleaned.dropna(subset=['Status', 'Country'])

# Calculate win rate: Status == 'Customer'
win_summary = (
    df_valid.groupby('Country')
    .agg(
        Total_Opportunities=('Status', 'count'),
        Wins=('Status', lambda x: (x == 'Customer').sum())
    )
    .assign(Win_Rate=lambda x: x['Wins'] / x['Total_Opportunities'])
    .sort_values('Win_Rate', ascending=False)
    .reset_index()
)

# Style the table
styled_win_table = (
    win_summary
    .style
    .format({'Win_Rate': '{:.2%}'})
    .set_properties(**{'text-align': 'center'})
    .set_table_styles([{
        'selector': 'th',
        'props': [('text-align', 'center'), ('background-color', '#f2f2f2')]
    }])
)

display(styled_win_table)
```


<style type="text/css">
#T_4792c th {
  text-align: center;
  background-color: #f2f2f2;
}
#T_4792c_row0_col0, #T_4792c_row0_col1, #T_4792c_row0_col2, #T_4792c_row0_col3, #T_4792c_row1_col0, #T_4792c_row1_col1, #T_4792c_row1_col2, #T_4792c_row1_col3, #T_4792c_row2_col0, #T_4792c_row2_col1, #T_4792c_row2_col2, #T_4792c_row2_col3, #T_4792c_row3_col0, #T_4792c_row3_col1, #T_4792c_row3_col2, #T_4792c_row3_col3, #T_4792c_row4_col0, #T_4792c_row4_col1, #T_4792c_row4_col2, #T_4792c_row4_col3, #T_4792c_row5_col0, #T_4792c_row5_col1, #T_4792c_row5_col2, #T_4792c_row5_col3, #T_4792c_row6_col0, #T_4792c_row6_col1, #T_4792c_row6_col2, #T_4792c_row6_col3, #T_4792c_row7_col0, #T_4792c_row7_col1, #T_4792c_row7_col2, #T_4792c_row7_col3, #T_4792c_row8_col0, #T_4792c_row8_col1, #T_4792c_row8_col2, #T_4792c_row8_col3 {
  text-align: center;
}
</style>
<table id="T_4792c">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_4792c_level0_col0" class="col_heading level0 col0" >Country</th>
      <th id="T_4792c_level0_col1" class="col_heading level0 col1" >Total_Opportunities</th>
      <th id="T_4792c_level0_col2" class="col_heading level0 col2" >Wins</th>
      <th id="T_4792c_level0_col3" class="col_heading level0 col3" >Win_Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_4792c_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_4792c_row0_col0" class="data row0 col0" >Netherlands</td>
      <td id="T_4792c_row0_col1" class="data row0 col1" >180</td>
      <td id="T_4792c_row0_col2" class="data row0 col2" >14</td>
      <td id="T_4792c_row0_col3" class="data row0 col3" >7.78%</td>
    </tr>
    <tr>
      <th id="T_4792c_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_4792c_row1_col0" class="data row1 col0" >Belgium</td>
      <td id="T_4792c_row1_col1" class="data row1 col1" >207</td>
      <td id="T_4792c_row1_col2" class="data row1 col2" >16</td>
      <td id="T_4792c_row1_col3" class="data row1 col3" >7.73%</td>
    </tr>
    <tr>
      <th id="T_4792c_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_4792c_row2_col0" class="data row2 col0" >Portugal</td>
      <td id="T_4792c_row2_col1" class="data row2 col1" >371</td>
      <td id="T_4792c_row2_col2" class="data row2 col2" >28</td>
      <td id="T_4792c_row2_col3" class="data row2 col3" >7.55%</td>
    </tr>
    <tr>
      <th id="T_4792c_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_4792c_row3_col0" class="data row3 col0" >Italy</td>
      <td id="T_4792c_row3_col1" class="data row3 col1" >620</td>
      <td id="T_4792c_row3_col2" class="data row3 col2" >37</td>
      <td id="T_4792c_row3_col3" class="data row3 col3" >5.97%</td>
    </tr>
    <tr>
      <th id="T_4792c_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_4792c_row4_col0" class="data row4 col0" >France</td>
      <td id="T_4792c_row4_col1" class="data row4 col1" >422</td>
      <td id="T_4792c_row4_col2" class="data row4 col2" >24</td>
      <td id="T_4792c_row4_col3" class="data row4 col3" >5.69%</td>
    </tr>
    <tr>
      <th id="T_4792c_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_4792c_row5_col0" class="data row5 col0" >Austria</td>
      <td id="T_4792c_row5_col1" class="data row5 col1" >199</td>
      <td id="T_4792c_row5_col2" class="data row5 col2" >11</td>
      <td id="T_4792c_row5_col3" class="data row5 col3" >5.53%</td>
    </tr>
    <tr>
      <th id="T_4792c_level0_row6" class="row_heading level0 row6" >6</th>
      <td id="T_4792c_row6_col0" class="data row6 col0" >Spain</td>
      <td id="T_4792c_row6_col1" class="data row6 col1" >189</td>
      <td id="T_4792c_row6_col2" class="data row6 col2" >9</td>
      <td id="T_4792c_row6_col3" class="data row6 col3" >4.76%</td>
    </tr>
    <tr>
      <th id="T_4792c_level0_row7" class="row_heading level0 row7" >7</th>
      <td id="T_4792c_row7_col0" class="data row7 col0" >Germany</td>
      <td id="T_4792c_row7_col1" class="data row7 col1" >420</td>
      <td id="T_4792c_row7_col2" class="data row7 col2" >17</td>
      <td id="T_4792c_row7_col3" class="data row7 col3" >4.05%</td>
    </tr>
    <tr>
      <th id="T_4792c_level0_row8" class="row_heading level0 row8" >8</th>
      <td id="T_4792c_row8_col0" class="data row8 col0" >Switzerland</td>
      <td id="T_4792c_row8_col1" class="data row8 col1" >392</td>
      <td id="T_4792c_row8_col2" class="data row8 col2" >15</td>
      <td id="T_4792c_row8_col3" class="data row8 col3" >3.83%</td>
    </tr>
  </tbody>
</table>



**Top Product-Region Win Rates**

This section highlights the top 10 product and country combinations with the highest sales win rates. The results are shown in a formatted table and a horizontal bar chart, providing a clear view of which product-region pairs are most successful in converting opportunities into wins.


```python
from IPython.display import display

# Replace 'Product' with the actual product column name if different
df_valid = df_cleaned.dropna(subset=['Status', 'Country', 'Product'])

win_by_product_region = (
    df_valid.groupby(['Product', 'Country'])
    .agg(
        Total_Opportunities=('Status', 'count'),
        Wins=('Status', lambda x: (x == 'Customer').sum())
    )
    .assign(Win_Rate=lambda x: x['Wins'] / x['Total_Opportunities'])
    .sort_values('Win_Rate', ascending=False)
    .reset_index()
)

# Remove underscores for display
win_by_product_region.columns = [col.replace('_', ' ') for col in win_by_product_region.columns]

# Move 'Country' column to the left
cols = win_by_product_region.columns.tolist()
cols.insert(0, cols.pop(cols.index('Country')))
win_by_product_region = win_by_product_region[cols]

# Show only the top 10 rows
win_by_product_region_top10 = win_by_product_region.head(10)

styled_win_table = (
    win_by_product_region_top10
    .style
    .format({'Win Rate': '{:.2%}'})
    .set_properties(**{'text-align': 'center'})
    .set_table_styles([{
        'selector': 'th',
        'props': [('text-align', 'center'), ('background-color', '#f2f2f2')]
    }])
)

display(styled_win_table.hide(axis='index'))  # Hide the index numbers


import matplotlib.pyplot as plt

# Calculate the maximum win rate in the top 10
max_win_rate = win_by_product_region_top10['Win Rate'].max()
xmax = max_win_rate * 1.05  # Add 5% margin for aesthetics

plt.figure(figsize=(14, 8))
plt.barh(
    win_by_product_region_top10.apply(lambda x: f"{x['Product']} ({x['Country']})", axis=1),
    win_by_product_region_top10['Win Rate'],
    color='skyblue'
)
plt.xlabel('Win Rate')
plt.ylabel('Product (Country)')
plt.title('Top 10 Product-Region Win Rates')
plt.xlim(0, xmax)
plt.tight_layout()
plt.gca().invert_yaxis()  # Highest win rate at the top
plt.show()
```


<style type="text/css">
#T_f68ac th {
  text-align: center;
  background-color: #f2f2f2;
}
#T_f68ac_row0_col0, #T_f68ac_row0_col1, #T_f68ac_row0_col2, #T_f68ac_row0_col3, #T_f68ac_row0_col4, #T_f68ac_row1_col0, #T_f68ac_row1_col1, #T_f68ac_row1_col2, #T_f68ac_row1_col3, #T_f68ac_row1_col4, #T_f68ac_row2_col0, #T_f68ac_row2_col1, #T_f68ac_row2_col2, #T_f68ac_row2_col3, #T_f68ac_row2_col4, #T_f68ac_row3_col0, #T_f68ac_row3_col1, #T_f68ac_row3_col2, #T_f68ac_row3_col3, #T_f68ac_row3_col4, #T_f68ac_row4_col0, #T_f68ac_row4_col1, #T_f68ac_row4_col2, #T_f68ac_row4_col3, #T_f68ac_row4_col4, #T_f68ac_row5_col0, #T_f68ac_row5_col1, #T_f68ac_row5_col2, #T_f68ac_row5_col3, #T_f68ac_row5_col4, #T_f68ac_row6_col0, #T_f68ac_row6_col1, #T_f68ac_row6_col2, #T_f68ac_row6_col3, #T_f68ac_row6_col4, #T_f68ac_row7_col0, #T_f68ac_row7_col1, #T_f68ac_row7_col2, #T_f68ac_row7_col3, #T_f68ac_row7_col4, #T_f68ac_row8_col0, #T_f68ac_row8_col1, #T_f68ac_row8_col2, #T_f68ac_row8_col3, #T_f68ac_row8_col4, #T_f68ac_row9_col0, #T_f68ac_row9_col1, #T_f68ac_row9_col2, #T_f68ac_row9_col3, #T_f68ac_row9_col4 {
  text-align: center;
}
</style>
<table id="T_f68ac">
  <thead>
    <tr>
      <th id="T_f68ac_level0_col0" class="col_heading level0 col0" >Country</th>
      <th id="T_f68ac_level0_col1" class="col_heading level0 col1" >Product</th>
      <th id="T_f68ac_level0_col2" class="col_heading level0 col2" >Total Opportunities</th>
      <th id="T_f68ac_level0_col3" class="col_heading level0 col3" >Wins</th>
      <th id="T_f68ac_level0_col4" class="col_heading level0 col4" >Win Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_f68ac_row0_col0" class="data row0 col0" >Belgium</td>
      <td id="T_f68ac_row0_col1" class="data row0 col1" >Services</td>
      <td id="T_f68ac_row0_col2" class="data row0 col2" >79</td>
      <td id="T_f68ac_row0_col3" class="data row0 col3" >8</td>
      <td id="T_f68ac_row0_col4" class="data row0 col4" >10.13%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row1_col0" class="data row1 col0" >Netherlands</td>
      <td id="T_f68ac_row1_col1" class="data row1 col1" >Services</td>
      <td id="T_f68ac_row1_col2" class="data row1 col2" >70</td>
      <td id="T_f68ac_row1_col3" class="data row1 col3" >7</td>
      <td id="T_f68ac_row1_col4" class="data row1 col4" >10.00%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row2_col0" class="data row2 col0" >Portugal</td>
      <td id="T_f68ac_row2_col1" class="data row2 col1" >SAAS</td>
      <td id="T_f68ac_row2_col2" class="data row2 col2" >158</td>
      <td id="T_f68ac_row2_col3" class="data row2 col3" >15</td>
      <td id="T_f68ac_row2_col4" class="data row2 col4" >9.49%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row3_col0" class="data row3 col0" >Belgium</td>
      <td id="T_f68ac_row3_col1" class="data row3 col1" >SAAS</td>
      <td id="T_f68ac_row3_col2" class="data row3 col2" >89</td>
      <td id="T_f68ac_row3_col3" class="data row3 col3" >7</td>
      <td id="T_f68ac_row3_col4" class="data row3 col4" >7.87%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row4_col0" class="data row4 col0" >Netherlands</td>
      <td id="T_f68ac_row4_col1" class="data row4 col1" >Custom solution</td>
      <td id="T_f68ac_row4_col2" class="data row4 col2" >41</td>
      <td id="T_f68ac_row4_col3" class="data row4 col3" >3</td>
      <td id="T_f68ac_row4_col4" class="data row4 col4" >7.32%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row5_col0" class="data row5 col0" >France</td>
      <td id="T_f68ac_row5_col1" class="data row5 col1" >Custom solution</td>
      <td id="T_f68ac_row5_col2" class="data row5 col2" >72</td>
      <td id="T_f68ac_row5_col3" class="data row5 col3" >5</td>
      <td id="T_f68ac_row5_col4" class="data row5 col4" >6.94%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row6_col0" class="data row6 col0" >Italy</td>
      <td id="T_f68ac_row6_col1" class="data row6 col1" >SAAS</td>
      <td id="T_f68ac_row6_col2" class="data row6 col2" >281</td>
      <td id="T_f68ac_row6_col3" class="data row6 col3" >19</td>
      <td id="T_f68ac_row6_col4" class="data row6 col4" >6.76%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row7_col0" class="data row7 col0" >Austria</td>
      <td id="T_f68ac_row7_col1" class="data row7 col1" >Services</td>
      <td id="T_f68ac_row7_col2" class="data row7 col2" >74</td>
      <td id="T_f68ac_row7_col3" class="data row7 col3" >5</td>
      <td id="T_f68ac_row7_col4" class="data row7 col4" >6.76%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row8_col0" class="data row8 col0" >Germany</td>
      <td id="T_f68ac_row8_col1" class="data row8 col1" >Custom solution</td>
      <td id="T_f68ac_row8_col2" class="data row8 col2" >78</td>
      <td id="T_f68ac_row8_col3" class="data row8 col3" >5</td>
      <td id="T_f68ac_row8_col4" class="data row8 col4" >6.41%</td>
    </tr>
    <tr>
      <td id="T_f68ac_row9_col0" class="data row9 col0" >Portugal</td>
      <td id="T_f68ac_row9_col1" class="data row9 col1" >Custom solution</td>
      <td id="T_f68ac_row9_col2" class="data row9 col2" >64</td>
      <td id="T_f68ac_row9_col3" class="data row9 col3" >4</td>
      <td id="T_f68ac_row9_col4" class="data row9 col4" >6.25%</td>
    </tr>
  </tbody>
</table>




    
![png](sales_pipeline_analysis_files/sales_pipeline_analysis_15_1.png)
    

