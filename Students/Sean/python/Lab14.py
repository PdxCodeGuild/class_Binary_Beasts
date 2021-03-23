def phraser(x):
    ones = ('', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',)
    odds = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
    tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety',)
    
    hun_dig = x//100
    ten_dig = (x//10)%10
    one_dig = x%10

    if x <= 9:
        return f"{ones[one_dig]}"
    elif x <= 19:
        return f"{odds[one_dig]}"
    elif x <= 99:
        return f"{tens[ten_dig-2]} {ones[one_dig]}"
    elif x <= 109:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 119:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x <= 209:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 219:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x <= 309:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 319:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x <= 409:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 419:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x <= 509:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 519:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x <= 609:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 619:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x <= 709:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 719:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x <= 809:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 819:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x <= 909:
        return f"{ones[hun_dig]}-hundred {ones[one_dig]}"
    elif x <= 919:
        return f"{ones[hun_dig]}-hundred {odds[one_dig]}"
    elif x >= 120:
        return f"{ones[hun_dig]}-hundred {tens[ten_dig-2]} {ones[one_dig]}"

num = int(input("Enter a number\n>"))
print(phraser(num))