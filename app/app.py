"""
=========================================================
RetailMart Analytics Platform

Author : Shivanshu Yadav

Description:
Professional Business Intelligence Dashboard
Powered by Databricks + Streamlit
=========================================================
"""
import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
from pathlib import Path

from utils.loader import (
    load_data,
    refresh_data
)

from utils.db import (
    test_connection
)

from utils.charts import (
    get_kpis,
    monthly_sales_chart,
    product_chart,
    payment_chart,
    delivery_chart,
    top_customers,
    dashboard_summary
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="RetailMart Analytics",

    page_icon="🛒",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# Load CSS
# ==========================================================

css_file = Path("assets/style.css")

if css_file.exists():

    with open(css_file) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# Load Data
# ==========================================================

with st.spinner("Loading data from Databricks..."):

    data = load_data()

customer360 = data["customer360"]

monthly_sales = data["monthly_sales"]

product_performance = data["product_performance"]

payment_summary = data["payment_summary"]

delivery_performance = data["delivery_performance"]

kpi = data["kpi"]

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("🛒 RetailMart")

st.sidebar.caption(
    "Business Intelligence Platform"
)

st.sidebar.divider()

# ----------------------------------------------------------

if test_connection():

    st.sidebar.success("🟢 Connected to Databricks")

else:

    st.sidebar.error("🔴 Connection Failed")

# ----------------------------------------------------------

st.sidebar.button(

    "🔄 Refresh Dashboard",

    on_click=refresh_data,

    use_container_width=True

)

st.sidebar.divider()

# ----------------------------------------------------------

st.sidebar.subheader("Navigation")

page = st.sidebar.radio(

    "",

    [

        "Dashboard",

        "Project Overview"

    ]

)

st.sidebar.divider()

# ----------------------------------------------------------

st.sidebar.subheader("Technology Stack")

st.sidebar.markdown("""

- Python

- PySpark

- SQL

- Delta Lake

- Databricks

- Streamlit

- Plotly

""")

st.sidebar.divider()

st.sidebar.subheader("Medallion Architecture")

st.sidebar.info("""

Bronze

⬇

Silver

⬇

Gold

⬇

Dashboard

""")

# ==========================================================
# Dashboard
# ==========================================================

if page == "Dashboard":

    # ------------------------------------------------------

    st.markdown(
        "<h1 class='dashboard-title'>🛒 RetailMart Analytics Platform</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='dashboard-subtitle'>Live Business Dashboard powered by Databricks SQL Warehouse</p>",
        unsafe_allow_html=True
    )

    st.divider()

    # ------------------------------------------------------
    # KPI
    # ------------------------------------------------------

    kpis = get_kpis(kpi)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.metric(

            "💰 Revenue",

            f"₹ {kpis['revenue']:,.2f}"

        )

    with col2:

        st.metric(

            "📦 Orders",

            f"{int(kpis['orders']):,}"

        )

    with col3:

        st.metric(

            "👥 Customers",

            f"{int(kpis['customers']):,}"

        )

    with col4:

        st.metric(

            "🛒 Avg Order",

            f"₹ {kpis['avg_order']:,.2f}"

        )

    with col5:

        st.metric(

            "🚚 Avg Delivery",

            f"{kpis['delivery']:.2f} Days"

        )

    st.divider()

    # ------------------------------------------------------
    # Dashboard Summary
    # ------------------------------------------------------

    summary = dashboard_summary(

        customer360,

        monthly_sales,

        product_performance

    )

    st.info(

        f"""
Loaded Successfully

👥 Customers : {summary['customers']:,}

📈 Months : {summary['months']}

📦 Products : {summary['products']:,}
"""

    )

    st.divider()


    # ======================================================
    # Monthly Revenue Trend
    # ======================================================

    st.markdown(
        "<h3 class='section-title'>📈 Monthly Revenue Trend</h3>",
        unsafe_allow_html=True
    )

    st.plotly_chart(
        monthly_sales_chart(monthly_sales),
        use_container_width=True
    )

    st.download_button(
        label="📥 Download Monthly Sales",
        data=monthly_sales.to_csv(index=False),
        file_name="monthly_sales.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # Products + Payment Charts
    # ======================================================

    left, right = st.columns(2)

    with left:

        st.markdown(
            "<h3 class='section-title'>📦 Top Product Categories</h3>",
            unsafe_allow_html=True
        )

        st.plotly_chart(
            product_chart(product_performance),
            use_container_width=True
        )

        st.download_button(
            "📥 Download Product Performance",
            product_performance.to_csv(index=False),
            "product_performance.csv",
            "text/csv",
            use_container_width=True,
            key="download_products"
        )

    with right:

        st.markdown(
            "<h3 class='section-title'>💳 Payment Method Distribution</h3>",
            unsafe_allow_html=True
        )

        st.plotly_chart(
            payment_chart(payment_summary),
            use_container_width=True
        )

        st.download_button(
            "📥 Download Payment Summary",
            payment_summary.to_csv(index=False),
            "payment_summary.csv",
            "text/csv",
            use_container_width=True,
            key="download_payment"
        )

    st.divider()

    # ======================================================
    # Delivery Analytics
    # ======================================================

    st.markdown(
        "<h3 class='section-title'>🚚 Delivery Analytics</h3>",
        unsafe_allow_html=True
    )

    st.plotly_chart(
        delivery_chart(delivery_performance),
        use_container_width=True
    )

    st.download_button(
        label="📥 Download Delivery Performance",
        data=delivery_performance.to_csv(index=False),
        file_name="delivery_performance.csv",
        mime="text/csv",
        use_container_width=True,
        key="download_delivery"
    )

    st.divider()


        # ======================================================
    # Top Customers Leaderboard
    # ======================================================

    st.markdown(
        "<h3 class='section-title'>🏆 Top 10 Customers</h3>",
        unsafe_allow_html=True
    )

    top_customer_df = top_customers(customer360)

    st.dataframe(
        top_customer_df,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="📥 Download Customer360",
        data=customer360.to_csv(index=False),
        file_name="customer360.csv",
        mime="text/csv",
        use_container_width=True,
        key="download_customer"
    )

    st.divider()

    # ======================================================
    # Delivery Performance Table
    # ======================================================

    st.markdown(
        "<h3 class='section-title'>🚚 Delivery Performance Summary</h3>",
        unsafe_allow_html=True
    )

    st.dataframe(
        delivery_performance,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="📥 Download Delivery Report",
        data=delivery_performance.to_csv(index=False),
        file_name="delivery_report.csv",
        mime="text/csv",
        use_container_width=True,
        key="download_delivery_table"
    )

    st.divider()

    # ======================================================
    # Footer
    # ======================================================

    st.markdown("---")

    st.caption(
        """
        RetailMart Analytics Platform

        Developed by **Shivanshu Yadav**

        Powered by:
        Databricks • PySpark • Delta Lake • SQL • Streamlit • Plotly

        Architecture:
        Bronze → Silver → Gold → Business Dashboard
        """
    )


# ==========================================================
# Project Overview Page
# ==========================================================

elif page == "Project Overview":

    st.title("📖 RetailMart Project Overview")

    st.markdown("""
## Overview

RetailMart Analytics Platform is an end-to-end Data Engineering project built using the Medallion Architecture.

The project demonstrates how raw retail datasets are ingested, transformed, and presented through an interactive business dashboard.

---

## Technology Stack

- Python
- PySpark
- SQL
- Delta Lake
- Databricks
- Unity Catalog
- Streamlit
- Plotly

---

## Medallion Architecture

### 🥉 Bronze Layer
- Raw CSV ingestion
- Delta Tables
- Data preservation

### 🥈 Silver Layer
- Data cleaning
- Data validation
- Feature engineering
- Business transformations

### 🥇 Gold Layer
- Customer 360
- Monthly Sales
- Product Performance
- Payment Summary
- Delivery Performance
- KPI Dashboard

---

## Dashboard Features

- Live Databricks Connection
- Executive KPI Cards
- Monthly Revenue Trend
- Product Revenue Analysis
- Payment Distribution
- Customer Leaderboard
- Delivery Analytics

---

## Business Value

The dashboard enables business users to:

- Monitor revenue trends
- Track customer spending
- Analyze product performance
- Understand payment behavior
- Evaluate delivery efficiency

without querying raw data.
""")

    st.success("✅ Connected to Databricks SQL Warehouse")

    st.info(
        """
        Dashboard refreshes data directly from the Gold Layer,
        providing near real-time analytics for business users.
        """
    )

    st.markdown("---")

    st.caption(
        """
        RetailMart Analytics Platform

        End-to-End Data Engineering Project

        Shivanshu Yadav
        """
    )