# CA1 Student no. 10363676
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

    def number_input(self):
        valid_input = False
        while not valid_input:  
            try: 
                numb_input = raw_input('Enter up to two numbers to calculate, leave space between numbers: ')
                numbers = list(map(float,numb_input.split())) #take up to two numbers, use the map function to loop over the strings and turn them into intergers, split them at the space, and add to a list
                valid_input = True #once the entry has made it through the except shield, continue to next step
                return numbers
            except:
                print 'Please enter a valid number.'
                

    def op2(self,x,y): #A function has a definitive number of parameters. Need two functions to cover one and two-number inputs.
        valid_input = False
        while not valid_input: 
            try:
                op = int(raw_input(
                "Which operation would you like to use?: \n"
                "[1] Enter 1 for addition. \n"
                "[2] Enter 2 for subtraction. \n"
                "[3] Enter 3 for multiplication. \n"
                "[4] Enter 4 for division. \n"  
                "[5] Enter 5 for exponential. \n"
                ))
                if op < 0 or op > 5:
                    return ('Please enter number in range 1 to 5.')
                    valid_input = True
                elif op == 1: 
                    return self.add(x,y)
                elif op == 2: 
                    return self.subtract(x,y)
                elif op == 3: 
                    return self.multiply(x,y)
                elif op == 4:
                    return self.divide(x,y)
                elif op == 5: 
                    return self.exponent(x,y)
                valid_input = True
            except: 
                print 'Please enter a valid number.'
    
    def op1(self, x):
        valid_input = False
        while not valid_input: 
            try:
                op = int(raw_input(
                "Which operation would you like to use?: \n"
                "[1] Enter 1 for sin. \n"
                "[2] Enter 2 for cos. \n"
                "[3] Enter 3 for tan. \n"
                "[4] Enter 4 for square root. \n"
                "[5] Enter 5 for square. \n"
                "[6] Enter 6 for cube. \n"
                ))
                if op < 0 or op > 6:
                    return ('Please enter number in range 1 to 6.')
                    valid_input = True
                elif op == 1:
                    return self.sin(x)
                elif op == 2:
                    return self.cos(x)
                elif op == 3:
                    return self.tan(x)
                elif op == 4:
                    return self.squareroot(x)
                elif op == 5:
                    return self.square(x)
                elif op == 6:
                    return self.cube(x)
            except: 
                print 'Please enter a valid number.'               

