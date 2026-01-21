import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "W35tW00d",
    "database": "inventory_orders_db"
}

def main():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    # Show customers
    cursor.execute("SELECT customer_id, first_name, last_name FROM Customers;")
    customers = cursor.fetchall()

    print("Customers:")
    for c in customers:
        print(f"{c[0]}: {c[1]} {c[2]}")

    customer_id = int(input("\nEnter customer_id to create an order for: "))

    # Create a new order
    cursor.execute("INSERT INTO Orders (customer_id) VALUES (%s);", (customer_id,))
    connection.commit()

    new_order_id = cursor.lastrowid
    print(f"\n✅ Created Order #{new_order_id} for customer_id {customer_id}")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()