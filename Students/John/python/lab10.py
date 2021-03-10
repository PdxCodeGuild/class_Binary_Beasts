#Version 1

def runVersion1():
    
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    
    def peaks(data):
        peaks = []
        i = 0
        while i < len(data):
            if i == 0 or i == len(data) - 1:
                i += 1
            else:
                if data[i - 1] < data[i] and data[i + 1] < data[i]:
                    peaks.append(i)
                i += 1
        return(peaks)
            
    def valleys(data):
        valleys = []
        i = 0
        while i < len(data):
            if i == 0 or i == len(data) - 1:
                i += 1
            else:
                if data[i - 1] > data[i] and data[i + 1] > data[i]:
                    valleys.append(i)
                i += 1
        return(valleys)
    
    def peaksAndValleys(data):
        all = []
        i = 0
        while i < len(data):
            if i == 0 or i == len(data) - 1:
                i += 1
            else:
                if data[i - 1] > data[i] and data[i + 1] > data[i]:
                    all.append(i)
                if data[i - 1] < data[i] and data[i + 1] < data[i]:
                    all.append(i)
                i += 1
        return(all)
        
    print(peaks(data))
    print(valleys(data))
    print(peaksAndValleys(data))

#Version 2

def runVersion2():
    
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    
    def drawHorizontal(data):
        for i in data:
            print(str(i) + ": " + "X " * i)
            
    def drawVertical(data):
        h = max(data)
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
            
    drawHorizontal(data)
    drawVertical(data)
    
runVersion2()