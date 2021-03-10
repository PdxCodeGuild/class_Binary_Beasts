"""
#Version 1
grade = int(input('Enter your grade: '))
if grade >= 90 and grade <= 100:
    print("Your grade is an A")
elif grade >= 80 and grade < 90:
    print("Your grade is an B")
elif grade >= 70 and grade < 80:
    print("Your grade is an C")
elif grade >= 60 and grade < 70:
    print("Your grade is an D")
elif grade >= 0 and grade < 60:
    print("Your grade is an F")
"""
#Version 2
grade = int(input('Enter your grade: '))
if grade >= 90 and grade <= 100:
    if grade < 95:
         print("Your grade is an A-")
    if grade == 95:
         print("Your grade is an A")
    if grade > 95:
         print("Your grade is an A+")
elif grade >= 80 and grade < 90:
    if grade < 85:
         print("Your grade is an B-")
    if grade == 85:
         print("Your grade is an B")
    if grade > 85:
         print("Your grade is an B+")
elif grade >= 70 and grade < 80:
    if grade < 85:
         print("Your grade is an C-")
    if grade == 85:
         print("Your grade is an C")
    if grade > 85:
         print("Your grade is an C+")
elif grade >= 60 and grade < 70:
    if grade < 85:
         print("Your grade is an D-")
    if grade == 85:
         print("Your grade is an D")
    if grade > 85:
         print("Your grade is an D+")
elif grade >= 0 and grade < 60:
    print("Your grade is an F")