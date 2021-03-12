"""

all codes are written and created by John Robson Wed Mar 10, 2021

"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Version 1


def run_version1():

    peaks = []
    valleys = []
    all = []
    
    def find_peaks():
        i = 0
        while i < len(data):
            if i == 0 or i == len(data) - 1:
                i += 1
            else:
                if data[i - 1] < data[i] and data[i + 1] < data[i]:
                    peaks.append(i)
                    all.append(i)
                i += 1

    def find_valleys():
        i = 0
        while i < len(data):
            if i == 0 or i == len(data) - 1:
                i += 1
            else:
                if data[i - 1] > data[i] and data[i + 1] > data[i]:
                    valleys.append(i)
                    all.append(i)
                i += 1
    
    find_peaks()
    find_valleys()
    print("Peaks: ")
    print(peaks)
    print("Valleys: ")
    print(valleys)
    print("Peaks and Valleys: ")
    print(all)

# Version 2


def run_version2(layout):

    def draw_horizontal(data):
        for i in data:
            print(str(i) + ": " + "X " * i)

    def draw_vertical(data):
        h = max(data) + 5  # add padding for graphs
        while h > -1:
            buf = ""
            for i in data:
                if h == 0:
                    buf += str(i) + " "
                else:
                    if i >= h:
                        buf += "X "
                    else:
                        buf += "  "
            print(buf)
            h -= 1

    if layout == "h":
        draw_horizontal(data)
    elif layout == "v":
        draw_vertical(data)
    else:
        draw_horizontal(data)
        draw_vertical(data)


# Version 3

def run_version3(layout):

    def draw_horizontal(data):
        buf = ""
        bar = 0
        for i in data:
            diff = 0
            if i > bar:
                bar = i
            buf = str(i) + ": " + "X " * i
            if i < bar:
                diff = bar - i
            buf += "O " * diff
            print(buf)

    def draw_vertical(data):
        h = max(data) + 5  # add padding for graphs
        while h > -1:
            buf = ""
            bar = 0
            for i in data:
                if i > bar:
                    bar = i
                if h == 0:
                    buf += str(i) + " "
                else:
                    if i >= h:
                        buf += "X "
                    elif i < bar and bar >= h:
                        buf += "O "
                    else:
                        buf += "  "
            print(buf)
            h -= 1


    if layout == "h":
        draw_horizontal(data)
    elif layout == "v":
        draw_vertical(data)
    else:
        draw_horizontal(data)
        draw_vertical(data)


versions = [run_version1, run_version2, run_version3]

while True:
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')

    while strategy < 1 or strategy > 3:
        strategy = int(input("Which version would you like to run: 1 - 3"))
        if strategy == "done":
            break
        
    if strategy == "done":
        break
    
    choice = strategy
    strategy = versions[strategy - 1]
    
    layout = ""
    
    if choice != 1:
        print("Do you want to print the horizontal graph, vertical graph, or both?")
        while layout != "h" and layout != "v" and layout != "b":
            layout = input('Enter "h" for horizontal, "v" for vertical, or "b" for both').lower()
            strategy(layout)
    else:
        strategy()