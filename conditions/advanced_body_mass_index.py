#We will calculate the body mass index(bmi) in this file.

"""
Severe Thinness	< 16
Moderate Thinness	16 - 17
Mild Thinness	17 - 18.5
Normal	18.5 - 25
Overweight	25 - 30
Obese Class I	30 - 35
Obese Class II	35 - 40
Obese Class III	> 40 
"""

#First of all, you must take body weight and height from the user.

body_weight = float(input("Please enter your body weight(kg): "))

body_height = float(input("Please enter your body height(m): "))

body_mass_index = body_weight / (body_height ** 2)

print("Your BMI {}".format(body_mass_index))

if (body_mass_index < 16):
    print("You're Severe Thinness.") 

elif (16 < body_mass_index < 17):
    print("You're Moderate Thinnes")

elif (17 < body_mass_index < 18.5):
    print("You're Mild Thinness.")

elif (18.5 < body_mass_index < 25):
    print("You're Normal weight.")

elif (25 < body_mass_index < 30):
    print("You're owerweight.")

elif (30 < body_mass_index):
    print("You're obese.")