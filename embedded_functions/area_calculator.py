# in this file we'll area calculator with map function.

# define function
def area_calculator(tuple):
    return tuple[0] * tuple[1]

# create list of lines
list_of_lines = [(3,4),(10,3),(5,6),(1,9)]

# and print result with map function
print(list(map(area_calculator,list_of_lines)))