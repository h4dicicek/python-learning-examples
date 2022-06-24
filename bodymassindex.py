#We will calculate the body mass index(bmi) in this file.

#First of all, you must take body weight and height from the user.

body_weight = float(input("Please enter your body weight(kg): "))

body_height = float(input("Please enter your body height(m): "))

print("Your BMI is, {}".format(body_weight / (body_height * body_height)))