import os
import pandas as pd

# ==========================
# Folder Paths
# ==========================
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_PATH = os.path.join(BASE_DIR, "data", "raw")
CLEAN_PATH = os.path.join(BASE_DIR, "data", "cleaned")

os.makedirs(CLEAN_PATH, exist_ok=True)



# ==========================
# Load CSV Files
# ==========================
customers = pd.read_csv(f"{RAW_PATH}/customers.csv")
products = pd.read_csv(f"{RAW_PATH}/products.csv")
orders = pd.read_csv(f"{RAW_PATH}/orders.csv")
order_items = pd.read_csv(f"{RAW_PATH}/order_items.csv")

print("=" * 50)
print("Original Dataset Shapes")
print("=" * 50)
print("Customers   :", customers.shape)
print("Products    :", products.shape)
print("Orders      :", orders.shape)
print("Order Items :", order_items.shape)


# ==========================
# Function for Cleaning
# ==========================
def clean_dataframe(df, name):
    print(f"\nCleaning {name}...")

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"Duplicates Removed: {before - after}")

    # Fill missing values
    for col in df.columns:

        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())

        else:
            mode = df[col].mode()

            if not mode.empty:
                df[col] = df[col].fillna(mode[0])
            else:
                df[col] = df[col].fillna("Unknown")

    return df


customers = clean_dataframe(customers, "Customers")
products = clean_dataframe(products, "Products")
orders = clean_dataframe(orders, "Orders")
order_items = clean_dataframe(order_items, "Order Items")


# ==========================
# Convert Date Columns
# ==========================
if "order_date" in orders.columns:
    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )

    orders = orders.dropna(subset=["order_date"])


# ==========================
# Referential Integrity
# ==========================

# customer_id in orders
if "customer_id" in orders.columns and "customer_id" in customers.columns:

    orders = orders[
        orders["customer_id"].isin(customers["customer_id"])
    ]


# order_id in order_items
if "order_id" in order_items.columns and "order_id" in orders.columns:

    order_items = order_items[
        order_items["order_id"].isin(orders["order_id"])
    ]


# product_id in order_items
if "product_id" in order_items.columns and "product_id" in products.columns:

    order_items = order_items[
        order_items["product_id"].isin(products["product_id"])
    ]


# ==========================
# Save Cleaned Files
# ==========================
customers.to_csv(
    f"{CLEAN_PATH}/customers_clean.csv",
    index=False
)

products.to_csv(
    f"{CLEAN_PATH}/products_clean.csv",
    index=False
)

orders.to_csv(
    f"{CLEAN_PATH}/orders_clean.csv",
    index=False
)

order_items.to_csv(
    f"{CLEAN_PATH}/order_items_clean.csv",
    index=False
)


print("\n" + "=" * 50)
print("Cleaning Completed Successfully")
print("=" * 50)

print("\nCleaned Dataset Shapes")

print("Customers   :", customers.shape)
print("Products    :", products.shape)
print("Orders      :", orders.shape)
print("Order Items :", order_items.shape)

print("\nFiles saved in:")
print(CLEAN_PATH)