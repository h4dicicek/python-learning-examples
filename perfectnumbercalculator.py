# In this file we calculate perfect number.
# In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisons, excluding the number itself.
# For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.

number = int(input("Please enter a number: "))

i = 1
total = 0 

# We have to use loop for find positive divisons

while(i < number):
    if (number % i  ==0):
        total += i
    i += 1

if ( total == number):
    print("{} is a perfect number.".format(number))

else:
    print("{} is not a perfect number.".format(number))