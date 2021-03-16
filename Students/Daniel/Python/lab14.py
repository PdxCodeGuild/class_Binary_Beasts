ones = {"0":"And ", "1":"One ", "2":"Two ", "3":"Three ", "4":"Four ", "5":"Five ", "6":"Six ", "7":"Seven ", "8":"Eight ", "9":"Nine "}
teens = {"0":"And ", "1":"Eleven ", "2":"Twelve ", "3":"Thirteen ", "4":"Fourteen ", "5":"Fifteen ", "6":"Sixteen ", "7":"Seventeen ", "8":"Eighteen ", "9":"Nineteen "}
tens = {"0":"And ", "1":"Ten ", "2":"Twenty ", "3":"Thirty ", "4":"Fourty ", "5":"Fifty ", "6":"Sixty ", "7":"Seventy ", "8":"Eighty ", "9":"Ninety "}
hundreds = {"1":"One Hundred ", "2":"Two Hundred ", "3":"Three Hundred ", "4":"Four Hundred ", "5":"Five Hundred ", "6":"Six Hundred ", "7":"Seven Hundred ", "8":"Eight Hundred ", "9":"Nine Hundred "}

number = input("Please enter a number to be converted to a phrase: ")

if len(number) == 3:
    print(hundreds[number[0]] + tens[number[1]] + ones[number[2]])

if len(number) == 2:
    if number [0] == "1":
        print(teens[number[1]])
    else:
        print(tens[number[0]] + ones[number[1]])

if len(number) == 1:
    print(ones[number[0]])