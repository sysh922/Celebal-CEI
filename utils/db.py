"""
=========================================================
RetailMart Analytics Platform
Databricks Connection Module
=========================================================
"""

import logging

import pandas as pd
import streamlit as st
from databricks import sql


# ---------------------------------------------------------
# Configure Logging
# ---------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# Create Databricks Connection
# ---------------------------------------------------------

@st.cache_resource
def get_connection():
    """
    Creates and caches a Databricks SQL Warehouse connection.
    The connection is reused until the app restarts.
    """

    try:

        connection = sql.connect(
            server_hostname=st.secrets["DATABRICKS_SERVER_HOSTNAME"],
            http_path=st.secrets["DATABRICKS_HTTP_PATH"],
            access_token=st.secrets["DATABRICKS_TOKEN"]
        )

        logger.info("Connected to Databricks SQL Warehouse.")

        return connection

    except Exception as e:

        logger.exception("Databricks connection failed.")

        st.error(f"Unable to connect to Databricks.\n\n{e}")

        st.stop()


# ---------------------------------------------------------
# Execute SQL Query
# ---------------------------------------------------------

def execute_query(query: str) -> pd.DataFrame:
    """
    Executes a SQL query and returns a Pandas DataFrame.

    Parameters
    ----------
    query : str
        SQL query to execute.

    Returns
    -------
    pd.DataFrame
    """

    connection = get_connection()

    cursor = connection.cursor()

    try:

        cursor.execute(query)

        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]

        dataframe = pd.DataFrame(rows, columns=columns)

        return dataframe

    except Exception as e:

        logger.exception("SQL Query Failed")

        st.error(f"Query Execution Failed\n\n{e}")

        return pd.DataFrame()

    finally:

        cursor.close()


# ---------------------------------------------------------
# Test Connection
# ---------------------------------------------------------

def test_connection() -> bool:
    """
    Tests whether Databricks is reachable.
    """

    try:

        execute_query("SELECT 1")

        return True

    except Exception:

        return False