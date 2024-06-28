class Dish:
    def __init__(self, name, price, description, ingredients, dietary_restrictions, calories, prep_time):
        self.name = name
        self.price = price
        self.description = description
        self.ingredients = ingredients
        self.dietary_restrictions = dietary_restrictions
        self.calories = calories
        self.prep_time = prep_time
        

    def __str__(self):
        return (f"{self.name} - ${self.price}\n"
                f"{self.description}\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Dietary Restrictions: {', '.join(self.dietary_restrictions)}\n"
                f"Calories: {self.calories} kcal\n"
                f"Preparation Time: {self.prep_time} minutes")

class Menu:
    def __init__(self):
        self.categories = {}

    def add_dish(self, category, dish):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(dish)

    def remove_dish(self, category, dish_name):
        if category in self.categories:
            self.categories[category] = [dish for dish in self.categories[category] if dish.name != dish_name]

    def get_dishes_by_category(self, category):
        return self.categories.get(category, [])

    def __str__(self):
        menu_str = ""
        for category, dishes in self.categories.items():
            menu_str += f"{category}:\n"
            for dish in dishes:
                menu_str += f"  {dish}\n"
        return menu_str

class Restaurant:
    def __init__(self, name, address, phone_number, opening_hours):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.opening_hours = opening_hours
        self.menu = Menu()

    def add_dish_to_menu(self, category, dish):
        self.menu.add_dish(category, dish)

    def remove_dish_from_menu(self, category, dish_name):
        self.menu.remove_dish(category, dish_name)

    def get_all_dishes(self):
        all_dishes = []
        for category in self.menu.categories:
            all_dishes.extend(self.menu.get_dishes_by_category(category))
        return all_dishes

    def __str__(self):
        return (f"{self.name}\n"
                f"{self.address}\n"
                f"Phone: {self.phone_number}\n"
                f"Opening Hours: {self.opening_hours}\n\n"
                f"Menu:\n{self.menu}")

# Example usage:
restaurant = Restaurant("The Great Eatery", "123 Food Lane", "123-456-7890", "9 AM - 10 PM")
dish1 = Dish("Spaghetti Carbonara", 12.99, "Classic Italian pasta dish with creamy sauce.",
             ["Pasta", "Eggs", "Cheese", "Pancetta"], ["Gluten", "Dairy"], 850, 20)
dish2 = Dish("Caesar Salad", 8.99, "Fresh romaine lettuce with Caesar dressing.",
             ["Lettuce", "Croutons", "Parmesan cheese", "Caesar dressing"], ["Dairy"], 350, 10)

restaurant.add_dish_to_menu("Main Courses", dish1)
restaurant.add_dish_to_menu("Appetizers", dish2)

print(restaurant)
