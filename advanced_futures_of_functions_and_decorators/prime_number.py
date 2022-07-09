def extraPerfectNumber(func):
    def wrapper():
        print("Perfect number between 1 to 1000")
        for number in range(1,1001):
            total = 0
            i = 1
            while (i < number):
                if(number % i == 0):
                    total += i
                i += 1
            if (total == number):
                print(number)
        func()
    return wrapper


@extraPerfectNumber
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