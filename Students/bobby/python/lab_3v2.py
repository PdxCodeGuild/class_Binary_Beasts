# This is my grading code.

score = input('Please enter your score: ') # User input there score.
score = int(score) # Converts the user input to an integer.
if score >= 95: # Condition for A+.
    print ('You got an A+!') 
elif score >= 90 and score < 95: # Condition for A-.
    print ('You got a A-!')
elif score >= 85 and score < 90: # Condition for B+.
    print ('You got a B+!')
elif score >= 80 and score < 85: # Condition for B-.
    print ('You got a B-!')
elif score >= 75 and score < 80: # Condition for C+.
    print ('You got a C+!')
elif score >= 70 and score < 75: # Condition C-.
    print ('You got a C-!')
elif score >= 65 and score < 70: # Condition D+.
    print ('You got a D+!')
elif score >= 60 and score < 65: # Condition for D-.
    print ('You got a D-!')
elif score <= 59: # Condition for less than 59.
    print ('YOU FAILED!')