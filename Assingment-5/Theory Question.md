# Week 5 - Apache Spark DataFrame Operations and Data Cleaning


## Q1. What are the key limitations of traditional MapReduce that make Spark a preferred choice for modern big data processing?

### Answer

Traditional MapReduce stores intermediate results on disk after every stage, which makes processing slow, especially for iterative tasks. Writing and reading data repeatedly from disk increases latency. It also requires complex code for operations that need multiple processing steps. Spark overcomes these limitations by performing most computations in memory and providing high-level APIs, making it much faster and easier to use.

---

## Q2. Explain how Spark uses In-Memory Computing to speed up iterative machine learning algorithms compared to disk-based systems.

### Answer

Spark keeps frequently used data in memory (RAM) instead of writing it to disk after each operation. Machine learning algorithms often process the same dataset multiple times during training. Since Spark avoids repeated disk I/O operations, it significantly reduces execution time and speeds up iterative computations.

---

## Q3. Remove all duplicate rows based on `user_id` and `transaction_date`.

```python
df_clean = df.dropDuplicates(["user_id", "transaction_date"])
```

---

## Q4. Filter rows where `region` is `'West'` and calculate the average `sale_amount` for each `product_category`.

```python
from pyspark.sql.functions import avg

result = (df_sales
          .filter(df_sales.region == "West")
          .groupBy("product_category")
          .agg(avg("sale_amount").alias("average_sale")))
```

---

## Q5. What is the difference between `.na.drop()` and `.na.fill()`?

### Answer

* `.na.drop()` removes rows that contain null values.
* `.na.fill()` replaces null values with a specified value.

Example:

```python
df = df.na.fill({"status": "Unknown"})
```

---

## Q6. Find the total count of records for each city where the count is greater than 100.

```python
from pyspark.sql.functions import count

result = (df.groupBy("city")
            .agg(count("*").alias("total_records"))
            .filter("total_records > 100"))
```

---

## Q7. How does the immutability of Spark DataFrames affect data cleaning?

### Answer

Spark DataFrames are immutable, which means existing DataFrames cannot be modified directly. Every operation such as dropping columns, renaming columns, or filtering data creates a new DataFrame. Therefore, each cleaning step must be assigned to a new variable or overwrite the existing reference.

Example:

```python
df = df.drop("age")
df = df.withColumnRenamed("name", "full_name")
```

---

## Q8. Filter rows where age is between 18 and 30 and subscription is `'Premium'`.

```python
result = df.filter(
    (df.age.between(18, 30)) &
    (df.subscription == "Premium")
)
```

---

## Q9. Why should null values be handled before performing aggregations like `sum()` or `avg()`?

### Answer

Null values can produce incorrect or misleading results during aggregations. Missing values may cause records to be ignored or calculations to be inaccurate. Cleaning or replacing null values beforehand ensures that the computed statistics represent the data correctly.

---

## Q10. Cast `raw_timestamp` to `TimestampType` and rename it to `event_time`.

```python
from pyspark.sql.functions import col
from pyspark.sql.types import TimestampType

df = (df
      .withColumn("event_time",
                  col("raw_timestamp").cast(TimestampType()))
      .drop("raw_timestamp"))
```

---

## Q11. Explain the Shuffle process and why it is a wide transformation.

### Answer

A shuffle occurs when Spark redistributes data across partitions so that records with the same key are placed together. Operations such as `groupBy`, `join`, and `reduceByKey` require shuffling. Since data moves between different partitions and executors, these operations are called wide transformations and are generally more expensive than narrow transformations.

---

## Q12. Remove rows where `email` is null or `username` is an empty string.

```python
result = df.filter(
    df.email.isNotNull() &
    (df.username != "")
)
```

---

## Q13. Calculate the minimum, maximum, and mean of the `price` column.

```python
from pyspark.sql.functions import min, max, mean

result = df.agg(
    min("price").alias("min_price"),
    max("price").alias("max_price"),
    mean("price").alias("avg_price")
)
```

---

## Q14. What is the risk of using `inferSchema=true` with inconsistent date formats?

### Answer

When source data contains inconsistent date formats, Spark may infer an incorrect data type or interpret some values as strings while treating others as dates. This can lead to parsing errors, null values, and unreliable results during analysis. It is generally safer to define the schema explicitly when the data is messy.

---

## Q15. Final Processing Pipeline

Requirements:

1. Remove duplicates.
2. Fill null prices with `0`.
3. Group by `store_id` and calculate total revenue.

```python
from pyspark.sql.functions import sum

result = (df
          .dropDuplicates()
          .na.fill({"price": 0})
          .groupBy("store_id")
          .agg(sum("price").alias("total_revenue")))
```

---

