# CA1 Student no. 10363676
# Scientific Calculator to call functions from 'calc.py' calculator program.

from Tkinter import *
from calculator import Calculator

SciCal = Calculator()

num = SciCal.number_input()

if len(num) == 1:#if list length = 1
    print SciCal.op1(num[0])#run operation one, which will offer sin, cos, and tan, on first index (in this case, the only index)
else: 
    print SciCal.op2(num[0],num[1]) #if list is longer than 1, run op2 function on first and second index