"""
all codes are written and created by John Robson Wed Mar 9, 2021
"""

g = ["A", "B", "C", "D", "F"] #global grades as list

#Minimized Approach (JS Style)
#Super fast, but not recommended for best coding practices

i = input; p = print; m = max; z = int; t = True; q = "What is your score?"; a = "Play again?"; n = "no";

def j(a, b, c):
    return b if a else c

def f(s):
    return g[j(s==100,-5,-(m(10,s-40))//10)]+j(s==100,"++",j(s<60,"",j(s%10<4,"-",j(s%10>6,"+",""))))

while t:
    p(f(z(i(q))))
    if i(a)==n:
        break




#Expanded Approach
#Best Approach

def getGradeExpanded(score):
    grades = g     #reassigning grades to a better variable name
    mod = ""
    if score > 59 and score % 10 < 4:
        mod = "-"
    elif score > 59 and score % 10 > 6:
        mod = "+"
    index = -(max(10, score - 50)) // 10   #The magic:
                                #we reduce the score to a number between 50 and 0
                                #then we get the highest number between the reduced score and 10
                                #we set 10 as the base, so that as the lowest number we
                                #get -(10/10) which equals -1 (if we have a 0 index it returns wrong value)
                                #then divide and floor to get a number 1 - 5
                                #we negate the number to get a negative index used to find our grade
    
    if score == 100:    #100 is index -5 which breaks our list range, so we write an exception
        return "A++"
    else:
        grade = grades[index]
        return grade + mod
    

# while True:
#     score = int(input("What is your score?"))
#     grade = getGradeExpanded(score)
#     print(grade)
#     again = input("Play again?")
#     if again == "no":
#         break
    
#Super Expanded Approach
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
    

# while True:
#     score = input("What is your score?")
#     score = int(score)
#     grade = getGradeExpanded(score)
#     print(grade)
#     again = input("Play again?")
#     if again == "no":
#         break