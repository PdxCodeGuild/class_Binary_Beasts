
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks = []
valleys = []
both = []
index = 0

def f_peaks():
    if data[index] > data[index+1] and data[index] > data[index-1]:
        peaks.append(index)
    
def f_valleys():
    if data[index] < data[index+1] and data[index] < data[index-1]:
        valleys.append(index) 

def f_both():
    if data[index] > data[index+1] and data[index] > data[index-1]:
        both.append(index)
    elif data[index] < data[index+1] and data[index] < data[index-1]:
        both.append(index)

for d in data:
    if index > 0 and index <= 19:
        f_peaks()
        f_valleys()
        f_both()
    index +=1

print (f"Peaks are {peaks}")
print (f"Valleys are {valleys}")
print (f"Both are {both}")


