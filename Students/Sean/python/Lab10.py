def peaks(data):
    peaks_test = []
    peaks_list = []
    for i, value in enumerate(data):
        peaks_test.append(value)
        if len(peaks_test) > 3:
            peaks_test.pop(0)
        if len(peaks_test) == 3:
            if peaks_test[1] > peaks_test[0]:
                if peaks_test[1] > peaks_test[-1]:
                    peaks_list.append(i-1)
        if i == len(data)-1:
            if peaks_test[-1] > peaks_test[1]:
                peaks_list.append(i)

    return peaks_list

def valleys(data):
    valleys_test = []
    valleys_list = []
    for i, value in enumerate(data):
        valleys_test.append(value)
        if len(valleys_test) > 3:
            valleys_test.pop(0)
        if len(valleys_test) == 3:
            if valleys_test[1] < valleys_test[0]:
                if valleys_test[1] < valleys_test[-1]:
                    valleys_list.append(i-1)

    return valleys_list

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

print(peaks(data))
print(valleys(data))

top = len(data)
for x in top:
    if x == top:
        print('x')
    else:
        print(' ')
    top += -1