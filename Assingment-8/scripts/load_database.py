import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "database", "ecommerce.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "sql", "schema.sql")
DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create Tables
with open(SCHEMA_PATH, "r") as file:
    cursor.executescript(file.read())

print("Tables Created Successfully!")

# Load Cleaned CSVs
customers = pd.read_csv(os.path.join(DATA_PATH, "customers_clean.csv"))
products = pd.read_csv(os.path.join(DATA_PATH, "products_clean.csv"))
orders = pd.read_csv(os.path.join(DATA_PATH, "orders_clean.csv"))
order_items = pd.read_csv(os.path.join(DATA_PATH, "order_items_clean.csv"))

# Insert into SQLite
customers.to_sql("customers", conn, if_exists="append", index=False)
products.to_sql("products", conn, if_exists="append", index=False)
orders.to_sql("orders", conn, if_exists="append", index=False)
order_items.to_sql("order_items", conn, if_exists="append", index=False)

print("\nData Loaded Successfully!\n")

tables = ["customers", "products", "orders", "order_items"]

for table in tables:
    count = cursor.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"{table:<12}: {count} rows")

conn.commit()
conn.close()

print("\nDatabase Created Successfully!")