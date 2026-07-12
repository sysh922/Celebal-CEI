# E-Commerce Sales Database Analysis using SQL

## Project Overview

This project was completed as part of the **Celebal Summer Internship 2026 - Week 2 Task**. The objective was to analyze an e-commerce sales database using SQL by performing data retrieval, filtering, aggregation, joins, and transaction management operations.

The database represents an online retail platform named **ShopEase**, containing information about customers, products, orders, and order items.

---

## Objectives

- Create and manage relational database tables.
- Load and analyze e-commerce sales data.
- Perform data filtering using WHERE clauses.
- Apply aggregation functions such as COUNT, SUM, AVG, MIN, and MAX.
- Use JOIN operations to combine data across multiple tables.
- Understand database constraints, indexes, and relationships.
- Implement CASE statements for conditional logic.
- Demonstrate ACID properties and transaction management.

---

## Database Schema

The project consists of four tables:

### Customers
- customer_id (Primary Key)
- first_name
- last_name
- email
- city
- state
- join_date
- is_premium

### Products
- product_id (Primary Key)
- product_name
- category
- brand
- unit_price
- stock_qty

### Orders
- order_id (Primary Key)
- customer_id (Foreign Key)
- order_date
- status
- total_amount

### Order_Items
- item_id (Primary Key)
- order_id (Foreign Key)
- product_id (Foreign Key)
- quantity
- unit_price
- discount_pct

---

## Key SQL Concepts Covered

### Section A – SQL Basics
- SELECT statements
- DISTINCT
- Primary Keys
- Constraints (UNIQUE, NOT NULL, CHECK)

### Section B – Filtering & Optimization
- WHERE clause
- BETWEEN
- Logical Operators
- Indexes
- Query Optimization (SARGable Queries)

### Section C – Aggregation
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- GROUP BY
- HAVING

### Section D – Joins & Relationships
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN (Conceptual)
- FULL OUTER JOIN (Conceptual)
- Foreign Keys

### Section E – Advanced SQL
- CASE Statements
- ACID Properties
- Transactions
- COMMIT
- ROLLBACK

---

## Technologies Used

- SQL
- SQLite
- Python
- Pandas
- Jupyter Notebook

---

## Files Included

```text
├── Week2_SQL_Task.ipynb
├── shopease.db
├── README.md
└── Assignment PDF
```

---

## Sample Insights

- Electronics products have the highest average selling price.
- Delivered orders contribute the majority of total revenue.
- JOIN operations help analyze customer purchasing behavior.
- Transactions ensure data consistency and reliability.
- Foreign key constraints maintain referential integrity.

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

- Database design and relationships
- Writing efficient SQL queries
- Data aggregation and reporting
- Query optimization techniques
- Transaction management
- Real-world business data analysis

---

## Author

**Shivanshu Yadav**

Celebal Excellence Internship (Data Engineer) - Celebal Technologies
