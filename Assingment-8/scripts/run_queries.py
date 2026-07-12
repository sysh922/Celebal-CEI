import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "ecommerce.db")

conn = sqlite3.connect(DB_PATH)

queries = {
    "Revenue by Customer": """
    SELECT
        c.customer_name,
        ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100)), 2) AS total_revenue
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.customer_name
    ORDER BY total_revenue DESC
    LIMIT 10;
    """,

    "Revenue by Category": """
    SELECT
        p.category,
        ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100)), 2) AS revenue
    FROM products p
    JOIN order_items oi ON p.product_id = oi.product_id
    GROUP BY p.category
    ORDER BY revenue DESC;
    """,

    "Top Products": """
    SELECT
        p.product_name,
        SUM(oi.quantity) AS quantity_sold,
        ROUND(SUM(oi.quantity * oi.unit_price),2) AS revenue
    FROM products p
    JOIN order_items oi ON p.product_id = oi.product_id
    GROUP BY p.product_id, p.product_name
    ORDER BY revenue DESC
    LIMIT 10;
    """,

    "Monthly Revenue": """
    SELECT
        strftime('%Y-%m', o.order_date) AS month,
        ROUND(SUM(oi.quantity * oi.unit_price),2) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY month
    ORDER BY month;
    """,
    "Customer Rank": """
SELECT
    c.customer_name,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS revenue,
    RANK() OVER(
        ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS rank
FROM customers c
JOIN orders o ON c.customer_id=o.customer_id
JOIN order_items oi ON o.order_id=oi.order_id
GROUP BY c.customer_id,c.customer_name
LIMIT 10;
""",

"Running Revenue": """
SELECT
    o.order_date,
    ROUND(SUM(oi.quantity*oi.unit_price),2) AS revenue,
    ROUND(
        SUM(SUM(oi.quantity*oi.unit_price))
        OVER(ORDER BY o.order_date),
        2
    ) AS running_total
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY o.order_date;
"""

    
}

for title, query in queries.items():
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    df = pd.read_sql_query(query, conn)

    print(df)

conn.close()