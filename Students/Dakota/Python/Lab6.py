#Lab 6
#Import Modules
import random
import string 
#define string values
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
#define password input as integer 
n = int(input('Enter a password lenght '))
#set up while loop to increment
i = 0
#Begin while loop
while i < n:
    #define output based on string values
    output = lowercase + uppercase + digits + punctuation
    #define random_output that chooses a random one from the output
    random_output = random.choice(output)
    #print users password
    print(random_output,end="")
    #increment by 1 until reaches users input integer
    i += 1