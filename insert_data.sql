USE inventory_orders_db;

-- Categories
INSERT INTO Categories (category_name) VALUES
('Electronics'),
('Clothing'),
('Home Goods');

-- Products
INSERT INTO Products (product_name, price, stock_quantity, category_id) VALUES
('Laptop', 999.99, 10, 1),
('Headphones', 199.99, 25, 1),
('T-Shirt', 19.99, 50, 2),
('Coffee Maker', 79.99, 15, 3);

-- Customers
INSERT INTO Customers (first_name, last_name, email) VALUES
('John', 'Doe', 'john.doe@email.com'),
('Jane', 'Smith', 'jane.smith@email.com');

-- Orders
INSERT INTO Orders (customer_id) VALUES
(1),
(2);

-- Order Items
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 3);