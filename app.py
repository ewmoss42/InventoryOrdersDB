import os
from dotenv import load_dotenv
import mysql.connector

# Load variables from .env file
load_dotenv()

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": os.getenv("DB_PASSWORD"),
    "database": "inventory_orders_db"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def list_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.product_id, p.product_name, p.price, p.stock_quantity, c.category_name
        FROM Products p
        JOIN Categories c ON p.category_id = c.category_id
        ORDER BY p.product_id;
    """)
    rows = cur.fetchall()
    print("\nProducts:")
    for r in rows:
        print(f"{r[0]}: {r[1]} | ${r[2]} | stock: {r[3]} | category: {r[4]}")
    cur.close()
    conn.close()

def list_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT customer_id, first_name, last_name FROM Customers ORDER BY customer_id;")
    rows = cur.fetchall()
    print("\nCustomers:")
    for r in rows:
        print(f"{r[0]}: {r[1]} {r[2]}")
    cur.close()
    conn.close()

def create_order():
    list_customers()
    customer_id = int(input("\nEnter customer_id to create an order for: "))

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Orders (customer_id) VALUES (%s);", (customer_id,))
    conn.commit()
    order_id = cur.lastrowid
    cur.close()
    conn.close()

    print(f"\n✅ Created Order #{order_id}")
    return order_id

def add_item_to_order():
    order_id = int(input("\nEnter order_id: "))
    list_products()

    product_id = int(input("\nEnter product_id: "))
    quantity = int(input("Enter quantity: "))

    conn = get_connection()
    cur = conn.cursor()

    # Check stock
    cur.execute("SELECT stock_quantity FROM Products WHERE product_id = %s;", (product_id,))
    row = cur.fetchone()
    if row is None:
        print("❌ Product not found.")
        cur.close()
        conn.close()
        return

    stock = row[0]
    if quantity <= 0:
        print("❌ Quantity must be > 0.")
        cur.close()
        conn.close()
        return
    if quantity > stock:
        print(f"❌ Not enough stock. Available: {stock}")
        cur.close()
        conn.close()
        return

    # Insert item (or update if already exists)
    try:
        cur.execute(
            "INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (%s, %s, %s);",
            (order_id, product_id, quantity)
        )
    except mysql.connector.Error as e:
        # Duplicate product in same order -> increase quantity
        if e.errno == 1062:
            cur.execute(
                "UPDATE OrderItems SET quantity = quantity + %s WHERE order_id = %s AND product_id = %s;",
                (quantity, order_id, product_id)
            )
        else:
            raise

    # Reduce stock
    cur.execute(
        "UPDATE Products SET stock_quantity = stock_quantity - %s WHERE product_id = %s;",
        (quantity, product_id)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("\n✅ Item added to order and stock updated.")

def show_order_totals():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
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
    """)
    rows = cur.fetchall()
    print("\nOrder Totals:")
    for r in rows:
        print(f"Order {r[0]} | {r[1]} | Total: ${r[2]}")
    cur.close()
    conn.close()

def main():
    if not DB_CONFIG["password"]:
        print("❌ DB_PASSWORD not found. Create a .env file with DB_PASSWORD=yourpassword")
        return

    while True:
        print("\n=== Inventory & Orders Menu ===")
        print("1) List products")
        print("2) Create new order")
        print("3) Add item to an order")
        print("4) Show order totals")
        print("5) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_products()
        elif choice == "2":
            create_order()
        elif choice == "3":
            add_item_to_order()
        elif choice == "4":
            show_order_totals()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()