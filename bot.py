import requests
import time
import threading
import sys

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bot:
    def __init__( self, a, b ):
        self.a = a
        self.b = b
        self.s=requests.Session()
        self.success=False
        self.driver=0
        self.stream="https://omlet.me/stream/username"
        self.like="https://omlet.gg/photo/eyJhIjoiWlY4VUtMTVZFVVFYSVRVUTJNMU8iLCJpZCI6IlhndVJacVgrNlpEeFFNOTUiLCJ0IjoiU2NyZWVuU2hvdCJ9"
    def get_id( self, get_url ):
        url = get_url
        cut1 = url
        cut2=cut1.split('k=')
        cut3=cut2[1].split('&')
        return cut3[0]

    
    def Browser_Quit( self ):
        time.sleep(3)
        self.driver.close()
        exit()

    def Browser_Login( self ):
        self.driver = webdriver.Chrome()
        
        self.driver.implicitly_wait(55)

        self.driver.get(self.stream)

        centre = self.driver.find_element_by_xpath("//*[@id='omlet-bar']/div[2]/div[2]") 
        hover = ActionChains(self.driver).move_to_element(centre)
        hover.perform()
        centre.click()

        login = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/a/button")
        login.click()
        self.driver.execute_script(f'var element = document.getElementById("omid"); element.value = "{self.a}";')
        self.driver.execute_script(f'var element = document.getElementById("pass"); element.value = "{self.b}";')
        
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/form/button"))).click()
        # login = self.driver.find_element_by_xpath("/html/body/div/div[2]/form/button")
        # login = self.driver.find_element_by_xpath("/html/body/div/div[2]/form/button")
        # login.click()
        print("Login")
        self.driver.find_element_by_xpath("/html/body").send_keys(Keys.CONTROL + 't')
        
        # self.driver.execute_script('chrome.windows.create({"url": "https://omlet.gg/stream/username", "incognito": true});')
    def Browser_Follow( self ):

        follow = self.driver.find_element_by_xpath('//*[@id="user-profile"]/div/div[2]/div/div[3]/div[2]/div[2]/div[1]')
        print("Profile Followed")
        self.Browser_Quit()
    def Browser_Like( self ):

        check = self.driver.find_element_by_xpath('//*[@id="omlet-bar"]/div[2]/div[5]')        
        self.driver.get(self.like)
        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.ID, "myDynamicElement"))
        #     )
            
        # finally:
        #     print("Failed to Like")
        # like = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[6]/div[2]/div[1]')
        # like.click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[6]/div[2]/div[1]'))).click()
        print("Post Liked")
        
        self.Browser_Quit()
    def Browser_Watch( self ):
        self.driver.get(self.stream)


        
        # self.driver.get("https://idp.omlet.me/auth")
        # url = self.driver.current_url
        # id = self.get_id( url )
        # url = url.replace('register', 'login')

        # self.driver.get(url)
        # self.driver.execute_script(f'var element = document.getElementById("omid"); element.value = "{self.a}";')
        # self.driver.execute_script(f'var element = document.getElementById("pass"); element.value = "{self.b}";')
        
                   
if sys.argv[1:]:
    name=sys.argv[1:]
    name= str(name)
    name=name.replace('[','')
    name=name.replace(']','')
    name=name.replace("'","")
    a = Bot(name, "username")
    a.Browser_Login()
    # a.Browser_Like()
    # a.reg()


    i=0
    while True:
        i=i+1
        if i==500:
            i=500
        if i==1000:
            i=0
else:
    print("Missing Username")
