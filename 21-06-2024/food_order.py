from food_customer import Customer
from food_dish import Dish

class Order:
    def __init__(self, customer=None, order_id="00000000", dishes=None):
        self.customer = customer
        self.order_id = order_id
        self.dishes = dishes if dishes is not None else []
    
    def add_dish(self, dish):
        self.dishes.append(dish)
        print(f"Added {dish.name} to the order.")
    
    def remove_dish(self, dish_id):
        for dish in self.dishes:
            if dish.dish_id == dish_id:
                self.dishes.remove(dish)
                print(f"Removed {dish.name} from the order.")
                return
        print(f"Dish with ID {dish_id} not found in the order.")
    
    def display_order(self):
        if not self.dishes:
            print("The order is empty.")
            return
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name if self.customer else 'No customer assigned'}")
        print("Order details:")
        for dish in self.dishes:
            dish.display_info()
            print("----")
    
    def calculate_total(self):
        total = sum(dish.price for dish in self.dishes)
        print(f"Total price: ${total:.2f}")
        return total

# Example usage:
if __name__ == "__main__":
    # Create customer
    # customer = Customer("C001", "John Doe", "john.doe@example.com", "123-456-7890")

    # Create dishes
    dish1 = Dish("Pasta", "D123", 4.5, 10.99, "Main Course")
    dish2 = Dish("Salad", "D124", 4.0, 5.99, "Appetizer")
    dish3 = Dish("Burger", "D126", 4.3, 8.99, "Main Course")

    dishes=[dish1,dish2,dish3]
    
    
    def bubble_sort(data):
        for i in range(len(data)):
            for j in range(len(data)-i-1):
                if data[j].rating > data[j+1].rating:
                    temp=data[j+1]
                    data[j+1]=data[j]
                    data[j]=temp
        
     
    bubble_sort(dishes)
    
    # for dish in dishes:
    #     dish.display_info()


    # Create order and add dishes
    # order1 = Order(customer, "O001")
    # order1.add_dish(dish1)
    # order1.add_dish(dish2)
    # order1.add_dish(dish3)

    # Add order to customer
    # customer.add_order(order1)

    # # Display customer and order details
    # customer.display_customer_info()
    # customer.view_order_history()
