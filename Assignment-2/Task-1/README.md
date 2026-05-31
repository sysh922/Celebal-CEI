# SQL Sales Analysis using Superstore Dataset

## Project Overview
This project analyzes the Superstore sales dataset using SQL queries executed within a Jupyter Notebook. The objective is to explore sales performance, apply filtering and aggregation techniques, identify business trends, and validate data quality.

## Objectives
- Load the dataset into a SQL database.
- Explore the table schema and sample records.
- Apply WHERE filters on region, category, sales, and dates.
- Perform aggregations using GROUP BY.
- Identify top-performing products and categories.
- Analyze monthly sales trends and top customers.
- Detect duplicate records and validate data quality.

## Tools & Technologies
- Python
- Pandas
- SQLite
- Jupyter Notebook

## Dataset
- **Dataset:** Sample Superstore Dataset
- **Format:** CSV

## Project Workflow

### 1. Data Loading
- Imported the CSV file using Pandas.
- Created an SQLite database.
- Loaded the dataset into a SQL table named `sales`.

### 2. Data Exploration
- Examined table schema.
- Viewed sample records.
- Checked column names and data types.

### 3. Data Filtering (WHERE Clause)
Examples:
- Sales in the West region.
- Technology category products.
- Orders with sales greater than 500.
- Date-based filtering.

### 4. Aggregations (GROUP BY)
Performed:
- Total sales by category.
- Total quantity sold by category.
- Average sales by region.
- Regional sales summaries.

### 5. Sorting & Ranking
Identified:
- Top 10 products by sales.
- Top categories by revenue.
- Top customers by total purchases.

### 6. Business Analysis
Conducted:
- Monthly sales trend analysis.
- Customer revenue analysis.
- Duplicate order detection.

### 7. Data Validation
Verified:
- Total row count.
- Missing values.
- Distinct customers and products.
- Duplicate records.

## Key Insights
- Technology category generated the highest sales revenue.
- West region contributed significantly to overall sales.
- A small group of customers accounted for a large portion of total revenue.
- Sales trends varied across different months.
- Dataset showed minimal data quality issues.

Learning Outcomes
SQL querying fundamentals
Data filtering using WHERE
Aggregation using GROUP BY
Sorting and ranking with ORDER BY and LIMIT
Business-oriented data analysis
Data validation and quality checks

## Author

Shivanshu Yadav

Celebal Excellence Internship (Data Engineer) - Celebal Technologies
