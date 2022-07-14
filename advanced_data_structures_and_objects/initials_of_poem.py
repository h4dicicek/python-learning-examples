initials = ""

with open("poem.txt", "r", encoding="utf-8") as file:
    for line in file:
        initials += line[0]

print(initials)
