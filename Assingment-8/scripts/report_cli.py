import argparse
import sqlite3
import pandas as pd
import os
from tabulate import tabulate

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "ecommerce.db")

reports = {

"revenue": """
SELECT
c.customer_name,
ROUND(SUM(oi.quantity*oi.unit_price),2) AS Revenue
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_name
ORDER BY Revenue DESC
LIMIT 10;
""",

"top_products": """
SELECT
p.product_name,
SUM(oi.quantity) AS Quantity
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
GROUP BY p.product_name
ORDER BY Quantity DESC
LIMIT 10;
""",

"monthly": """
SELECT
strftime('%Y-%m',order_date) AS Month,
COUNT(*) AS Orders
FROM orders
GROUP BY Month;
"""
}

parser = argparse.ArgumentParser()

parser.add_argument(
    "--report",
    required=True,
    help="revenue | top_products | monthly"
)

args = parser.parse_args()

if args.report not in reports:
    print("Invalid report name.")
    exit()

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql_query(reports[args.report], conn)

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

conn.close()