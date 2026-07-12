import plotly.express as px
import plotly.graph_objects as go


# =========================================================
# Monthly Revenue Trend
# =========================================================

def monthly_sales_chart(df):

    fig = px.line(
        df,
        x="sales_month",
        y="total_revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.02,

        xaxis_title="Month",

        yaxis_title="Revenue (₹)",

        hovermode="x unified",

        height=450,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    fig.update_traces(
        line=dict(width=4),
        marker=dict(size=8)
    )

    return fig


# =========================================================
# Product Revenue
# =========================================================

import plotly.express as px


def product_chart(df):

    # Sort by revenue (highest first)
    df = df.sort_values(
        by="total_revenue",
        ascending=False
    )

    fig = px.bar(

        df,

        x="product_category_name",

        y="total_revenue",

        color="total_revenue",

        title="Revenue by Product Category",

        text="total_revenue"

    )

    fig.update_traces(

        texttemplate="₹ %{text:,.0f}",

        textposition="outside"

    )

    fig.update_layout(

        template="plotly_white",

        height=500,

        xaxis_title="Product Category",

        yaxis_title="Revenue (₹)",

        xaxis_tickangle=-30,

        showlegend=False,

        coloraxis_showscale=False,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    return fig

# =========================================================
# Payment Distribution
# =========================================================

def payment_chart(df):

    fig = px.pie(

        df,

        values="number_of_payments",

        names="payment_type",

        hole=0.55,

        title="Payment Method Distribution"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.02,

        height=450,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    return fig


# =========================================================
# Delivery Performance
# =========================================================

def delivery_chart(df):

    fig = px.bar(

        df,

        x="order_status",

        y="avg_delivery_days",

        color="avg_delivery_days",

        text_auto=".2f",

        title="Average Delivery Days"
    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.02,

        xaxis_title="Order Status",

        yaxis_title="Days",

        height=450,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    return fig


# =========================================================
# KPI Cards
# =========================================================

def get_kpis(df):

    row = df.iloc[0]

    return {

        "revenue": row["total_revenue"],

        "customers": row["total_customers"],

        "orders": row["total_orders"],

        "avg_order": row["average_order_value"],

        "delivery": row["average_delivery_days"]

    }


# =========================================================
# Customer Leaderboard
# =========================================================

def top_customers(df):

    return (

        df

        .sort_values(

            "total_spent",

            ascending=False

        )

        .head(10)

    )


# =========================================================
# Dashboard Statistics
# =========================================================

def dashboard_summary(customer360,
                      monthly_sales,
                      products):

    return {

        "customers": len(customer360),

        "months": len(monthly_sales),

        "products": len(products)

    }