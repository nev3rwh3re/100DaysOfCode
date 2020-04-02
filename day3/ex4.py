# number of cars
cars = 100
# number of people that can go into each car
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# cars that will not be driven
cars_not_driven = cars - drivers
# cars that will be driven, i.e. have a driver
cars_driven = drivers
# the capacity of the carpool
carpool_capacity = cars_driven + space_in_a_car
# the average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# the end
