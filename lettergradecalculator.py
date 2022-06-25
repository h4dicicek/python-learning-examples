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

#We use conditions for calculate letter grade.

if (total_grade >= 90):
    print("Your letter grade AA. Congrats!")

elif ( 90 > total_grade >= 85 ):
    print("Your letter grade BA. Well done!")

elif ( 85 > total_grade >= 80 ):
    print("Your letter grade BB. Good job!")

elif ( 80 > total_grade >= 75 ):
    print("Your letter grade CB. Nice!")

elif ( 75 > total_grade >= 70 ):
    print("Your letter grade CC. You're going to great!")

elif ( 70 > total_grade >= 65 ):
    print("Your letter grade DC.")

elif ( 65 > total_grade >= 60 ):
    print("Your letter grade DD.")

elif ( 60 > total_grade >= 55 ):
    print("Your letter grade FD. Sorry for you!")

elif ( 55 > total_grade ):
    print("Your letter grade FF. Sorry for you!")