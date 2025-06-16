import requests
import time
import sys
import threading
import random 
import names
from random_username.generate import generate_username
import omlet_bot
from threading import Thread



######################
### SELENOID SERVERS :->
servers=[
"35.245.123.216",
"104.196.232.76",

"35.227.177.187", ### NOT WORKING
"34.94.145.176", ### NOT WORKING
"34.73.218.30", ### NOT WORKING
"35.245.216.139", ### NOT WORKING

"35.245.213.142",
"35.231.44.169",
"35.202.142.197",

"35.196.231.162",
"34.83.203.177",

# "35.230.6.83", ### NOT WORKING
]
#########################
thread_count= len(servers)

thread_count = 1

like_="https://omlet.gg/photo/eyJhIjoiT1NPVDAwNFBUNkRBMUxWSkVQTzYiLCJpZCI6IlhobGJrWUpvWU0yUVZCRlkiLCJ0IjoiU2NyZWVuU2hvdCJ9"
report_="https://omlet.gg/video/eyJhIjoiUU1FVEJXSVFHWENaVVhOQ1BYSFciLCJpZCI6IlhnL2pjVW9nY0lMdnkwcGUiLCJ0IjoiVmlkZW8ifQ"
follow_="https://omlet.gg/profile/username"
watch_="https://omlet.gg/stream/username"

def Gen():
    # fake = generate_username(1)
    # fake = fake[0]
    fake = names.get_last_name().lower()
    return fake



def Register_Bot(ip):
    link=watch_
    ip = ip
    name=Gen()
    bonus = Gen()
    name = name + bonus
    name = name + random.choice(["_", "_g", "3", ".o", "_4"])
    bonus = name + "_a" + random.choice(["__", ".gg", "123", "_pro", "_123"])
    try:
        
        a = omlet_bot.Bot(name,"username",bonus,ip,link)
        
        a.Browser_Register()
        # a.Browser_Start()
        a.Browser_Start_Local()
        a.Browser_Login()
        # a.Browser_Like()
        time.sleep(10)
        # a.driver.get(report_)
        # a.Browser_Report_Post()
        # time.sleep(2)
        # a.driver.get(follow_)
        # a.Browser_Follow()
        # time.sleep(2)
        # a.driver.get(watch_)
        a.Browser_Chat()
        time.sleep(2)
        # a.Browser_Watch()
        # a.Browser_Quit()
        a.Browser_NoLoginWatch()
        
    except:
        print("Session Failed/Ended")
        pass
    while True:
        try:
            name=Gen()
            bonus = Gen()
            name = name + bonus
            name = name + random.choice(["_", "_g", "3", ".o", "_4"])
            bonus = name + "_a" + random.choice(["__", ".gg", "123", "_pro", "_123"])
            a = omlet_bot.Bot(name,"username",bonus,ip,link)
            a.Browser_Register()
            a.Browser_Start_Local()
            a.Browser_Login()
            # a.Browser_Like()
            time.sleep(10)
            # a.driver.get(report_)
            # a.Browser_Report_Post()
            # time.sleep(2)
            # a.driver.get(follow_)
            # a.Browser_Follow()
            # time.sleep(2)
            # a.driver.get(watch_)
            a.Browser_Chat()
            time.sleep(2)
            # a.Browser_Watch()
            # a.Browser_Quit()
            a.Browser_NoLoginWatch()
        except:
            print("Session Failed/Ended")
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
