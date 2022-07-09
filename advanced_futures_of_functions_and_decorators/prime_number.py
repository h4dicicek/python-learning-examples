def prime_number():
    print("Prime number between 1 to 1000")
    for number in range(2,1001):
        i = 2
        num = 0
        while (i < number):
            if (number % i == 0):
                num += 1
            i += 1
        if (num == 0):
            print(number) 

prime_number()