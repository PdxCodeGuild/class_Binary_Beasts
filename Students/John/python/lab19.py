"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""
import requests

headers = {'Authorization': 'Token token="412e38bbec5d340582da162fa0bb8a2b"'}
keyword = ""
i = 1
page = 1

while True:
    if keyword == "":
        keyword = input("Please enter a keyword to search quotes")
    
    url = "https://favqs.com/api/quotes?page=" + str(page) + "&filter=" + keyword
    
    response = requests.get(url, headers=headers, verify=False)
    
    json = response.json()
    
    quotes = json["quotes"]
    
    quotes_list = []
    for q in quotes:
        quotes_list.append(q["body"])
    
    for q in quotes_list:
        print(str(i) + ": " + q + "\n")
        i += 1
    
    nextP = ""
    
    while json["last_page"] != True:
        nextP = input('Enter "next" for next page or "done" to exit')
        if nextP == "done":
            break
        elif nextP == "next":
            page += 1
            break
    else:
        print("End of quotes")
    
    if nextP != "next":
        again = ""
        while again != "yes" and again != "no":
            again = input("Play Again?")
            if again == "no":
                break
            else:
                keyword = ""
                i = 1
                page = 1