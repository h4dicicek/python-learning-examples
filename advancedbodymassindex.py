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
