from .models.customer import Customer
from .models.order import Order
from .models.base_model import Session

def main():
    session = Session()
    while True:
        menu()
        choice = input("> ")
        handle_choice(choice, session)

def menu():
    print("\nWelcome to Teketeke Delivery CLI!")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create Customer")
    print("2. Create Order")
    print("3. View All Customers")
    print("4. View Customer Orders")
    print("5. Delete Order")

def handle_choice(choice, session):
    """Handle user menu choice."""
    if choice == "0":
        exit_program()
    elif choice == "1":
        create_customer(session)
    elif choice == "2":
        create_order(session)
    elif choice == "3":
        view_all_customers(session)
    elif choice == "4":
        view_customer_orders(session)
    elif choice == "5":
        delete_order(session)
    else:
        print("Invalid choice. Please try again.")

def create_customer(session):
    name = input("Enter customer name: ")
    phone = input("Enter customer phone number: ")
    Customer.create(session, name, phone)
    print("Customer created successfully.")

def create_order(session):
    customer_id = input("Enter customer ID for the order: ")
    coffee_type = input("Enter coffee type (e.g., espresso, latte): ")
    size = input("Enter coffee size (small, medium, large): ")
    
    # Assuming there's a create method in the Order class
    Order.create(session, coffee_type, size, customer_id)
    print("Order created successfully.")

def view_all_customers(session):
    customers = Customer.get_all(session)
    if customers:
        for customer in customers:
            print(f"ID: {customer.id}, Name: {customer.name}, Phone: {customer.phone}")
    else:
        print("No customers found.")

def view_customer_orders(session):
    customer_id = input("Enter customer ID to view orders: ")
    customer = Customer.find_by_id(session, customer_id)
    
    if customer:
        if customer.orders:
            for order in customer.orders:
                print(f"Order ID: {order.id}, Coffee: {order.coffee_type}, Size: {order.size}")
        else:
            print("No orders found for this customer.")
    else:
        print("Customer not found.")

def delete_order(session):
    order_id = input("Enter order ID to delete: ")
    order = Order.find_by_id(session, order_id)
    
    if order:
        order.delete(session)
        print("Order deleted successfully.")
    else:
        print("Order not found.")

def exit_program():
    print("Kwaheri! Thank you for using the Teketeke Delivery CLI.")
    exit()

if __name__ == "__main__":
    main()
