# 11 common functions found on a scientific calculator.
# These calculator functions are tested in the 'test_calculator.py' testsuite.

class Calculator(object):
 
# Function adds integer, float, or complex numbers.
    def add(self, x, y):
        number_types = (int, float, complex)      
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError


# Function calculates the trigonometric cosine function for integer, float, or complex numbers.
# Cos values are returned rounded to 3 decimal places.            
    def cos(self, x):
        import math
        number_types = (int, float, complex)  
        y = math.cos(math.radians(x))
        if isinstance(x, number_types) and isinstance(y, number_types):
            return round (y, 3)
        else:
            raise ValueError

# Function cubes integer, float, or complex numbers.
# Cubed results are returned rounded to 3 decimal places.            
    def cube(self, x):
        number_types = (int, float, complex)  
        y = x * x * x
        if isinstance(x, number_types) and isinstance(y, number_types):
            return round (y, 3)
        else:
            raise ValueError
            
# Function divides integer, float, or complex numbers.
# Dividing by zero returns 'nan' - not a number.            
    def divide(self, x, y):
        if y == 0:
            return 'nan'
        number_types = (int, float, complex)        
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x / float(y)
        else:
            raise ValueError    

# Function calculates the exponent for integer, float, or complex numbers.    
    def exponent(self, x, y):
        number_types = (int, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x ** y
        else:
            raise ValueError

# Function multiplies integer, float, or complex numbers.       
    def multiply(self, x, y):
        number_types = (int, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError

# Function calculates the trigonometric sine function for integer, float, or complex numbers.
# Sine values are returned rounded to 3 decimal places.            
    def sin(self, x):
        import math
        number_types = (int, float, complex) 
        y = math.sin(math.radians(x))
        if isinstance(x, number_types) and isinstance(y, number_types):
            return round(y, 3)
        else:
            raise ValueError 
    
# Function squares integer, float, or complex numbers.
# Square results are returned rounded to 3 decimal places.            
    def square(self,x):
        number_types = (int, float, complex)
        y = x * x
        if isinstance(x, number_types):
            return round(y, 3)
        else:
            raise ValueError

# Function calculates the squart root of integer, float, or complex numbers.
# Square root values are returned rounded to 3 decimal places.           
    def squareroot(self, x):
        number_types = (int, float, complex)         
        y = x ** (0.5)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return round (y, 3)
        else:
            raise ValueError  
    
# Function subtracts integer, float, or complex numbers.
    def subtract(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError 
            
# Function calculates the trigonometric tangent function for integer, float, or complex numbers.           
    def tan(self, x): 
        import math
        number_types = (int, float, complex)
        y = math.tan(math.radians(x))
        if isinstance(x, number_types) and isinstance(y, number_types):
            return y
        else:
            raise ValueError    

# Calculates functions within the 'Calc_App.py' GUI.            
    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "cos":
            self.total = math.cos(math.radians(self.total))
        # cube?
        if self.op == "divide":
            self.total /= self.current
        if self.op == "exponent":
           self.total = math.exp(self.total)
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "sin":
            self.total=math.sin(math.radians(self.total))
        if self.op == "square":
            self.total = self.total ** self.total
        if self.op == "squareroot":
            self.total = self.total ** (1/self.current)
        if self.op == "subtract":
            self.total -= self.current
        if self.op == "tan":
            self.total = math.tan(math.radians(self.total))
        self.new_num = True
        self.op_pending = False
        self.display(self.total)
        
    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False
  