score = input('Enter in your score: ')
score = int(score)
if score >= 90:
    grade = 'A'
    if score % 10 >= 7:
        grade += '+'
    elif score % 10 <= 3:
        grade += '-'
elif 89 >= score >= 80:
    grade = 'B'
    if score % 10 >= 7:
        grade += '+'
    elif score % 10 <= 3:
        grade += '-'
elif 79 >= score >= 70:
    grade = 'C'
    if score % 10 >= 7:
        grade += '+'
    elif score % 10 <= 3:
        grade += '-'
elif 69 >= score >= 60:
    grade = 'D'
    if score % 10 >= 7:
        grade += '+'
    elif score % 10 <= 3:
        grade += '-'
else:
    grade = 'F'

print(f'Your score was {score}. Your grade is {grade}')