import random

predictions = [
    'Pretty sure, yeah.',
    'For sure, yes.',
    'Not gonna happen.',
    'Try again later.',
    'Don\'t hold your breath.',
    'Your guess is as good as mine.',
]

print('Welcome to the magic 8 ball!\nAll your questions can soon be answered.')

while True:
    answer = random.choice(predictions)
    user_question = input('Ask a question, or enter "done" if you don\'t believe in magic.\n>')
    if user_question == 'done':
        break
    elif user_question[-1] != '?':
        print('Please ask a valid question.')
    else:
        print(f'I\'m asking the ball "{user_question}"\nI\'m getting a reply of "{answer}"\n')