# CA2 - Car Dealership
# Student no. 10363676

# Aungier Car Rental
# When cars are rented they are unavailable to customers, when cars are not rented they are 
# available to customers, and when cars are returned to the rental pool they become available 
# to customers again. When all 40 cars are unavailable the customer receives a notification that
# there are no cars available to rent. When a specific type of car e.g. petrol is no longer available
# the customer is notified that there are none available and that they can select a different type.
# This script is run by the dealership_app
 
from dealershipcars import Car, ElectricCar, HybridCar, PetrolCar, DieselCar

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.hybrid_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.car_list = []

    def available_stock(self): # Available stock
        for i in range(40):
            self.car_list.append(Car())
        for i in range(20):
            self.petrol_cars.append(PetrolCar())
        for i in range(8):
            self.diesel_cars.append(DieselCar())
        for i in range(4):
            self.electric_cars.append(ElectricCar())
        for i in range(8):
            self.hybrid_cars.append(HybridCar())

    def stock_count(self): # Lists all avaialble cars for the customer
        print 'Petrol cars in stock: ' + str(len(self.petrol_cars))
        print 'Diesel cars in stock: ' + str(len(self.diesel_cars))
        print 'Electric cars in stock: ' + str(len(self.electric_cars))
        print 'Hybrid cars in stock: ' + str(len(self.hybrid_cars))

    def rent(self, car_list, amount): # Defines how cars are rented/removed from availability
        if len(car_list) < amount: # If available car stock is zero a notification is sent.
            print 'Sorry not enough of type in stock - please select again.'
            return
        total = 0
        while total < amount: # Makes cars avaialble until amount requested = 0
           car_list.pop()
           total = total + 1
       
    def ret(self, car_list, amount): # Defines how cars are returned/made available
        total = 0
        while total < amount:
           car_list.append(Car())
           total = total + 1   
           
    def process_rental(self): # Adds and removed cars from availability
        answer = raw_input('Would you like to rent or return a car? rent/return: ')
        if answer == 'rent':
            self.stock_count()
            answer = raw_input('What type would you like? p/d/e/h: ')
            if answer == 'p':
                print 'Available petrol cars: ' + str(len(self.petrol_cars))
            if answer == 'd':
                print 'Available diesel cars: ' + str(len(self.diesel_cars))                
            if answer == 'e':
                print 'Available electric cars: ' + str(len(self.electric_cars))                
            if answer == 'h':
                print 'Available hybrid cars: ' + str(len(self.hybrid_cars))                                
         
            amount = int(raw_input('How many would you like? '))   
            if answer == 'p' and amount < (self.petrol_cars, amount):
                self.rent(self.petrol_cars, amount), self.rent(self.car_list, amount)
            if answer == 'd'and amount < (self.diesel_cars, amount):
                self.rent(self.diesel_cars, amount), self.rent(self.car_list, amount)
            if answer == 'e'and amount < (self.electric_cars, amount):
                self.rent(self.electric_cars, amount), self.rent(self.car_list, amount)
            if answer == 'h'and amount < (self.hybrid_cars, amount):
                self.rent(self.hybrid_cars, amount), self.rent(self.car_list, amount)

        if answer == 'return':
            answer = raw_input('What type are you returning? p/d/e/h: ')                              
            amount = int(raw_input('How many are you returning? '))
            if answer == 'p':
                self.ret(self.petrol_cars, amount), self.ret(self.car_list, amount)               
            if answer == 'd':
                self.ret(self.diesel_cars, amount), self.ret(self.car_list, amount) 
            if answer == 'e':
                self.ret(self.electric_cars, amount), self.ret(self.car_list, amount) 
            if answer == 'h':
                self.ret(self.hybrid_cars, amount), self.ret(self.car_list, amount) 
        self.stock_count()