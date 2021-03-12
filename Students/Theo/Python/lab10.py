numbers = [6, 10, 0, 3, 4, 5, 3, 10, 5, 7, 2, 10, 2, 3, 10, 5, 6, 6, 0, 5]

index = 0

peaks = []

valleys = []

both = []

blank = ''

def find_peaks():
    if numbers[index] > numbers[index+1] and numbers[index] > numbers[index-1]:
        peaks.append(index)

def find_valleys():
    if numbers[index] < numbers[index+1] and numbers[index] < numbers[index-1]:
        valleys.append(index)

def find_both():
    if numbers[index] > numbers[index+1] and numbers[index] > numbers[index-1]:
        both.append(index)
    elif numbers[index] < numbers[index+1] and numbers[index] < numbers[index-1]:
        both.append(index)


for number in numbers:
    if index > 0 and index < 19:
        find_peaks()
        find_valleys()
        find_both()
    index += 1

print(f'Peaks are at indicies {str(peaks)}')
print(f'Valleys are at indicies {str(valleys)}')
print(f'Peaks and valleys are at indicies {str(both)}')



