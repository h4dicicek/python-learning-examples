def evenNumber(s):
    if (s % 2 == 0):
        return s
    else:
        raise ValueError

list_1 = [12,32,34,62,8,35,3,654,23,45,2]

for number in list_1:
    try:
        print(evenNumber(number))
    except:
        pass