import requests
import time
import sys
import threading
import random 
import names
from random_username.generate import generate_username
import omlet_bot
from threading import Thread

# thread_count = 12



servers=[
"35.245.123.216",
# "104.196.232.76",
# "35.227.177.187",
# "34.94.145.176",
# "34.73.218.30",
# "35.245.216.139",
# "35.245.213.142",
# "35.231.44.169",
# "35.202.142.197",
# "35.230.6.83",
# "35.196.231.162",
# "34.83.203.177",
]
thread_count= len(servers)

def Gen():
    # fake = generate_username(1)
    # fake = fake[0]
    fake = names.get_last_name().lower()
    return fake

def Register_Bot(ip):
    link="https://omlet.gg/video/eyJhIjoiUU1FVEJXSVFHWENaVVhOQ1BYSFciLCJpZCI6IlhnL2pjVW9nY0lMdnkwcGUiLCJ0IjoiVmlkZW8ifQ"
    ip = ip
    name=Gen()
    bonus = Gen()
    name = name + bonus
    name = name + random.choice(["__", "_gg", "123", "_pro", "_4123"])
    bonus = name + "_a" + random.choice(["__", ".gg", "123", "_pro", "_123"])
    try:
        
        a = omlet_bot.Bot(name,"username",bonus,ip,link)
        
        a.Browser_Register()
        
        a.Browser_Start()
        a.Browser_Login()
        a.Browser_Report_Post()
        a.Browser_Quit()
        # a.Browser_Watch()
    except:
        # print("Session Failed/Ended")
        pass
        
    #a.Browser_NewTab()
    while True:
        try:
            name=Gen()
            bonus = Gen()
            name = name + bonus
            name = name + random.choice(["__", "_gg", "123", "_pro", "_4123"])
            bonus = name + "_a" + random.choice(["__", ".gg", "123", "_pro", "_123"])
            a = omlet_bot.Bot(name,"username",bonus,ip,link)
            a.Browser_Register()
            a.Browser_Start()
            a.Browser_Login()
            # a.Browser_Watch()
            a.Browser_Report_Post()
            a.Browser_Quit()
        except:
            # print("Session Failed/Ended")
            pass

def Start(ip):
    threads_ = []
    for i in range(0,5):
        threads_.append(Thread(target=Register_Bot,args=(ip,)))
    for thread in threads_:
        time.sleep(2)
        thread.start()
  

threads = []
for i in range(0,thread_count):
    threads.append(Thread(target=Start,args=(servers[i],)))
for thread in threads:
    time.sleep(2)
    thread.start()

