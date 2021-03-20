while True:

    def grade(x):
        if x in range(0, 101):
            if x >= 90:
                if x < 94:
                    return 'A-'
                elif x < 97:
                    return 'A'
                elif x <= 100:
                    return 'A+'

            elif x >= 80:
                if x < 84:
                    return 'B-'
                elif x < 87:
                    return 'B'
                elif x <= 89:
                    return 'B+'

            elif x >= 70:
                if x < 74:
                    return 'C-'
                elif x < 78:
                    return 'C'
                elif x <= 79:
                    return 'C+'

            elif x >= 60:
                if x < 64:
                    return 'D-'
                elif x < 68:
                    return 'D'
                elif x <= 69:
                    return 'D+'
            
            else:
                return 'F'

    try:
        score = int(input('Please enter your grade between 0 and 100\n'))
        if score > 0 and score < 101:
            print(grade(score))
            break
    except Exception as exc:
        print(exc)