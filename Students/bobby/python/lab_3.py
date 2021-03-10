# This is my grading code.

score = input('Please enter your score: ') # User input there score.
score = int(score) # Converts the user input to an integer.
if score >= 90: # Condition for greater or equal to 90.
    print ('You got an A!') 
elif score >= 80: # Condition for greater or equal to 80.
    print ('You got a B!')
elif score >= 70: # Condition for greater or equal to 70.
    print ('You got a C!')
elif score >= 60: # Condition for greater or equal to 60.
    print ('You got a D!')
elif score < 59: # Condition for less than 59.
    print ('YOU FAILED!')