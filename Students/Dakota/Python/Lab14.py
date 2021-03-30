# #Lab14
# #Version 1
# #Tens Dictionary
# tens = {2:'Twenty',3:'Thirty',4:'Fourty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
# #Ones Dictionary
# ones = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}

# user_input = int(input('What number would you like to convert: '))

# #Split number
# user_input_split_tens = user_input//10
# user_input_split_ones = user_input%10

# #find index of tens and ones dict
# if user_input_split_tens in tens:
#     tens_word = tens[user_input_split_tens]
# if user_input_split_ones in ones:
#     ones_word = ones[user_input_split_ones]
# print(f'{tens_word}-{ones_word}')

#Version 2
#Hundreds Dictionary
hundreds = {0:'',1:'One Hundred',2:'Two Hundred',3:'Three Hundred',4:'Four Hundred',5:'Five Hundred',6:'Six Hundred',7:'Seven Hundred',8:'Eight Hundred',9:'Nine Hundred'}
#Tens Dictionary
tens = {0:'0',1:'',2:'Twenty',3:'Thirty',4:'Fourty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
#Teens Dictionary
teens = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15:'Fifteen', 16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
#Ones Dictionary
ones = {0:'0',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}

user_input = int(input('What number would you like to convert: '))




#Split number
user_input_split_hundreds = user_input//100
user_input_split_tens = user_input%100//10
user_input_split_teens = user_input%100//1
user_input_split_ones = user_input%10

#find index of hundreds, tens, teens, and ones dict
while True:
    hundreds_word = hundreds[user_input_split_hundreds]
    tens_word = tens[user_input_split_tens]
    ones_word = ones[user_input_split_ones]
    
    if user_input > 100:
        if user_input_split_tens == 1:
            teen_word = teens[user_input_split_teens]
            print(f'{hundreds_word} and {teen_word}')
            break
        elif user_input_split_tens < 1 and user_input_split_ones < 1:
            print(f'{hundreds_word}')
            break
        elif user_input_split_tens > 1:
            print(f'{hundreds_word} and {tens_word}-{ones_word}')
            break
        elif user_input_split_ones > 0:
            print(f'{hundreds_word} and {ones_word}')
            break

    elif user_input < 100:
        if user_input_split_tens == 1:
            teen_word = teens[user_input_split_teens]
            print(f'{teen_word}')
            break
        if user_input_split_tens > 1:
            print(f'{tens_word}-{ones_word}')
            break
        elif user_input_split_tens < 1:
            print(f'{ones_word}')
            break
    