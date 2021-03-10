"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

g = ["A", "B", "C", "D", "F"] #global grades as list

#Minimized Approach (JavaScript Style)
#Super fast, but not recommended for best coding practices

i = input; p = print; m = max; l = str.lower; z = int; t = True; q = "Score?"; a = "Again?"; n = "no";

def j(a, b, c):
    return b if a else c

def f(s):
    return g[j(s==100,-5,-(m(10,s-40))//10)]+j(s==100,"++",j(s<60,"",j(s%10<4,"-",j(s%10>6,"+",""))))

while t:
    p(f(z(i(q))))
    if l(i(a))==n:
        break




#Best Approach

def getGradeExpanded(score):
    grades = g     #reassigning grades to a better variable name
    mod = ""
    if score > 59 and score % 10 < 4:
        mod = "-"
    elif score > 59 and score % 10 > 6:
        mod = "+"
    index = -(max(10, score - 50)) // 10   #The magic
    
    if score == 100:
        return "A++"
    else:
        grade = grades[index]
        return grade + mod
    

#Uncomment lines below to test this approach
# while True:
#     score = int(input("What is your score?"))
#     grade = getGradeExpanded(score)
#     print(grade)
#     again = input("Play again?")
#     if again == "no":
#         break
    
    
    
#Beginner approach

def getGradeExpanded(score):
    grade = "F"
    if score > 90:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score > 70:
        grade = "C"
    elif grade > 60:
        grade = "D"
        
    mod = ""
    if score >= 60 and score % 10 < 4: #no modifier if below 60 (f)
        mod = "-"
    elif score >= 60 and score % 10 > 6:
        mod = "+"
    
    if score == 100:
        return "A++"
    else:
        return grade + mod
    

#Uncomment lines below to test this approach

# while True:
#     score = input("What is your score?")
#     score = int(score)
#     grade = getGradeExpanded(score)
#     print(grade)
#     again = input("Play again?")
#     if again == "no":
#         break