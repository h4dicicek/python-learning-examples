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

total_grade = (midterm1 * 0.3) + (midterm2 * 0.3) + (final_grade * 0.4)

print("Your total grade: {}".format(total_grade))

#We use conditions for calculate letter grade.

if (total_grade >= 90):
    print("Your letter grade AA. Congrats!")
elif (total_grade >= 85 ):
    print("Your letter grade BA. Well done!")
elif (total_grade >= 80 ):
    print("Your letter grade BB. Good job!")
elif (total_grade >= 75 ):
    print("Your letter grade CB. Nice!")
elif (total_grade >= 70 ):
    print("Your letter grade CC. You're going to great!")
elif (total_grade >= 65 ):
    print("Your letter grade DC.")
elif (total_grade >= 60 ):
    print("Your letter grade DD.")
elif (total_grade >= 55 ):
    print("Your letter grade FD. Sorry for you!")
elif (total_grade >= 0):
    print("Your letter grade FF. Sorry for you!")
elif ( total_grade > 100):
    print("Your total grade can't over 100.")
else:
    print("Your total grade can't under 0.")