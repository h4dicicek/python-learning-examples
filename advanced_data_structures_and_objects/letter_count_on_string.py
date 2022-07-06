# in this file we'll calculate how many times a letter in string repeats.

string = "Howmanytimesaletterinstringrepeats?"
repeats = dict()

for letter in string:
    if (letter in repeats):
        repeats[letter] += 1
    else:
        repeats[letter] = 1

for i,j in repeats.items():
    print(i,':',j)