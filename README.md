\# Financial Market Intelligence Platform



\## Project Overview

This project develops a Financial Market Intelligence Platform using an end-to-end ETL pipeline. The system integrates financial data from multiple APIs, processes and stores it in a structured database, and visualises insights using an interactive Power BI dashboard.



\---



\## Data Sources

The project integrates multiple external APIs:



\- Alpha Vantage API – Stock market data  

\- Frankfurter API – Exchange rates (EUR/USD)  

\- World Bank API – Macroeconomic indicators (GDP)  



\---



\## ETL Pipeline



\### 1. Extraction

Data is collected from external APIs using Python and the `requests` library.



\### 2. Transformation

Data is cleaned and processed using `pandas`, including:



\- Handling missing values  

\- Converting data types  

\- Creating new features:

&#x20; - Daily Returns  

&#x20; - Volatility (Risk Measure using rolling standard deviation)  



\### 3. Loading

Processed data is stored in a PostgreSQL database:



\- Tables:

&#x20; - `market\_prices`  

&#x20; - `fx\_rates`  

&#x20; - `macro\_indicators`  



\---



\## Automation

The pipeline is automated using:



\- `pipeline.py` script  

\- Cron scheduling for periodic execution  



This ensures the system runs automatically at regular intervals without manual intervention.



\---



\## Machine Learning Component

A machine learning model is implemented to demonstrate predictive analytics:



\- Model: Random Forest Regressor  

\- Type: Regression (predicting numerical financial values)  

\- Purpose: Forecast financial trends  

\- Evaluation Metric: Mean Squared Error (MSE)  



\---



\## Data Visualisation

A Power BI dashboard was developed to present financial insights:



\### Key Features:

\- Stock Price Trend (time-series analysis)  

\- Daily Return Distribution  

\- GDP Trend (Germany)  



\### Key Performance Indicators (KPIs):

\- Latest Stock Price  

\- Average Return  

\- Risk (%) (Volatility)  

\- EUR/USD Exchange Rate  



\### Interactivity:

\- Date range slicer  

\- Dynamic filtering across all visuals  



\---



\## Tools \& Technologies

\- Python (pandas, requests, scikit-learn)  

\- PostgreSQL  

\- Power BI  

\- Jupyter Notebook  

\- Cron (automation)  



\---



\## Key Insights

\- Financial trends change dynamically over time  

\- Volatility reflects market risk and uncertainty  

\- Integration of macroeconomic data improves financial analysis  



\---



\## Project Structure



``

