def peaks(data):
    print(data)
    y = 0
    for x in data:
        if data[y-1]< x > data[y+1]:
            print(str(x) + "Added")
            peaks_list.append(x)
        y+=1
def valleys(data):
    return 0

def peaks_and_valleys(data):
    return 0

test_data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]



peaks_list = []

valleys_list = []

peaks_and_valleys = []

peaks(test_data)
print(peaks_list)