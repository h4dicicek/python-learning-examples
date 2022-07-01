# In this file we'll question whether a number is a even number in this file.

# First we define a function.

def evenNumber(s):
    if (s % 2 == 0):
        return s
    else:
        raise ValueError

# create a list for testing function.

list_1 = [12,32,34,62,8,35,3,654,23,45,2]

for number in list_1:
    
    try:
        print(evenNumber(number))
    except:
        pass