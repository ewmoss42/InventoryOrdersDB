import os
from dotenv import load_dotenv
import mysql.connector

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = connection.cursor()

query = """
SELECT
  o.order_id,
  CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
  ROUND(SUM(oi.quantity * p.price), 2) AS order_total
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN OrderItems oi ON oi.order_id = o.order_id
JOIN Products p ON p.product_id = oi.product_id
GROUP BY o.order_id, customer_name
ORDER BY o.order_id;
"""

cursor.execute(query)

print("Order Totals:")
for row in cursor:
    print(row)

cursor.close()
connection.close()