# Declaring the total number of cars.
cars = 100
# Declaring the space in each car.
space_in_a_car = 4.0
# Declaring the number of drivers available.
drivers = 30
# Declaring the number of passengers.
passengers = 90
# Calculating the number of cars that will not have drivers.
cars_not_driven = cars - drivers
# Calculating the number of cars that have drivers.
cars_driven = drivers
# Calculating the total number of passengers that can be transported.
carpool_capacity = cars_driven * space_in_a_car
# Calculating the average number of passengers in each car.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")