# Week 6 - Apache Spark Assignment

## Q1. Explain the roles of the Driver, Cluster Manager, and Executor in a Spark application.

### Answer:
- **Driver:** The Driver is the main process that runs the Spark application. It creates the Spark session, converts the user program into tasks, and coordinates the execution.
- **Cluster Manager:** It is responsible for managing the available resources in the cluster and assigning them to Spark applications.
- **Executor:** Executors are worker processes that execute the tasks assigned by the Driver and store data in memory or on disk during computation.

---

## Q2. How does Spark's Lazy Evaluation strategy improve performance when processing large datasets?

### Answer:
Spark does not execute transformations immediately. Instead, it records them in a logical execution plan (DAG). The actual execution begins only when an action is called. This approach allows Spark to optimize the execution plan, reduce unnecessary operations, and improve overall performance.

---

## Q3. Write a Spark command to read a CSV file located at "data/source.csv", ensuring the first row is treated as a header and inferSchema is enabled.

### Answer:

```python
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("data/source.csv")
```

---

## Q4. What is the difference between CSV and Parquet in terms of storage (row-based vs. columnar) and why does it matter for performance?

### Answer:

| CSV | Parquet |
|------|----------|
| Row-based storage | Column-based storage |
| Larger file size | Compressed and smaller |
| Slower for analytics | Faster for analytical queries |
| No schema support | Stores schema information |

Parquet reads only the required columns, which reduces disk I/O and improves query performance.

---

## Q5. Given a DataFrame `df`, write a query to select the columns `product_id` and `price` where the category is 'Electronics'.

### Answer:

```python
df.filter(df.category == "Electronics") \
  .select("product_id", "price")
```

---

## Q6. Write the code to revise a DataFrame by renaming the column `old_name` to `new_name` and casting the `price` column from String to Double.

### Answer:

```python
from pyspark.sql.functions import col

df = df.withColumnRenamed("old_name", "new_name") \
       .withColumn("price", col("price").cast("double"))
```

---

## Q7. How does Spark use the Lineage Graph (DAG) to provide fault tolerance if a worker node fails?

### Answer:
Spark maintains a DAG that records all transformations applied to the data. If a partition is lost because of a worker failure, Spark uses the DAG to recompute only the missing partition instead of recalculating the entire dataset. This provides efficient fault tolerance.

---

## Q8. Write a query to filter a DataFrame `df_orders` for rows where the status is 'Completed' AND the amount is greater than 1000.

### Answer:

```python
df_orders.filter(
    (df_orders.status == "Completed") &
    (df_orders.amount > 1000)
)
```

---

## Q9. Explain the concept of Predicate Pushdown in Parquet and how it affects the amount of data loaded into memory.

### Answer:
Predicate Pushdown allows Spark to apply filtering conditions while reading a Parquet file. Instead of loading the complete dataset, only the required rows are read into memory. This reduces disk access, memory usage, and query execution time.

---

## Q10. Write a code snippet to add a new column `final_price` which is the `base_price` multiplied by 1.18 (18% tax).

### Answer:

```python
from pyspark.sql.functions import col

df = df.withColumn("final_price", col("base_price") * 1.18)
```

---

## Q11. What is the difference between Transformations and Actions? Provide two examples of each.

### Answer:

**Transformations**
- Create a new DataFrame or RDD.
- Executed lazily.

Examples:
- `filter()`
- `select()`

**Actions**
- Trigger the execution of transformations.
- Return results or write data.

Examples:
- `show()`
- `collect()`

---

## Q12. Write the Spark command to load a Parquet file from `"path/to/input"`, filter out any rows where `user_id` is null, and save the result as a CSV at `"path/to/output"`.

### Answer:

```python
spark.read.parquet("path/to/input") \
    .filter("user_id IS NOT NULL") \
    .write.option("header", "true") \
    .csv("path/to/output")
```

---

## Q13. In Spark Architecture, what is the difference between Client Mode and Cluster Mode?

### Answer:

| Client Mode | Cluster Mode |
|--------------|--------------|
| Driver runs on the user's machine | Driver runs inside the cluster |
| Suitable for development and testing | Suitable for production |
| Driver failure stops the application | More reliable and fault tolerant |

---

## Q14. Write a query to filter a dataset for rows where the region is 'North' OR the priority is 'High'.

### Answer:

```python
df.filter(
    (df.region == "North") |
    (df.priority == "High")
)
```

---

## Q15. When exploring a dataset, why is it safer to use `.show(5)` instead of `.collect()` on a multi-terabyte dataset?

### Answer:
`.show(5)` retrieves and displays only a few rows, making it fast and memory-efficient. On the other hand, `.collect()` transfers the entire dataset to the Driver, which can consume excessive memory and may even crash the application when working with very large datasets.

---
