#selenium allows python to access sites through chrome and automates it
from selenium import webdriver
#time allows the sleep method to wait x seconds before the next task is run
from time import sleep
#I put my password for my instagram into another python file and imported it from there
from secrets import pw
from selenium.webdriver.common.keys import Keys

#define my Instagram "bot" that will run the process of going to my wifes Instagram page liking 5 of her pics
class Bot():
    #created a links array which allows me to cycle through her pics
    links = []
    #defined two initializers for my login and my wifes username
    def __init__(self):
        self.login('dakotalearnstocode')
        self.like_by_username('Chelseadoingstuff')
    #defined login funtion which takes the username   
    def login(self, usename):
        #used the drive module to set the browser I wanted to use a chrome 
        self.driver = webdriver.Chrome()
        #used the driver.get method to go to Instagrams homepage
        self.driver.get('https://www.instagram.com')
        #wait 5 seconds before moving to the next step to let the log in page load
        sleep(5)
        #used the driver.find_element_by_xpath to input my username and password onto the login page
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys('dakotalearnstocode')
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(pw)
        #used the inspect within Chrome to identify the xpath of the buttons I wanted to use
        login_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        #used the .click() to click the login button
        login_button.click()
        sleep(5)
        #used the .click() to click save log in
        save_login_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button')
        save_login_button.click()
        sleep(5)
        ##used the .click() to click the not now for notifications
        not_now_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_button.click()
    #defined my like_by_username function
    def like_by_username(self, like):
        search_box = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        #used the send_keys() method within selenium select username that wants to be searched for
        search_box.send_keys(like)
        sleep(5)
        search_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a')
        search_button.click()
        sleep(5)
        #defined the picutres tag type the pics used the 'a' tag
        links = self.driver.find_elements_by_tag_name('a')
        #defined a function that looks at all of the pics from links that have '.com/p'
        def condition(link):
            #all of the pics within
            return '.com/p/' in link.get_attribute('href')
        #valid links variable which lists out picturs that have a tag and meet the condition function
        valid_links = list(filter(condition, links))
        #created a for loop to look through 5 pictures on instagram
        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)
        #created a for loop to like each of those 5 pics
        for link in self.links:
            #use driver.get method to get link to the 5 pics
            self.driver.get(link)
            sleep(3)
            #like button, uses click method to click like button on Instagram
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(3)
#define main function            
def main():
    #define my_bot to intialize the bot class
    my_bot = Bot()
#set __name__ equal to __main__ to run the python code
if __name__ == '__main__':
    main()
