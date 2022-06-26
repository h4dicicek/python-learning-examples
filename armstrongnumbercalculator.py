# In this file we calculate Armstrong Number.
# An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. 
# For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.

number = input("Please enter a number: ")

number_of_digits = len(number)

number = int(number)

digit = 0

total = 0

number2 = number

while (number2 > 0):
    digit == number2 % 10
    total += digit ** number_of_digits 
    number2 //= 10