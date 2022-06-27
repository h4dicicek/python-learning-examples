#In this file we create calculator with math module.

#we have to import math module to use methods in module.

import math

# We have to create table of operations.

print("""
___________________________________________

Operations:

Press 1 for add

Press 2 for subtract 

Press 3 for divide 

Press 4 for multiply

Press 5 for absolute value

Press 6 for factorial

Press 7 for gcd

Press 8 for logarithm

Press 9 for x^y

Press 10 for squareroot

Press 11 for to change radian to degrees

Press 12 for to change degrees to radian

Press 13 for calculate sin value in radian

Press 14 for calculate cos value in radian

Press 15 for calculate tan value in radian

PRESS ANOTHER NUMBER FOR QUIT
___________________________________________

""")


operation = int(input("Please enter a number for select operation: "))

while True:
    if (operation == 1):
        x = float(input("Please enter a number: "))
        y = float(input("Please enter a number: "))
        print("{} + {} = {}".format(x,y,x+y))
    
    elif (operation == 2):
        x = float(input("Please enter a number: "))
        y = float(input("Please enter a number: "))
        print("{} - {} = {}".format(x,y,x-y))
