def extra(func):
    def wrapper(numbers):
        evens_total = 0
        evens = 0
        odds_total = 0
        odds = 0

        for i in numbers:
            if(i % 2 == 0):
                evens_total += i
                evens += 1
            else:
                odds_total += i
                odds += 1
        print("Average of evens:",evens_total/evens)
        print("Average  of odds:",odds_total/odds)
        func(numbers)
    return wrapper

@extra
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    print("Average:",total/len(numbers))

numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

average(numbers)