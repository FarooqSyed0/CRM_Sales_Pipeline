<h1 align="center">CRM Sales Pipeline Analysis</h1>

**Business Problem:** Analyzed 2,000+ CRM opportunities to identify sales performance patterns, optimize pipeline management, and provide data-driven insights for revenue growth and strategic decision-making.

<h2 align="center">📈 Business Impact Questions & Results</h2>

| Question | Key Result |
|--|--|
| 📊 **Pipeline Optimization** What does my current sales pipeline look like and how can it be optimized? | 🏆 **867 active opportunities** identified across the sales pipeline<br>**28.9%** of all records are in "Opportunity" stage—providing clear visibility into conversion potential and resource allocation needs<br>Top markets: Italy (173), Germany (124) |
| 📈 **Revenue Forecasting** What is the sales forecast accuracy for strategic planning? | 💰 **$2.3M total opportunity value** in current pipeline<br>Progressive quarterly growth pattern from Q1 to Q4 based on expected close dates<br>Transparent gross pipeline approach enables data-driven revenue planning without probability weighting |
| 🎯 **Performance Benchmarking** What are the actual win rate benchmarks for competitive positioning? | 📊 **9.6% overall win rate** with significant performance variance between markets<br>**Belgium** leads at 16.9%, followed by Germany (10.5%) and Italy (10.4%)<br>**83 total wins** across all opportunities—enabling targeted improvement strategies |
| 🧩 **Product-Market Optimization** Which product-market combinations offer the highest revenue potential? | 🚀 **SAAS: $961K** identified as top revenue opportunity<br>**Services: $847K** and **Custom solution: $488K** complete the product portfolio<br>Three active products represent concentrated opportunity focus for sales prioritization |


<h2 align="center">🛠️ Technologies Used</h2>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![DBeaver](https://img.shields.io/badge/DBeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)
![Mermaid JS](https://img.shields.io/badge/Mermaid-FF3670?style=for-the-badge&logo=mermaid&logoColor=white)
![Google Workspace](https://img.shields.io/badge/Google%20Workspace-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Anaconda Cloud](https://img.shields.io/badge/Anaconda%20Cloud-44A833?style=for-the-badge&logo=anaconda&logoColor=white)
![Microsoft Excel](https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
![Apple Numbers](https://img.shields.io/badge/NUMBERS-27C93F?style=for-the-badge&logo=apple&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-444876?style=for-the-badge&logo=seaborn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
[![Matplotlib](https://img.shields.io/badge/MATPLOTLIB-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
<img src="https://img.shields.io/badge/PLOTLY-3F4F75?style=flat&logo=plotly&logoColor=white" width="98" height="80" />



<h2 align="center">🚀 Live Dashboard</h2>

<p align="center">
  <a href="https://public.tableau.com/app/profile/farooq.syed6811/viz/CRM-and-Sales-Pipelines/CRMSalesPipelines?publish=yes">
    View the Interactive Tableau Dashboard
  </a>
</p>

<p align="center">
  <img src="screenshots/dashboard.png" width="1200" height="800">
</p>

<h2 align="center">🗺️ Project Workflow</h2>


<img src="./screenshots/workflow.png" alt="Workflow Diagram" width="1200" height="800">


<h2 align="center">📖 Technical Documentation</h2>

| <img src="./screenshots/sql_business_question.png" alt="SQL Business Question" width="500"><br><b>SQL Business Question</b> | <img src="./screenshots/win_rates.png" alt="Win Rates" width="500"><br><b>Win Rates</b> |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <img src="./screenshots/forecast.png" alt="Forecast" width="500"><br><div align="center"><b>Expected Sales Forecast</b></div>               | <img src="./screenshots/no_opps.png" alt="Number of Opportunities" width="500"><br><div align="center"><b>Number of Opportunities</b></div> |






## Supporting Resources

- **Business Impact Analysis** `src/impact_questions.ipynb`  
  Jupyter notebook analyzing pipeline optimization, forecasting, benchmarking, and product-market insights from 867 opportunities.

- **Data Cleaning** `src/data_cleaning.ipynb`  
  Notebook for deduplication, missing-value handling, type conversion, and standardization of the 3,000-record CRM dataset.

- **SQL Queries** `src/business_analysis_queries.sql`  
  Queries for pipeline snapshots, sales forecasts, closure-time analysis, win-rate calculations, and regional performance.

- **Dashboard Visualizations** `src/CRM-and-Sales-Pipelines.twbx`  
  Tableau workbook with interactive dashboards for pipeline health, revenue forecasts, and market/product analysis.

- **Clean Dataset** `src/CRM-and-Sales-Pipelines_cleaned.csv`  
  The processed CRM dataset—standardized, cleaned, and ready for analytics.
