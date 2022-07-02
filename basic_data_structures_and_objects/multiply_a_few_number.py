
"""
Solution 1
# if you wanna solve the problem with create function:

def multiply_a_few_number(*args):
    number = 1
    for arg in args:
        number *= arg
    return number

print(multiply_a_few_number(15,20,25))
"""

# Solution 2
number = int(input("How many values you want to multiply: "))
num = 1
for i in range(number):
    num = int(input("Enter number to multiply: ")) * num
print(num)