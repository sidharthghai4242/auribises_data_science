from food_customer import Customer
from food_order import Order
from food_dish import Dish

# Defining the dish menu
dish_menu = [
    Dish("Pasta", "D123", 4.5, 10.99, "Main Course"),
    Dish("Salad", "D124", 4.0, 5.99, "Appetizer"),
    Dish("Burger", "D126", 4.3, 8.99, "Main Course"),
    Dish("Soup", "D127", 4.2, 4.99, "Appetizer"),
    Dish("Steak", "D128", 4.7, 15.99, "Main Course"),
    Dish("Pizza", "D129", 4.6, 12.99, "Main Course"),
    Dish("Fries", "D130", 4.1, 3.99, "Side"),
    Dish("Ice Cream", "D131", 4.8, 6.49, "Dessert"),
    Dish("Sandwich", "D132", 4.4, 7.99, "Main Course"),
    Dish("Chicken Wings", "D133", 4.3, 9.99, "Appetizer"),
    Dish("Tacos", "D134", 4.5, 8.49, "Main Course"),
    Dish("Sushi", "D135", 4.9, 13.99, "Main Course"),
    Dish("Lasagna", "D136", 4.7, 11.99, "Main Course"),
    Dish("Garlic Bread", "D137", 4.0, 4.49, "Side"),
    Dish("Brownie", "D138", 4.6, 5.49, "Dessert")
]

# Defining customers
customer1 = Customer("C001", "John Doe", "john.doe@example.com", "123-456-7890")
customer2 = Customer("C002", "Jane Smith", "jane.smith@example.com", "234-567-8901")
customer3 = Customer("C003", "Emily Johnson", "emily.johnson@example.com", "345-678-9012")
customer4 = Customer("C004", "Michael Brown", "michael.brown@example.com", "456-789-0123")

# Creating orders
order1 = Order(customer1, "O001")
order1.add_dish(dish_menu[0])
order1.add_dish(dish_menu[2])
order1.add_dish(dish_menu[7])



order2 = Order(customer2, "O002")
order2.add_dish(dish_menu[1])
order2.add_dish(dish_menu[5])
order2.add_dish(dish_menu[4])

# Adding orders to customers
customer1.add_order(order1)
customer2.add_order(order2)

# Displaying customer info and order history
print("```````````````````````````````````````````````````````")
customer1.display_customer_info()
customer1.view_order_history()

print("```````````````````````````````````````````````````````")
customer2.display_customer_info()
customer2.view_order_history()

print("```````````````````````````````````````````````````````")