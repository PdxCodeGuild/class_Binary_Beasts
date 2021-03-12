"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

g = ["A", "B", "C", "D", "F"]  # global grades as list

# Minified Approach (JavaScript Style)
# Super fast, but not recommended for best coding practices

m = max

def run_approach1(s):

    def j(a, b, c):
        return b if a else c

    def f(s):  # the madness
        return g[j(s==100,-5,-(m(0,s-50))//10)]+j(s==100,"++",\
            j(s<60,"",j(s%10<4,"-",j(s%10>6,"+",""))))

    return f(s)

# Best Approach


def run_approach2(score):
    grades = g  # reassigning grades to a better variable name
    mod = ""
    if score > 59 and score % 10 < 4:
        mod = "-"
    elif score > 59 and score % 10 > 6:
        mod = "+"
    index = -(m(0, score - 50)) // 10  # The magic

    if score == 100:
        return "A++"
    else:
        grade = grades[index]
        return grade + mod


# Beginner approach

def run_approach3(score):
    grade = "F"
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif grade >= 60:
        grade = "D"

    mod = ""
    if score >= 60 and score % 10 < 4:  # no modifier if below 60 (f)
        mod = "-"
    elif score >= 60 and score % 10 > 6:
        mod = "+"

    if score == 100:
        return "A++"
    else:
        return grade + mod


approaches = [run_approach1, run_approach2, run_approach3]

while True:

    print('Welcome. You can type "done" at any time to exit.')
    
    max = len(approaches)

    strategy = 0
    while strategy not in range(1, max):
        try:
            strategy = input(f"Which approach would you like to run: 1 - {max}")
            if strategy == "done":
                break
            strategy = int(strategy)
        except:
            continue
        if strategy == "done":
            break

    strategy = approaches[strategy - 1]
    
    score = ""
    
    while True:
        score = input("Enter a score 0 - 100")
        try:
            score = int(score)
            break
        except:
            continue

    print(strategy(score))
