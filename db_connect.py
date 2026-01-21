import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables from .env
load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = connection.cursor()

query = """
SELECT p.product_name, p.price, p.stock_quantity, c.category_name
FROM Products p
JOIN Categories c ON p.category_id = c.category_id;
"""

cursor.execute(query)

print("Available Products:")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()