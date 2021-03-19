"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

import re
import matplotlib.pyplot as plt
from datetime import datetime

data = {}

def init():
    with open("class_Binary_Beasts/Students/John/python/lab17-content.txt", "r") as file:
        text = file.read()

    text = re.split(" |\n", text)
    text = list(filter(None, text))

    i = 0
    while i < len(text):
        if i % 26 == 0:
            data[text[i]] = int(text[i + 1])
        i += 1
        
def run_version2():
    totals = list(data.values())
    dates = list(data.keys())
    
    def calculate_mean():
        return sum(totals) / len(totals)
    
    def calculate_variance(mean):
        sq_dev = 0
        for x in totals:
            sq_dev += (x - mean) ** 2
        return sq_dev / len(totals)
    
    def find_day_most_rain():
        m = max(totals)
        
        idx = totals.index(m)
        return dates[idx]
    
    print("Mean: ")
    mean = calculate_mean()
    print(mean)
    print("Variance: ")
    var = calculate_variance(mean)
    print(var)
    day = find_day_most_rain()
    print("Day with most rain: ")
    print(day)
    

#Version 3

def run_version3():
    totals = list(data.values())
    dates = list(data.keys())
    
    x_values = []
    y_values = []

    for d in dates:
        date = datetime.strptime(d, "%d-%b-%Y")
        x_values.append(date)
    for t in totals:
        y_values.append(t)
    plt.plot(x_values, y_values)
    plt.show()


#Version 4

#Data not available to complete lab

versions = [run_version2, run_version3]

while True:
    
    init()
    
    strategy = 0

    print('Welcome. You can type "done" at any time to exit.')
    
    m = len(versions) + 1

    while strategy not in range(2, m + 1):
        try:
            strategy = input(f"Which version would you like to run: 2 - {m}")
            if strategy == "done":
                break
            strategy = int(strategy)
        except:
            continue
        if strategy == "done":
            break

    strategy = versions[strategy - 2]

    strategy()
    