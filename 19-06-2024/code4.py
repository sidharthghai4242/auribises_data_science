class Driver:
    def __init__(self, name, license_number, rating=0, experience=0):
        self.name = name
        self.license_number = license_number
        self.vehicle = Vehicle()
        self.vehicle.add_vehicle_info()
        self.rating = rating
        self.experience = experience

    def __str__(self):
        return (f"{self.name},\n"
                f"\t Vehicle: {self.vehicle}"
                )


class Vehicle: # 1 to 1 
    def __init__(self, make="NA", model="NA", year="NA", license_plate="NA", capacity="NA"):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.capacity = capacity
    
    def add_vehicle_info(self):
        self.make = input("Enter vehicle brand:- ")
        self.model = input("Enter vehicle model:- ")
        self.year = input("Enter vehicle manufacture year:- ")
        self.license_plate = input("Enter vehicle license number:- ")
        self.capacity = input("Enter vehicle capacity:- ")
    
    def __str__(self):
        return (f"{self.make} - {self.model}")



class Customer:
    def __init__(self, name, contact_number, rating=0, ride_history=None):
        if ride_history is None:
            ride_history = []
        self.name = name
        self.contact_number = contact_number
        self.rating = rating
        self.ride_history = ride_history  # This should be a list of Ride objects

    def __str__(self):
        # Basic details
        result = f"Customer Name: {self.name}\nContact Number: {self.contact_number}\nRating: {self.rating}\n"
        
        # Ride history summary
        result += "Ride History:\n"
        if self.ride_history:
            for ride in self.ride_history:
                result += f" - {ride}\n"
        else:
            result += "No rides taken yet.\n"
        
        return result        

class Ride:
    def __init__(self, customer, driver, pickup_location, dropoff_location, fare, status='requested'):
        self.customer = customer  # This should be a Customer object
        self.driver = driver  # This should be a Driver object
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.fare = fare
        self.status = status

    def __str__(self):
        return (f"Driver: {self.driver}, "
                f"Pickup: {self.pickup_location}, "
                f"Pickup: {self.pickup_location}, "
                f"Dropoff: {self.dropoff_location}, "
                f"Fare: ${self.fare:.2f}, "
                f"Status: {self.status}")



# vehicle1 = Vehicle(make='Toyota', model='Camry', year=2020, license_plate='ABC123', capacity=4)

# vehicle2=Vehicle()

# vehicle2.add_vehicle_info()

driver1 = Driver(name='John Doe', license_number='D1234567', rating=4.9, experience=5)

customer1 = Customer(name='Jane Smith', contact_number='555-1234', rating=4.8)

ride1 = Ride(customer=customer1, driver=driver1, pickup_location='123 Main St', dropoff_location='456 Elm St', fare=25.50)

customer1.ride_history.append(ride1)

print(customer1)
