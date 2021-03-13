def lengther(a, b, c):
    dist = {
        'ft':0.3048,
        'mi':1609.34,
        'm':1,
        'km':1000,
        'yard':0.9144,
        'inch':0.0254,
    }
    return a * dist[b] * dist[c]

length = input("How many units are you trying to convert?\n>")
unit1 = input("Please enter what unit you are trying to convert\n'ft', 'mi', 'm', 'km', 'yard', or 'inch'\n>")
unit2 = input("Please enter what unit you are trying to convert to\n'ft', 'mi', 'm', 'km', 'yard', or 'inch'\n>")
print(lengther(int(length),unit1,unit2))