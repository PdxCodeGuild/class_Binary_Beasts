#lab 5
import random
#While loop to generate 5 emoticons
i = 0
while i < 5:
    #Define List of eyes
    eyes = [':',';','=','8']
    #Define List of noses 
    noses = ['>','-','~']
    #Define List of mouths
    mouths = ['(',')','0','>','{','}']
    #Concatenate Eyes Nose and Mouth
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    #Print Emoticons
    print(emoticon,end=" ")
    #Increment by 1 until 5 emoticons have printed
    i += 1