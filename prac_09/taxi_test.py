from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)
my_taxi.drive(40)

print(my_taxi)
print("Current fare:", my_taxi.get_fare())

# Restart the meter and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# Print the details and the current fare
print(my_taxi)
print("Current fare:", my_taxi.get_fare())
