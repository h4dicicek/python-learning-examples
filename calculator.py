#In this file we create calculator with math module.

#we have to import math module to use methods in module.

from cgi import print_environ
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
    
    elif (operation == 3):
        x = float(input("Please enter a number: "))
        y = float(input("Please enter a number: "))
        print("{} x {} = {}".format(x,y,x*y))

    elif (operation == 4):
        x = float(input("Please enter a number: "))
        y = float(input("Please enter a number: "))
        print("{} ÷ {} = {}".format(x,y,x/y))

    elif (operation == 5):
        x = int(input("Please enter a number: "))
        print(math.fabs(x))

    elif (operation == 6):
        x = int(input("Please enter a number: "))
        print(math.factorial(x))
    
    elif (operation == 7):
        x = int(input("Please enter a number: "))
        y = int(input("Please enter a number: "))
        print(math.gcd(x,y))
    
    elif (operation == 8):
        x = int(input("Please enter a number: "))
        print(math.log10(x))

    elif (operation == 9):
        x = int(input("Please enter a number: "))
        y = int(input("Please enter a number: "))
        print(math.pow(x,y))
    
    elif (operation == 10):
        x = int(input("Please enter a number: "))
        print(math.sqrt(x))
    
    elif (operation == 11):
        x = float(input("Please enter a number: "))
        print(math.degrees(x))

    elif (operation == 12):
        x = float(input("Please enter a number: "))
        print(math.radians(x))
    
    elif (operation == 13):
        x = float(input("Please enter a number: "))
        print(math.sin(math.radians(x)))

    elif (operation == 14):
        x = float(input("Please enter a number: "))
        print(math.cos(math.radians(x)))