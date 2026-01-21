Instructions for Build and Use
Software Demo

📹 Demo Video:
(Insert your YouTube video link here)

Steps to Build and/or Run the Software

Ensure MySQL Server is running and accessible through MySQL Workbench.

In MySQL Workbench, run the database schema script:

schema.sql

Populate the database with sample data:

insert_data.sql

Install the required Python dependency:

pip3 install mysql-connector-python


Run the main application:

python3 app.py

Instructions for Using the Software

Once the menu appears:

Select 1 to list all products with prices, stock levels, and categories.

Select 2 to create a new order for an existing customer.

Select 3 to add items to an order (inventory stock is updated automatically).

Select 4 to view order totals per customer.

Select 5 to exit the application.

Development Environment

To recreate the development environment, you will need:

Python 3.9+

MySQL Server (local installation)

MySQL Workbench

Visual Studio Code (or another code editor)

mysql-connector-python (installed via pip)

Useful Websites to Learn More

The following resources were helpful during development:

MySQL Connector/Python Documentation
https://dev.mysql.com/doc/connector-python/en/

MySQL Workbench Documentation
https://dev.mysql.com/doc/workbench/en/

Future Work

Planned improvements and extensions for this project include:

 Adding user authentication and roles

 Implementing order deletion and modification

 Improving error handling and input validation

 Adding reporting features (daily sales, low inventory alerts)

 Refactoring into a web-based application