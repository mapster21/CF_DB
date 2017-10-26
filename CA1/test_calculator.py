# Testsuites for 11 functions that one would expect to find on a scientific calculator. 
# Calculator functions being tested are held in 'calc.py' calculator class.

from calc import Calculator
import unittest

class TestCalculator(unittest.TestCase):

# Test calculators addition function    
    def test_calculator_add(self):
        result = Calculator().add(5,5)
        self.assertEqual(10, result)
        result = Calculator().add(2,3)
        self.assertEqual(5, result)
        result = Calculator().add(2,0)
        self.assertEqual(2, result)
        # Test for an attempt to add string values
        try:
            Calculator().add('2', '5')
            self.fail('should have thrown error')
        except ValueError:
            pass

# Test calculators trigonometric cosine function          
    def test_calculator_cos(self):
        result = Calculator().cos(90)
        self.assertEqual(0, result)      
        result = Calculator().cos(45)
        self.assertEqual(0.707, result) 
        result = Calculator().cos(0)
        self.assertEqual(1, result)
        result = Calculator().cos(360)
        self.assertEqual(1, result)
        result = Calculator().cos(1)
        self.assertEqual(1, result)

# Test calculators cube function
    def test_calculator_cube(self):
        result = Calculator().cube(2)
        self.assertEqual(8, result)      
        result = Calculator().cube(0)
        self.assertEqual(0, result) 
        result = Calculator().cube(1)
        self.assertEqual(1, result) 
        result = Calculator().cube(0.25)
        self.assertEqual(0.016, result)

# Test calculators divide function
    def test_calculator_divide(self):
        result = Calculator().divide(5,5)
        self.assertEqual(1, result)
        result = Calculator().divide(5,1)
        self.assertEqual(5, result)
        result = Calculator().divide(5,0.2)
        self.assertEqual(25, result)
        result = Calculator().divide(5,4)
        self.assertEqual(1.25, result)
        result = Calculator().divide(5,0)
        self.assertEqual('nan', result)
        # Test for an attempt to divide string values
        try:
            Calculator().divide('5', '5')
            self.fail('should have thrown error')
        except ValueError:
            pass 

# Test calculators exponent function
    def test_calculator_exponent(self):
        result = Calculator().exponent(2, 2)
        self.assertEqual(4, result)
        result = Calculator().exponent(2,4)
        self.assertEqual(16, result)
        result = Calculator().exponent(2, -2)
        self.assertEqual(0.25, result)
        result = Calculator().exponent(2, 0)
        self.assertEqual(1, result)

# Test calculators multiplication function     
    def test_calculator_multiply(self):
        result = Calculator().multiply(5,5)
        self.assertEqual(25, result)      
        result = Calculator().multiply(5,0)
        self.assertEqual(0, result) 
        result = Calculator().multiply(5,1)
        self.assertEqual(5, result) 
        result = Calculator().multiply(5,0.2)
        self.assertEqual(1, result)
        # Test for an attempt to multiply string values
        try:
            Calculator().multiply('2', '5')
            self.fail('should have thrown error')
        except ValueError:
            pass        

# Test calculators trigonometric sine function        
    def test_calculator_sin(self):
        result = Calculator().sin(90)
        self.assertEqual(1, result)      
        result = Calculator().sin(45)
        self.assertEqual(0.707, result) 
        result = Calculator().sin(0)
        self.assertEqual(0, result)
        result = Calculator().sin(360)
        self.assertEqual(0, result)
        result = Calculator().sin(1)
        self.assertEqual(0.017, result)

# Test calculators square function
    def test_calculator_square(self):
        result = Calculator().square(2)
        self.assertEqual(4, result)      
        result = Calculator().square(0)
        self.assertEqual(0, result) 
        result = Calculator().square(1)
        self.assertEqual(1, result) 
        result = Calculator().square(0.883)
        self.assertEqual(0.78, result)

# Test calculators square root function
    def test_calculator_squareroot(self):
        result = Calculator().squareroot(16)
        self.assertEqual(4, result)      
        result = Calculator().squareroot(0)
        self.assertEqual(0, result) 
        result = Calculator().squareroot(1)
        self.assertEqual(1, result) 
        result = Calculator().squareroot(0.2)
        self.assertEqual(0.447, result) 

# Test calculators subtraction function    
    def test_calculator_subtract(self):
        result = Calculator().subtract(5,5)
        self.assertEqual(0, result)
        result = Calculator().subtract(5,3)
        self.assertEqual(2, result)
        result = Calculator().subtract(3,5)
        self.assertEqual(-2, result)
        # Test for an attempt to subtract string values
        try:
            Calculator().subtract('5', '3')
            self.fail('should have thrown error')
        except ValueError:
            pass 

# Test calculators trigonometric tangent function
    def test_calculator_tan(self):
        result = Calculator().tan(90)
        self.assertEqual(1.633123935319537e+16, result)      
        result = Calculator().tan(45)
        self.assertEqual(0.9999999999999999, result) 
        result = Calculator().tan(0)
        self.assertEqual(0, result)
        result = Calculator().tan(360)
        self.assertEqual(-2.4492935982947064e-16, result)
        result = Calculator().tan(1)
        self.assertEqual(0.017455064928217585, result)
            
if __name__ == '__main__':
    unittest.main()

    

 


