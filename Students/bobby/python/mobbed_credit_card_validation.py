
def cc_validator():
    cc_num = list(input("Enter your 16 digit credit card number: ")) # This string will be 16 digits long
    cc_num = [int(i) for i in cc_num] # Converts list to a list of intigers
    chk_dig = cc_num[-1::] # This is my check digit
    cc_num_1 = cc_num[:15:] # This will need to be 15 for 16 digit input (list minus the last digit)
    cc_num_1.reverse() # This reversed my list

    cc_multi = []
    for x in range(len(cc_num_1)):
        if x % 2 == 0: # even numbers are pushed to the list
            cc_multi.append(cc_num_1[x] * 2) # Multipying all even [indicies] numbers 
        else:
            cc_multi.append(cc_num_1[x]) # Appending the all numbers to the list

    cc_sub = []
    for x in range(len(cc_multi)):
        if cc_multi[x] > 9: # Numbers greater than 9 are captured
            cc_sub.append(cc_multi[x] - 9) # Numbers greater than 9 are subtracted by 9
        else:
            cc_sub.append(cc_multi[x]) # Appending the all numbers to the list
            
    cc_sum = sum(cc_sub)

    if cc_sum % 10 == chk_dig[0]: # Performs comparison between sum second digit and check digit, returns valid or not valid 
        return("Valid")
    else:
        return("Not Valid")
        
print (cc_validator())

" 4556737586899855 " # Card number used for validation




