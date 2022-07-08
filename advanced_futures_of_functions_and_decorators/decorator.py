def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return "Average" + total/len(numbers)

