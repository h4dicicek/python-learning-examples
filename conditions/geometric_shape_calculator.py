import time

def triangle_calculator(line_1 = int ,line_2 = int,line_3 = int):
    line_1 = abs(line_1)
    line_2 = abs(line_2)
    line_3 = abs(line_3)
    print("Your triangle is calculating..")
    time.sleep(0.5)
    if (line_1 == line_2 == line_3):
        return "Your triangle is Equilateral Triangle."
    elif (line_1 + line_2 < line_3):
        return "The shape is not a triangle."
    elif ((line_1 == line_2 != line_3) or (line_2 == line_3 != line_1) or (line_1 == line_3 != line_2)):
        return "Your triangle is Isosceles Triangle."
    else:
        return "Your triangle is Normal Triangle :)."

def rectangle_calculator(line_1 = int ,line_2 = int,line_3 = int,line_4 = int):
    line_1 = abs(line_1)
    line_2 = abs(line_2)
    line_3 = abs(line_3)
    line_4 = abs(line_4)
    print("Your rectangle is calculating..")
    time.sleep(0.5)
    if (line_1 == line_2 == line_3 == line_4):
        return "Your rectangle is Square."
    elif(line_1 == line_3 != line_2 == line_4):
        return "Your shape is Rectangle."
    else:
        return "Your shape is normal rectangle."

print(rectangle_calculator(3,3,3,3))
    

### Unfortunately we can't calculate many geometrical shape. Because to calculate that, we have to learn their angle. 
### We can do this future projects.