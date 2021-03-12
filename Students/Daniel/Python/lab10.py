def peaks(data):
    for x in range(len(test_data)-1):
        if test_data[x -1] < test_data[x] > test_data[x+1]:
            peaks_list.append(x)
            peaks_and_valleys.append(x)



def valleys(data):
    for x in range(len(test_data)-1):
        x+=1
        if test_data[x -1] > test_data[x] < test_data[x+1]:
            valleys_list.append(x)
            peaks_and_valleys.append(x)
    

test_data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]



peaks_list = []

valleys_list = []

peaks_and_valleys = []


peaks(test_data)
print(peaks_list)
valleys(test_data)
print(valleys_list)
peaks_and_valleys = sorted(peaks_and_valleys)
print(peaks_and_valleys)