import random
user_input = input("How many charcters would you like your password to be? ")
user_input = int(user_input)
#print(user_input)
letters = ("abcdef") # String of letters for password
numbers = ["1","2","3","4","5","6"] # List of numbers for password
count = 0 # This is my loop control
password = [] # Empty list to hold the password(must be outside the loop)
while count < user_input: # While loop to run 5 times
    passwordl = random.choice(letters) # Randomly chooses the letters from the string
    passwordn = random.choice(numbers) # Randomly chooses the numbers from the list
    password.append(passwordl + passwordn) # Appends the letters & numbers in pairs
    count += 1 # Adds one at the end of the loop
print ("".join(password)) # Joins both strings together

