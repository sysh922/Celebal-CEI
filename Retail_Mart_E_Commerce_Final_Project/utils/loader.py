"""
=========================================================
RetailMart Analytics Platform
Data Loader Module

Author : Shivanshu Yadav
=========================================================
"""

import streamlit as st
import pandas as pd

from utils.db import execute_query


# =========================================================
# Gold Layer Tables
# =========================================================

TABLES = {

    "customer360": "workspace.default.gold_customer360",

    "monthly_sales": "workspace.default.gold_monthly_sales",

    "product_performance": "workspace.default.gold_product_performance",

    "payment_summary": "workspace.default.gold_payment_summary",

    "delivery_performance": "workspace.default.gold_delivery_performance",

    "kpi": "workspace.default.gold_kpi_dashboard"

}


# =========================================================
# Load All Tables
# =========================================================

@st.cache_data(ttl=300, show_spinner="Loading data from Databricks...")
def load_data():
    """
    Load all Gold Layer tables from Databricks.

    Returns
    -------
    dict
        Dictionary containing all DataFrames.
    """

    data = {}

    for key, table in TABLES.items():

        query = f"""
        SELECT *
        FROM {table}
        """

        try:

            df = execute_query(query)

            data[key] = clean_dataframe(df)

        except Exception as e:

            st.error(f"Failed to load {table}")

            st.exception(e)

            data[key] = pd.DataFrame()

    return data


# =========================================================
# Clean DataFrame
# =========================================================

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataframe after loading.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    if df.empty:
        return df

    # -----------------------------
    # Revenue Columns
    # -----------------------------

    revenue_columns = [

        "total_revenue",

        "total_spent",

        "average_order_value",

        "total_amount"

    ]

    for column in revenue_columns:

        if column in df.columns:

            df[column] = (

                df[column]

                .astype(str)

                .str.replace(",", "", regex=False)

                .astype(float)

            )

    # -----------------------------
    # Delivery Columns
    # -----------------------------

    if "average_delivery_days" in df.columns:

        df["average_delivery_days"] = (

            df["average_delivery_days"]

            .astype(float)

            .round(2)

        )

    if "avg_delivery_days" in df.columns:

        df["avg_delivery_days"] = (

            df["avg_delivery_days"]

            .astype(float)

            .round(2)

        )

    # -----------------------------
    # Monthly Sales Date
    # -----------------------------

    if "sales_month" in df.columns:

        df["sales_month"] = pd.to_datetime(

            df["sales_month"],

            format="%Y-%m"

        )

    # -----------------------------
    # Purchase Dates
    # -----------------------------

    date_columns = [

        "first_purchase",

        "last_purchase"

    ]

    for column in date_columns:

        if column in df.columns:

            df[column] = pd.to_datetime(df[column])

    return df


# =========================================================
# Refresh Cache
# =========================================================

def refresh_data():
    """
    Clear Streamlit cache.
    """

    st.cache_data.clear()


# =========================================================
# Get Single Table
# =========================================================

def get_table(name: str):
    """
    Returns a single dataframe.

    Example
    -------
    data = load_data()

    customers = get_table("customer360")
    """

    data = load_data()

    return data.get(name, pd.DataFrame())