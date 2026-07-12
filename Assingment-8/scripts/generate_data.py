import pandas as pd

print(pd.read_csv("data/cleaned/customers_clean.csv").columns.tolist())
print(pd.read_csv("data/cleaned/products_clean.csv").columns.tolist())
print(pd.read_csv("data/cleaned/orders_clean.csv").columns.tolist())
print(pd.read_csv("data/cleaned/order_items_clean.csv").columns.tolist())