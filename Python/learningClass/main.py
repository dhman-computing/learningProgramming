class car:
    petrol = 100 # It represent the price of petrol in rupees
    discount = 10 # this is the default discount that can be given to a car
    cars = []

    def __init__(self, model: str, top_speed: float, milage: float, price: float):
        ## This initializes the object of class car

        # Checks if the inputs are given in correct manner
        # assert (top_speed > 0 & milage > 0 & price > 0), f"The attributes given to create an object of class Car is not in correct manner."

        # Istance atributes of an object created from class car
        self.model = model
        self.top_speed = top_speed
        self.milage = milage
        self.price = price

        #Creating a list of available cars
        car.cars.append(self)

    def perKmCost(self):
        #calculates the operating cost of a car per kilometer

        return car.petrol / self.milage
    
    def costAfterDiscount(self):
        # gives the cost of the car after discount

        return self.price * (100 - self.discount)
    
    def __repr__(self):
        return f"{self.model}"

