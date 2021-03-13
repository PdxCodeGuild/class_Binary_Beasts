"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

import requests  # run "python3 -m pip install requests" to install this library
from string import *
import re

url = "http://www.gutenberg.org/files/64796/64796-0.txt"

response = requests.get(url)
response.encoding = "utf-8"
text = response.text


def get_word_count():
    words = re.split(" |\n, |\r\n", text)

    return len(words)


def get_sentence_count():
    sentences = text.split(".")

    return len(sentences)


def get_character_count():
    count = 0
    for x in text:
        if x.isalpha():
            count += 1

    return count


def calculate_level():
    chars = get_character_count()
    words = get_word_count()
    sentences = get_sentence_count()

    return int(4.71 * (chars / words) + 0.5 * (words / sentences) - 21.43)


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

level = calculate_level()
results = ari_scale[level]
grade = results["grade_level"]
ages = results["ages"]

print(f"The ARI for this book is {level}.")
print(f"This corresponds to a {grade} level of difficulty.")
print(f"This is suitable for an average person {ages} years old.")
