# In this file we'll question whether a number is a even number in this file.

# First we define a function.

def evenNumber(s):
    if (s % 2 == 0):
        return s
    else:
        raise ValueError