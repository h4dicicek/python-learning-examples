# In this file, we will get a shape type and lengths from user. And calculate is what type of them shape. 

# First, we have to know which shape calculate.

from operator import indexOf
from random import seed
from re import A


print("""
______________________
                      
PRESS 1 FOR TRIANGLE  
                      
PRESS 2 FOR RECTANGLE 
______________________
""")

selected_shape =  int(input("Please enter a number: "))

if ( selected_shape == 1):

    print("Triangle selected by user. Please enter the triangle lengths in the order from small to large.")
    x = int(input("Please enter first edge: "))
    y = int(input("Please enter second edge: "))
    z = int(input("Please enter third edge: "))
    
    #We have to use abs to obtain its absolute value.
    print("Your triangle edge lenghts: {} , {} , {}".format(abs(x),abs(y),abs(z)))
    
    if((x == y and y != z) or (y == z and z != x) or (x == z and z != y)):
        print("Your shape is Isosceles Triangle.")
    
    elif(x == y and y == z):
        print("Your shape is Equilateral Triangle.")
    
    else:
        print("Your shape is normal triangle :).")

elif( selected_shape == 2):

    print("Rectangle selected by user.")

    a = int(input("Please enter first edge: "))
    b = int(input("Please enter second edge: "))
    c = int(input("Please enter third edge: "))
    d = int(input("Please enter fourth edge: "))

    #We have to use abs to obtain its absolute value.
    print("Your rectangle edge lenghts: {} , {} , {} , {}".format(abs(a),abs(b),abs(c),abs(d)))

    if(a == b and b == c and c == d ):
        print("Your shape is Square.")
    elif((a == b and c == d and b != c) or (b == c and a == d and b != a) or (b == d and c == a and b != c)):
        print("Your shape rectangle :).")
    else:
        print("Your shape is normal rectangle :|.")

else:
    print("Shape type not found!")