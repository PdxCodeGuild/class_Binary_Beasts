import random
playagain = 'yes'
responselist = ['It is certain','It is decidedly so','Without a doubt'
'Yes definitely',
'You may rely on it',
'As I see it, yes',
'Most likely',
'Outlook good',
'Yes',
'Signs point to yes',
'Reply hazy try again',
'Ask again later',
'Better not tell you now',
'Cannot predict now',
'Concentrate and ask again',
'Don\'t count on it',
'My reply is no',
'My sources say no',
'Outlook not so good',
'Very doubtful']
while playagain == 'yes':
    welcomescreen = input('Welcome to Magic 8 Ball\nWhat is your question: ')
    response = random.choice(responselist)
    print(response)
    playagain = input('Would you like to play again?\nyes or done')


