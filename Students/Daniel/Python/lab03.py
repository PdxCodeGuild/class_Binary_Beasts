user_input = input("Please enter a number representing a letter grade of (0-100): ")
user_input = int(user_input)
user_grade = ""
user_sign = ""
if user_input % 10 >= 5:
    user_sign = "+"
else:
    user_sign = "-"

if user_input >= 90:
    user_grade = "A"
elif user_input >= 80:
    user_grade = "B"
elif user_input >= 70:
    user_grade = "C"
elif user_input >= 60:
    user_grade = "D"
else:
    user_grade = "F"

print(user_grade + user_sign)

