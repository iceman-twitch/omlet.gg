import requests
import time
import threading
import sys
import subprocess
from os import system, name

menu = {}
menu['1']="Create Bots." 
menu['2']="Register Bots."
menu['3']="!!!!!"
menu['4']="Exit"
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
ans=True
while ans:
    print("""
    1.Create Bots
    2.Register Bots
    3.Dunno
    4.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
        clear()
        number=input("Login ID? ")
        subprocess.call(["start", "/wait", "python", "manage.py","login",number],shell=True)
    elif ans=="2":
        clear()
        number=input("Register ID? ")
        subprocess.call(["start", "/wait", "python", "manage.py","register",number],shell=True)
    elif ans=="3":
        clear()
    elif ans=="4":
        clear()
        ans = None
    else:
        clear()
        print("\n Not Valid Choice Try again")
        time.sleep(1)
        clear()