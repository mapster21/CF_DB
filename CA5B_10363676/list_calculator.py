# 11 common functions found on a scientific calculator.
# Functions  handle lists
from Tkinter import *
import math

class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
    
    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)
    
    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())
    
    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

# Calculates functions within the 'Calc_App.py' GUI.            
    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "cos":
            self.total = math.cos(math.radians(self.total))
        if self.op == "divide":
            self.total /= self.current
        if self.op == "exponent":
           self.total = math.exp(self.total)
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "sin":
            self.total=math.sin(math.radians(self.total))
        if self.op == "square":
            self.total = self.total * self.total
        if self.op == "squareroot":
            self.total = self.total ** (0.5)  
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
        
    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True
    
    def all_clear(self):
        self.clear()
        self.total = 0
    
    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calculator()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(calc, justify=RIGHT,width=30,font="Times 16 bold")
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "0")

# Calculator Design - Button layout and function calls
numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
        bttn[i]["bg"]= "ghost white"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0",bg="ghost white")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 0, padx= 1, pady = 1)

add = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+",bg="light steel blue")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3,  padx=1, pady = 1)

cos = Button(calc, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "light sea green")
cos["command"]=lambda: sum1.operation("cos")
cos.grid(row=5,column=1,padx=1,pady=1)

divide = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/",bg="light steel blue")
divide["command"] = lambda: sum1.operation("divide")
divide.grid(row = 1, column = 3, padx=1, pady = 1)

exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='exp', bg="light sea green")
exponent["command"]=lambda: sum1.operation("exponent")
exponent.grid(row=5,column=3,padx=1,pady=1)

multiply = Button(calc,height =2,width=4,padx=10, pady = 10, text = "*",bg="light steel blue")
multiply["command"] = lambda: sum1.operation("multiply")
multiply.grid(row = 2, column = 3,  padx=1, pady = 1)

sin = Button(calc, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "light sea green")
sin["command"]=lambda: sum1.operation("sin")
sin.grid(row=5,column=0,padx=1,pady=1)

square = Button(calc, height=2, width=4, padx=10, pady=10, text="sq", bg = "light sea green")
square["command"] = lambda: sum1.operation("square")
square.grid(row=3, column=4, padx=1, pady=1)

squareroot = Button(calc, height=2, width=4, padx=10, pady=10, text="sqrt", bg = "light sea green")
squareroot["command"] = lambda: sum1.operation("squareroot")
squareroot.grid(row=4, column=4, padx=1, pady=1)

subtract = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-",bg="light steel blue")
subtract["command"] = lambda: sum1.operation("subtract")
subtract.grid(row = 3, column = 3, padx=1, pady = 1)

tan = Button(calc, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "light sea green")
tan["command"]=lambda: sum1.operation("tan")
tan.grid(row=5,column=2,padx=1,pady=1)

point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".",bg="white")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 1, padx=1, pady = 1)

neg= Button(calc,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="white")
neg["command"] = sum1.sign
neg.grid(row = 4, column = 2,  padx=1, pady = 1)

clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C",bg="white")
clear["command"] = sum1.clear
clear.grid(row = 1, column = 4,  padx=1, pady = 1)

all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC",bg="white")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 2, column = 4, padx=1, pady = 1)

equals = Button(calc,height = 2,width=4,padx=10, pady = 10, text = "=",bg="light sea green")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 4, padx=1, pady = 1)

root.mainloop()