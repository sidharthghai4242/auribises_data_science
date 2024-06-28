class Dish:

    def __init__(self,name,dish_id="000000000000",rating=0.0,price=0.0,category="Veg"):
        self.name=name
        self.dish_id=dish_id
        self.rating=rating
        self.price=price
        self.category=category
    
    def add_info_to_dish(self):
        print(">>>>> Enter Info to Dish")
        self.name = input("Please enter the name: ")
        self.dish_id = input("Please enter the dish ID: ")
        self.rating = float(input("Please enter the rating: "))
        self.price = float(input("Please enter the price: "))
        self.category = input("Please enter the category: ")
    
    def display_info(self):
        print(f"Dish Name: {self.name}")
        print(f"Dish ID: {self.dish_id}")
        print(f"Rating: {self.rating}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
