from main import *

car1 = car('suv', 170, 20, 2000000)
car2 = car('compact', 150, 35, 1000000)
car3 = car('sedan', 190, 25, 1500000)
car4 = car('sports', 250, 15, 5000000)
car5 = car('truck', 130, 27, 1200000)

# car1.model = "SUV"
# car2.model = "Compact"


#print(type(car1))
#print(type(car2))
for item in car.cars:
    print(item.model)
print()
for item in car.cars:
    print(item.top_speed)
print()
for item in car.cars:
    print(item.milage)
print()
for item in car.cars:
    print(item.price)
print()
for item in car.cars:
    print(item.perKmCost())
print()
for item in car.cars:
    print(item.costAfterDiscount())
print()
print(car.cars)