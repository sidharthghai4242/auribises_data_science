class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print(f"Order added for customer {self.name}")

    def display_customer_info(self):
        print(f"Customer ID: {self.customer_id}"," || ",f"Name: {self.name}"," || ",f"Email: {self.email}"," || ",f"Phone: {self.phone}")
        

    def view_order_history(self):
        if not self.orders:
            print("No orders found for this customer.")
            return
        print(f"Order history for {self.name}:")
        for idx, order in enumerate(self.orders, start=1):
            print(f"Order {idx}:")
            order.display_order()
            print("----")

# # Example usage:
# customer = Customer("C001", "John Doe", "john.doe@example.com", "123-456-7890")

# order1 = Order()
# dish1 = Dish("Pasta", "D123", 4.5, 10.99, "Main Course")
# dish2 = Dish("Salad", "D124", 4.0, 5.99, "Appetizer")
# order1.add_dish(dish1)
# order1.add_dish(dish2)

# order2 = Order()
# dish3 = Dish("Burger", "D126", 4.3, 8.99, "Main Course")
# order2.add_dish(dish3)

# customer.add_order(order1)
# customer.add_order(order2)

# customer.display_customer_info()
# customer.view_order_history()
