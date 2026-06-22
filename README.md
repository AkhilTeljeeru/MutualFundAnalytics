# Mutual Fund Analytics Project

## Project Overview

This project focuses on collecting, validating, and analyzing mutual fund data using Python, Pandas, SQL, and data visualization tools.

The objective is to build a data pipeline that ingests mutual fund datasets, validates data quality, fetches live NAV data from public APIs, and prepares the data for further analysis and dashboard development.

---

## Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* Requests
* SciPy
* Jupyter Notebook
* Git & GitHub

---

## Day 1 Tasks Completed

* Created project folder structure
* Initialized Git repository
* Installed required dependencies
* Loaded and validated 10 CSV datasets
* Checked dataset shapes and data types
* Checked missing values and duplicates
* Validated AMFI scheme codes
* Fetched live NAV data from mfapi.in
* Downloaded NAV history for multiple mutual fund schemes
* Generated data quality summary
* Pushed project to GitHub

---

## Data Quality Results

* Missing Values: 0
* Duplicate AMFI Codes: 0
* Missing AMFI Codes in NAV History: 0

The datasets are complete, consistent, and ready for further analysis.

---

## Future Work

* Data Cleaning
* Exploratory Data Analysis (EDA)
* SQL Database Integration
* Mutual Fund Performance Analysis
* Risk Analysis
* Interactive Dashboard Development
* Reporting and Insights
