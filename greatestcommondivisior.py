# This file for calculate greatest common divisior (gcd) between two number.

# First of all we have to define function with def function.

def greatestcommondivisior(y, x):
    
    if (x > y) :
        small_number = y
    
    else:
        small_number = x

    for i in range(1,small_number+1):
        if ((x % i == 0 ) and (y % i == 0)):
            gcd = i

    return gcd
