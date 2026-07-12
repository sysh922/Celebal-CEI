# 🛒 RetailMart Analytics Platform

An end-to-end Data Engineering project that transforms raw retail data into business-ready insights using the **Medallion Architecture (Bronze → Silver → Gold)**. The project demonstrates modern data engineering practices with **PySpark, Delta Lake, Databricks, SQL, and Streamlit** to build an interactive analytics dashboard.

---

## 📌 Project Overview

RetailMart generates large volumes of transactional data from customers, orders, products, and payments. This project builds a centralized analytics platform that ingests raw data, cleans and transforms it, creates business-ready datasets, and visualizes key business metrics through a live dashboard.

---

## 🎯 Objectives

- Build an end-to-end Data Engineering pipeline.
- Implement the Medallion Architecture.
- Clean and transform raw retail datasets.
- Create business-ready Gold Layer tables.
- Perform SQL-based business analysis.
- Build an interactive Streamlit dashboard.
- Connect Streamlit directly with Databricks for real-time reporting.

---

# 🏗️ Medallion Architecture

```
                Raw CSV Files
                     │
                     ▼
             🥉 Bronze Layer
          (Raw Data Ingestion)
                     │
                     ▼
             🥈 Silver Layer
      (Cleaning & Transformation)
                     │
                     ▼
              🥇 Gold Layer
      (Business Ready Tables)
                     │
                     ▼
              SQL Analytics
                     │
                     ▼
          Streamlit Dashboard
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming |
| PySpark | Data Processing |
| Databricks | Data Engineering Platform |
| Delta Lake | ACID Storage |
| SQL | Business Analysis |
| Streamlit | Dashboard |
| Plotly | Interactive Charts |
| Pandas | Data Handling |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```
RetailMart_E_Commerce/

│
├── app/
│   ├── app.py
│   └── style.css
│
├── utils/
│   ├── db.py
│   ├── loader.py
│   └── charts.py
│
├── notebooks/
│   ├── 01_Data_Exploration
│   ├── 02_Bronze_Layer
│   ├── 03_Silver_Layer
│   ├── 04_Gold_Layer
│   ├── 05_SQL_Analytics
│   └── 06_Export_Gold_Tables
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── requirements.txt
└── README.md
```

---

# 📊 Datasets Used

- Customers
- Orders
- Order Items
- Products
- Payments

---

# 🥉 Bronze Layer

The Bronze Layer stores the raw datasets without modification.

### Tasks Performed

- Loaded CSV files into Databricks.
- Created Bronze Delta Tables.
- Preserved original data.
- Maintained schema consistency.

---

# 🥈 Silver Layer

The Silver Layer focuses on data cleaning and transformation.

### Tasks Performed

- Removed duplicates
- Handled null values
- Standardized column names
- Converted data types
- Improved data quality

---

# 🥇 Gold Layer

Business-ready tables created for analytics.

### Gold Tables

- Customer360
- Monthly Sales
- Product Performance
- Payment Summary
- Delivery Performance
- KPI Dashboard

---

# 📈 SQL Analytics

Business insights generated using SQL.

Examples:

- Monthly Revenue Analysis
- Customer Spending Analysis
- Product Category Performance
- Payment Method Distribution
- Delivery Performance
- KPI Summary

---

# 📊 Dashboard Features

The Streamlit dashboard connects directly to Databricks SQL Warehouse.

Features include:

- Live Databricks Connection
- Interactive KPI Cards
- Monthly Revenue Trend
- Product Revenue Analysis
- Payment Distribution
- Top Customers
- Month Range Filter
- CSV Export
- Responsive Layout

---

# 📌 KPIs

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Average Delivery Time

---

# 🚀 Business Insights

The dashboard helps answer questions such as:

- Which product categories generate the highest revenue?
- How does revenue change over time?
- Which payment methods are most popular?
- Who are the highest-value customers?
- What are the key business KPIs?

---

# 💡 Skills Demonstrated

- Data Engineering
- ETL Pipeline Development
- PySpark
- Delta Lake
- Databricks
- SQL Analytics
- Streamlit Dashboard Development
- Data Visualization
- Data Modeling

---

# 📷 Dashboard Preview

- 📈Home Dashboard
![Home Page](<Screenshots/Home Dashboard.png>)


- 📦Product Analysis and Payment Distribution
![Monthly Revenue](<Screenshots/Monthly Revenue.png>)


- 🚚 Delivery Analytics and Top Customer
![Delivery Analytics](<Screenshots/Delivery Analytics.png>)
![Top Customer](<Screenshots/Top Customer.png>)



---

# 👨‍💻 Author

**Shivanshu Yadav**

Data Engineering Enthusiast

---



