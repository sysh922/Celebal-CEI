SELECT
    c.customer_name,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS revenue,
    RANK() OVER(
        ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS customer_rank
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.customer_name;


SELECT
    c.customer_name,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS revenue,
    DENSE_RANK() OVER(
        ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS dense_rank
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.customer_name;


SELECT
    o.order_date,
    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS daily_revenue,

    ROUND(
        SUM(
            SUM(oi.quantity * oi.unit_price)
        ) OVER(
            ORDER BY o.order_date
        ),
        2
    ) AS running_total

FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY o.order_date
ORDER BY o.order_date;


SELECT
    o.order_date,

    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS revenue,

    ROUND(
        AVG(
            SUM(oi.quantity * oi.unit_price)
        ) OVER(
            ORDER BY o.order_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS moving_average

FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY o.order_date
ORDER BY o.order_date;


