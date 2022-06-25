# We'are gonna calculate letter grade for university students. 

"""
Midterm1 will impact 30% of the total grade.

Midterm2 will impact 30% of the total grade.

Final will impact 40% of the total grade.


Total grade >=  90 -----> AA

Total grade >=  85 -----> BA

Total grade >=  80 -----> BB

Total grade >=  75 -----> CB

Total grade >=  70 -----> CC

Total grade >=  65 -----> DC

Total grade >=  60 -----> DD

Total grade >=  55 -----> FD

Total grade <  55 -----> FF
"""

#You must take grades from user.

midterm1 = int(input("Please enter your first midterm grade: "))

midterm2 = int(input("Please enter your second midterm grade: "))

final_grade = int(input("Please enter your final grade: "))

#You have to calculate total grade for letter grade.

total_grade = (midterm1 * (3/10)) + (midterm2 * (3/10)) + (final_grade * (4/10))

print("Your total grade: {}".format(total_grade))