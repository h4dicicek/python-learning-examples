import time

def how_many_lines_equal(line_1 = int,line_2 = int,line_3 = int):
    if (line_1 == line_2 == line_3):
        return 3
    elif ((line_1 == line_2 != line_3) or (line_1 != line_2 == line_3)):
        return 2
    else:
        return 0

def how_many_lines_equal_rectangle(line_1 = int ,line_2 = int,line_3 = int,line_4 = int):
    if (line_1 == line_2 == line_3 == line_4):
        return 4
    elif(line_1 == line_3 != line_2 == line_4):
        return 2
    else:
        return 0

print("""
_________________________________
                                |
Press 1 for calculate triangle. |
Press 2 for calculate rectangle.|
________________________________|
""")

selected_shape = int(input("Please enter a number for calculate the shape: "))

if (selected_shape == 1):
    print("Please enter lines from small to large!")
    first_line = abs(int(input("Please enter the first line: ")))
    second_line = abs(int(input("Please enter the second line: ")))
    third_line = abs(int(input("Please enter the third line: ")))
    equal_lines = how_many_lines_equal(first_line,second_line,third_line)
    print("Your triangle is calculating..")
    time.sleep(0.5)
    if (equal_lines == 3):
        print("Your triangle is Equilateral Triangle.")
    elif(first_line + second_line < third_line):
        print("The shape is not a triangle.")
    elif (equal_lines == 2):
        print("Your triangle is Isosceles Triangle.")
    else:
        print("Your triangle is Normal Triange :].")
elif (selected_shape == 2):
    first_line = abs(int(input("Please enter the first line: ")))
    second_line = abs(int(input("Please enter the second line: ")))
    third_line = abs(int(input("Please enter the third line: ")))
    fourth_line = abs(int(input("Please enter the fourth line: ")))
    equal_lines = how_many_lines_equal_rectangle(first_line,second_line,third_line,fourth_line)
    print("Your rectangle is calculating..")
    time.sleep(0.5)
    if (equal_lines == 4):
        print("Your rectangle is Square.")
    elif (equal_lines == 2):
        print("Your shape is Rectangle.")
    else:
        print("Your shape is normal rectangle.")
else:
    print("Shape is not found.")



### Unfortunately we can't calculate many geometrical shape. Because to calculate that, we have to learn their angle. 
### We can do this future projects.