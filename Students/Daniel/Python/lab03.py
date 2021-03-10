user_input = input("Please enter a number representing a letter grade of (0-100): ")
user_input = int(user_input)
if user_input >= 90:
    print("A")
elif user_input >= 80:
    print("B")
elif user_input >= 70:
    print("C")
elif user_input >= 60:
    print("D")
else:
    print("F")
print(bool(1))