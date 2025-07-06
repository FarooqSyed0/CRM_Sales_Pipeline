# CRM Sales Pipeline Analysis – Process \& Methodology

This document outlines the complete, step-by-step process for the CRM Sales Pipeline Analysis project, aligned with industry portfolio standards. Each step includes a concise summary and references to screenshots for clarity.

## Week 1: Data Acquisition \& Exploration

### 1.1 Prepare Environment and Ingest CSV

Installed required Python packages (pandas, numpy) and configured Jupyter Notebook. Loaded the provided CRM CSV file into a DataFrame; validated schema and types.

### 1.2 Design Data Model for Pipeline Analysis

Defined tables/dataframes for opportunities, accounts, activities, and products. Used appropriate types: STRING for text, DATE for timestamps, FLOAT for deal values, INTEGER for probabilities.

### 1.3 Initial Data Profiling

Computed record counts, null value summaries, and basic statistics. Identified 3,000 total records, 169 closed opportunities, and 558 custom solutions with missing some fields. Visualized distributions in notebooks.

### 1.4 Data Quality Assessment

Checked for duplicates, invalid dates (close dates before creation), and outlier deal values. Removed 12 duplicate rows and corrected 5 date inconsistencies using Python.

### 1.5 Define Core Business Questions

Framed five key questions: pipeline snapshot, sales forecast, closure time, win rates, and product-region win rate. Ensured alignment with stakeholder goals for revenue planning and process optimization.

## Week 2: Data Cleaning \& Validation

### 2.6 Clean and Standardize Data

Standardized stage names and status codes, filled missing probability values with stage-based estimates, and converted date strings to datetime objects.

### 2.7 Verify CSV Metrics Against Report

Recalculated total opportunities, stage distributions, and win counts to confirm 3,000 records and 171 wins. Updated percentages accordingly.

### 2.8 Calculate Weighted Forecast Data

Computed weighted deal values (deal_value × probability) and grouped by expected close month. Prepared monthly forecast table and summary metrics.

### 2.9 Compute Closure Time Metrics

Calculated days between creation and close for won opportunities; derived average and median by country. Stored results in a summary dataframe.

### 2.10 Derive Win Rate Metrics

Calculated global and per-country win rates, and per-product win rates. Assembled product-region matrix for strategic analysis.

## Week 3: Visualization \& Dashboard Design

### 3.11 Wireframe Dashboard Layout

Sketched an interactive dashboard layout: pipeline status chart, monthly forecast line chart, closure time bar chart, win rate map, and product-region heatmap.

### 3.12 Develop Visuals in Python

Created charts in Jupyter using matplotlib/seaborn:

- Bar chart for pipeline distribution
- Line chart for weighted forecast
- Horizontal bar chart for closure time by country
- Choropleth map for win rates
- Heatmap for product-region win rates


### 3.13 Assemble Interactive Tableau Dashboard

Exported cleaned data to CSV and connected to Tableau Public. Built KPI cards, filter panels, and integrated all visuals into a single dashboard.

## Week 4: Documentation, Publishing, and Portfolio Prep

### 4.14 Document Process in GitHub process.md

Authored this process.md file with detailed step summaries and embedded screenshot references stored under `/screenshots/week-*/`.

### 4.15 Summarize Key Findings \& Business Impact

drafted `business-impact-results.md` and `executive-summary.md` to highlight metrics and strategic recommendations.

### 4.16 Publish Dashboard \& Final Deliverables

Published interactive dashboard on Tableau Public and linked it in the project README. Prepared portfolio assets and technical documentation for stakeholder review.

