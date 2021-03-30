'''
Theo Cocco
Thursday March 25, 2021
Lab 16 Compute Automated Readability Index
'''

from math import ceil

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

book = 'The Great Gatsby.txt'

book_title = book.replace('.txt', '')

with open(book, 'r', encoding='utf-8') as f:
    text = f.read()

punct = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ '


def compute(x,y,z):
    score = ceil(4.72 * (x/y) + .5 * (y/z) - 21.43)
    if score >= 14:
        score = 14
    return score

def get_c(x):
    translator = str.maketrans('','',punct)
    c = x.translate(translator)
    c = len(c)
    return c

def get_w(x):
    w = x.split()
    w = len(w)
    return w

def get_s(x):
    s = x.split('.')
    s = len(s)
    return s

print(f'''The ARI of {book_title} is {compute(get_c(text), get_w(text), get_s(text))}
This corresponds to a {ari_scale[compute(get_c(text), get_w(text), get_s(text))]['grade_level']} Grade level of difficulty
that is suitable for an average person {ari_scale[compute(get_c(text), get_w(text), get_s(text))]['ages']} years old.''')
