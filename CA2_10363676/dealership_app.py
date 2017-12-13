# CA2 - Car Dealership
# Student no. 10363676

# Aungier Car Rental Application
# This application runs the dealership scrip which allows Aungier Car Rental to manage their rental
# pool of 40 cars (50% petrol, 20% diesel, 10% electric, 20% hybrid).

from dealership import Dealership

dealership = Dealership()
dealership.available_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue? y/n: ')