# CA2 - Car Dealership
# Student no. 10363676

# Associated test suite for classes in dealershipcars and dealership

import unittest

from dealershipcars import Car, PetrolCar, DieselCar, ElectricCar, HybridCar
from dealership import Dealership

# Test car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ford')
        self.assertEqual('Ford', self.car.getMake())

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('', self.car.getColour())
        
    def test_car_engineSize(self):
        self.assertEqual('', self.car.getengineSize())
        self.car.setengineSize('1.4')
        self.assertEqual('1.4', self.car.getengineSize())          

class TestPetrolCar(unittest.TestCase):
    
    def setUp(self):
        self.car = PetrolCar()
        
    def test_car_numberCylinders(self):
        self.assertEqual('', self.car.getNumberCylinders())
        self.car.setNumberCylinders('1')
        self.assertEqual('1', self.car.getNumberCylinders())
                      
class TestDieselCar(unittest.TestCase):
    
    def setUp(self):
        self.car = DieselCar()
        
    def test_car_numberCylinders(self):
        self.assertEqual('', self.car.getNumberCylinders())
        self.car.setNumberCylinders('1')
        self.assertEqual('1', self.car.getNumberCylinders())

class TestElectricCar(unittest.TestCase):
    
    def setUp(self):
        self.car = ElectricCar()
        
    def test_car_numberFuelCells(self):
        self.assertEqual('', self.car.getNumberFuelCells())
        self.car.setNumberFuelCells('370')
        self.assertEqual('370', self.car.getNumberFuelCells())
        
class TestHybridCar(unittest.TestCase):
    
    def setUp(self):
        self.car = HybridCar()
        
    def test_car_numberFuelCells(self):
        self.assertEqual('', self.car.getNumberFuelCells())
        self.car.setNumberFuelCells('370')
        self.assertEqual('370', self.car.getNumberFuelCells())

# Test dealership functionality
class TestDealership(unittest.TestCase):
    
    def setUp(self):
        self.electric_cars = [4]
        self.hybrid_cars = [8]
        self.petrol_cars = [20]
        self.diesel_cars = [8]
        self.car_list = [40]

    def test_available_stock(self):
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
  
if __name__ == '__main__':
    unittest.main()
