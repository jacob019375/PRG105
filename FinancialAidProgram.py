

student_Enrollment = int(input('Are you a new or returning student? Enter 1 for returning and 2 for new '))

gpa = float(input('Enter your GPA: '))

criminal_record = int(input('Have you ever been convicted of a drug felony? Enter 1 for yes and 2 for no.  '))

creditHours = int(input('Enter your enrolled credit hours for next semester: '))

income = int(input('Enter your yearly salary rounded to the nearest dollar: '))

points = 0
if student_Enrollment == 1 or student_Enrollment == 2:
    points += 1

if gpa > 2.0:
    points += 1
if gpa < 2.0:
    points -= 1

if criminal_record == 2:
    points += 1
if criminal_record == 1:
    points -= 1

if creditHours >= 6:
    points += 1
if creditHours < 6:
    points -= 1

if income < 50000:
    points += 1
if income > 50000:
    points -= 1

print(points)
if points < 5:
    print('You are not eligible for financial assistance.')
if points == 5:
    print('You are eligible for financial assistance.')
