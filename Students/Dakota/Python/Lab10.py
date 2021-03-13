#Lab 10
#define functions 
def peaks(x):
    for i,j in enumerate(data):
        if x > j or j > x:
            return peaks
def valleys(y):
    for i,j in enumerate(data):
        if i < j or j < i:
            return valleys
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9] #j values
# index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 i values

fruits = ['apples', 'bananas', 'pears']
for i, fruit in enumerate(fruits):
    print(str(i) + ' ' + fruit)