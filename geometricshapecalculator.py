# In this file, we will get a shape type and lengths from user. And calculate is what type of them shape. 

# First, we have to know which shape calculate.

from operator import indexOf


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
        print("Your triangle is Isosceles Triangle.")
    elif(x == y and y == z):
        print("Your triangle is Equilateral Triangle.")
    else:
        print("Your triangle is normal triangle :).")