# In this file we calculate perfect number. Between 1 and 1000

# We have to create a new function with use def.

def perfectnumber(number):

    total = 0 

    for i in range(1,number):

        if (number % i == 0):
            total += i

    return total == number

for i in range(1,1001):
    if (perfectnumber(i)):
        print("Perfect Number:",i)