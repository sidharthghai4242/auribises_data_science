class FlightBooking:
    # default constructor 
    # self is refrence variable that holds hashcode of the object
    
    def __init__(self):
        self.fromLocaton="Delhi"
        self.toLocation="Bengaluru"
        self.travelDate="17-06-2024"
        self.numberoftravellers= 1
        self.travelClass="Economy"
    
    def __init__(self,fromLocaton,toLocation,travelDate,numberoftravellers,travelClass):
        self.fromLocaton=fromLocaton
        self.toLocation=toLocation
        self.travelDate=travelDate
        self.numberoftravellers= numberoftravellers
        self.travelClass=travelClass
    
    def show(self):
        print("Booking data")
        print("FROM:-",self.fromLocaton," || ","TO:-",self.toLocation)

booking1=FlightBooking("New Delhi","chandigarh","18-06-2024",1,"economy")
print(booking1)
print(vars(booking1))

# Throws error
# booking3=FlightBooking()


booking2=FlightBooking("chennai","chandigarh","18-06-2024",3,"economy")
print(booking2)
print(vars(booking2))

booking1.show()