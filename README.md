Inventory & Orders Database (Module 1)

This project is a small inventory and order management system built with MySQL and Python.
It demonstrates relational database design (tables, keys, relationships) and real interaction with the database through a Python menu application.

Instructions for Build and Use

Software Demo

Steps to build and/or run the software:

Ensure MySQL Server is running and you can connect using MySQL Workbench.

Run the schema script in MySQL Workbench: schema.sql

Run the insert script in MySQL Workbench: insert_data.sql

Install the Python connector:

pip3 install mysql-connector-python

Run the menu app:

python3 app.py

Instructions for using the software:

Choose 1 to list products.

Choose 2 to create a new order for a customer.

Choose 3 to add an item to an order (updates stock too).

Choose 4 to display order totals.

Choose 5 to exit.

Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

Python 3.9+

MySQL Server (local)

MySQL Workbench

VS Code (or any editor)

mysql-connector-python (installed via pip)

Useful Websites to Learn More

I found these websites useful in developing this software:

MySQL Connector/Python Documentation: https://dev.mysql.com/doc/connector-python/en/

MySQL Workbench Documentation: https://dev.mysql.com/doc/workbench/en/

Future Work

The following items I plan to fix, improve, and/or add to this project in the future: