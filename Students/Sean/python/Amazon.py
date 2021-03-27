def Compress(string):
    compressed = []
    for letter in string:
        if letter not in compressed:
            compressed.append(letter)
        if letter in compressed:
            compressed.append(1)
    return str(compressed)
    
print(Compress("wwaeexxaa"))