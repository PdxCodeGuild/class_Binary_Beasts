#Minimized Approach

g = ["A", "B", "C", "D"]

def getGrade(s):
    return "F" if s<60 else g[-4 if s==100 else -(s-59)//10] + "++" if s==100\
        else "-" if s%10<4 else "+" if s%10>6 else ""

while True:
    print(getGrade(int(input("What is your score?"))))
    if input("Play again?") == "no":
        break


#Expanded Approach

def getGradeExpanded(score):
    g.append("F")
    grades = g
    mod = ""
    if score > 59 and score % 10 < 4:
        mod = "-"
    elif score > 59 and score % 10 > 6:
        mod = "+"
    index = -(score - 49) // 10
    
    if score == 100:
        return "A++"
    else:
        grade = grades[index]
        return grade + mod
    

while True:
    score = input("What is your score?")
    score = int(score)
    grade = getGradeExpanded(score)
    print(grade)
    again = input("Play again?")
    if again == "no":
        break