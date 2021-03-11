user_string = input("Please enter a string for the ROT Cipher: ")
desired_rotation = int(input("Please enter desired rotation: "))
english = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
rot = ""
for x in user_string:
    pos = english.index(x)
    rot += english[pos-desired_rotation]

print(rot)