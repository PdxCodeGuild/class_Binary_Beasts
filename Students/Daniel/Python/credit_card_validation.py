credit_card_num = "4556737586899855"
cc_num_list = []
cc_sum = 0
for digit in credit_card_num:
    cc_num_list.append(int(digit))



check_digit = cc_num_list[-1]
cc_num_list = cc_num_list[0:-1]
cc_num_list.reverse()




for num in range(0,len(cc_num_list),2):
    cc_num_list[num] = cc_num_list[num]*2
    if cc_num_list[num] > 9:
        cc_num_list[num] = cc_num_list[num] - 9


for item in cc_num_list:
    cc_sum += item



print(cc_num_list)
print(cc_sum)
print(check_digit)
cc_sum = str(cc_sum)  # making int object subscriptable for comparison
if cc_sum[-1] == str(check_digit):
    print("Valid!")