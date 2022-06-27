# In this file we calculate lowest common multiple between two number.

# Now we have to define a function.

def lowestcommonmultiple(x,y):

    if (x > y):
        bigger = x
    else:
        bigger = y
    
    while True:
        if((bigger % x == 0 ) and (bigger % y == 0 )):

            lcm = bigger
            break
    
        bigger += 1
    return lcm