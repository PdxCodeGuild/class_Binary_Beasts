def getGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def getFinalGrade(score):
    grade = getGrade(score)
    
    if grade == "F":
        return grade
    
    if score % 10 > 6:
        return grade + "+"
    elif score % 10 < 4:
        return grade + "-"
    else:
        return grade

score = input("What is your score?")
print(getFinalGrade(score))