#In this file, we will take the 2 edges of a perpendicular triangle and calculate its hypotenuse.

x = int(input("Please enter first edge: "))
y = int(input("Please enter second edge: ")) 

# x^2 + y^2 = z^2 
z = ((x ** 2) + (y ** 2)) ** 0.5

print("Hypotenuse = {}".format(z))