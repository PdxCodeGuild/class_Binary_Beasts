#Lab 10
#define the functions for the peaks and valleys game
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    for i,j in enumerate(data):
        if j > data[i+1] and j > data[i-1]:
            print(f'{i} is a peak')
def valleys(data):
    for i,j in enumerate(data):
        if j < data[i+1] and j < data[i-1]:
            print(f'{i} is a valley')
def peaks_and_valleys(data):
    return peaks + valleys
peaks(data)
valleys(data)
peaks_and_valleys(data)