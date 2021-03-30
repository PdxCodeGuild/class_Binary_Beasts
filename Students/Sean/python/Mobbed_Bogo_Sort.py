import random

def random_list(num):
    random_values = []
    for i in range(num):
        random_values.append(random.randint(0,100))
    return random_values

def shuffle(l,a_list):
    for i in range(l):
        swap = random.randint(0,len(range(l))-1)
        a_list[i], a_list[swap] = a_list[swap], a_list[i]
    return a_list

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
        
def bogosort(n):
    while True:
        random_values = random_list(n)
        print(random_values)

        random_values = shuffle(len(random_values),random_values)
        print(random_values)

        sorted_or_not = is_sorted(random_values)
        print(sorted_or_not)
        if sorted_or_not == True:
            break

random_values = random_list(4)
bogosort(4)