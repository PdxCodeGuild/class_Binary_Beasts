
cc_num = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5] # This list will be 12 long
chk_dig = cc_num[-1::] # This is my check digit
cc_num_1 = cc_num[:15:] # This will need to be 11 for 12 digit input (list minus the last digit)
cc_num_1.reverse() # This reversed my list

cc_multi = []
for x in range(len(cc_num_1)):
    if x % 2 == 0: # even numbers are pushed to the list
        cc_multi.append(cc_num_1[x] * 2) # Multipying all even numbers 
    else:
        cc_multi.append(cc_num_1[x]) # Appending the all numbers to the list

cc_sub = []
for x in range(len(cc_multi)):
    if cc_multi[x] > 9: # Numbers greater than 9 are captured
        cc_sub.append(cc_multi[x] - 9) # Numbers greater than 9 are subtracted by 9
    else:
        cc_sub.append(cc_multi[x]) # Appending the all numbers to the list
        
cc_sum = sum(cc_sub)

if cc_sum % 10 == chk_dig[0]: 
    print(True)
else:
    print(False)




print(chk_dig)
print(cc_num_1)
print(cc_multi)
print(cc_sub)
print(cc_sum)