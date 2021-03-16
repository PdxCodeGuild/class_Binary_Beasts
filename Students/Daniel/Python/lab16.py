import requests
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

response = requests.get("https://www.gutenberg.org/cache/epub/4/pg4.txt")
response.encoding = 'utf-8'
response = response.text.split("*END*THE SMALL PRINT! FOR PUBLIC DOMAIN ETEXTS*Ver.04.29.93*END*")
response = response[1]
response = response.split("Gettysburg, Pennsylvania, USA")
response = response[1]
response = response.replace(". . .", " ")
word_count = len(response.split(" "))
response = response.replace(" ", "")
char_count = 0
sentence_count = 0
for char in response:
    char_count+=1
    if char == ".":
        sentence_count += 1


print(4.71*(char_count/word_count)+0.5*(word_count/sentence_count)-21.43)
print(4.71*(1152/268)+0.5*(268/10)-21.43)
print(char_count)
print(sentence_count)
print(word_count)