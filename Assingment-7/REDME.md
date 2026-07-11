# Week 7 - Delta Lake MERGE Implementation

## Overview

This assignment demonstrates how to perform **incremental data processing** using **Delta Lake** with **PySpark** in **Databricks**. The workflow includes loading a dataset, cleaning the data, creating a customer master table, simulating incremental records, performing a **MERGE** operation, and validating the final output.

The project highlights how Delta Lake simplifies **upsert operations** while ensuring **ACID transactions**, making it a reliable solution for modern data engineering pipelines.

---

## Objectives

- Load a CSV dataset into a Delta Table.
- Clean the dataset by removing duplicate records and handling missing values.
- Create a customer master dataset.
- Simulate incremental data containing both updated and new records.
- Perform the Delta Lake **MERGE** operation.
- Validate the final dataset after the merge.
- Understand incremental data processing using Databricks and PySpark.

---

## Technologies Used

- Databricks Community Edition
- Apache Spark
- PySpark
- Delta Lake
- Python
- Jupyter Notebook

---


## Workflow

1. Load the Superstore dataset.
2. Explore the dataset and examine its schema.
3. Clean the data by removing duplicates and missing values.
4. Create a Customer Master table.
5. Save the Customer Master as a Delta Table.
6. Prepare an incremental dataset with updated and new records.
7. Apply the Delta Lake **MERGE** operation.
8. Validate the final dataset.

---

## Key Concepts Covered

- Apache Spark DataFrames
- Delta Lake
- ACID Transactions
- Delta Tables
- Incremental Data Processing
- Upsert Operations
- MERGE INTO
- Data Validation
- Data Engineering Best Practices

---

## Screenshots Included

- Dataset Loading
- Dataset Schema
- Cleaned Dataset
- Customer Master Table
- Delta Table Creation
- Incremental Dataset
- MERGE Operation
- Final Validation

---

## Learning Outcomes

Through this assignment, I learned how to:

- Work with Delta Lake in Databricks.
- Create and manage Delta Tables using PySpark.
- Perform incremental data loading.
- Update and insert records using the **MERGE** operation.
- Validate processed data after transformations.
- Understand the importance of ACID transactions in Delta Lake.

---

## Conclusion

This assignment demonstrates an end-to-end implementation of incremental data processing using Delta Lake. Existing customer records were updated, new records were inserted, and the final dataset was successfully validated. The project also provided practical experience with Delta Lake's MERGE operation and showcased how Databricks and PySpark can be used to build scalable and reliable data engineering pipelines.

---

## Author

**Shivanshu Yadav**

**Celebal Excellence Internship (Data Engineer)**  
**Celebal Technologies**
