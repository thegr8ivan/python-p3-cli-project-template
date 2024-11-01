# Teketeke Coffee Delivery CLI

Teketeke is a CLI application for managing coffee delivery orders. With Teketeke, users can create, view, and delete orders, browse products, and manage customer information, all through a simple, text-based interface.

## Features

- Order Management: Create, delete, view all orders, and search for orders by ID.
- Product Listing: Browse the available coffee products.
- Customer Management: Add, delete, view all customers, and search for a customer by ID.

## Getting Started


### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/thegr8ivan/teketeke-coffee-delivery.git

Running the CLI
Start the CLI using python lib/cli.py

## Project Structure

1. lib/cli.py: Main CLI script where users can navigate options to manage orders, products, and customers.
2. lib/models: Contains the model definitions for the database:
 .Order.py: Defines attributes and methods for coffee orders.
 .Product.py: Defines product information, such as product name, description, and price.
 .Customer.py: Defines customer details like name, address, and contact information.
3. lib/helpers.py: Includes helper functions for CLI interaction (menus, validations, etc.).
4. Pipfile: Lists the dependencies used in the project.

### CLI Commands and options
In the CLI main menu, you have several options to choose from:

1 - Create a new order
2 - Delete an order
3 - View all orders
4 - Search for an order by ID
5 - View available products
6 - Manage customers
0 - Exit the application

### Creating new Order

To create a new order:

Start the CLI with python lib/cli.py.
Select option 1 to create a new order.
Enter the required details (product selection, customer details, etc.) as prompted.
## Viewing All orders

Select option 3 to view all existing orders, with details like order ID, product, quantity, and customer information.

