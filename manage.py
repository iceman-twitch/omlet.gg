import requests
import time
import threading
import sys
import subprocess


def Create_Bot(x):
    name=sys.argv[2:]
    name= str(name)
    name=name.replace('[','')
    name=name.replace(']','')
    name=name.replace("'","")
    name = "username" + name  + str(x)
    subprocess.call(["python","bot.py",name])
    print("Bot (" + name + ") has been created")

def Register_Bot(x):
    name=sys.argv[2:]
    name= str(name)
    name=name.replace('[','')
    name=name.replace(']','')
    name=name.replace("'","")
    name = "username" + name  + str(x)
    subprocess.call(["python","register.py",name])
    print("Bot (" + name + ") has been registered")

def Function_Call(method,number):
    if method in "register":
        t0 = threading.Thread(target=Register_Bot, args=(0,))
        t1 = threading.Thread(target=Register_Bot, args=(1,))
        t2 = threading.Thread(target=Register_Bot, args=(2,))
        t3 = threading.Thread(target=Register_Bot, args=(3,))
        t4 = threading.Thread(target=Register_Bot, args=(4,)) 
        t5 = threading.Thread(target=Register_Bot, args=(5,))
        t6 = threading.Thread(target=Register_Bot, args=(6,))
        t7 = threading.Thread(target=Register_Bot, args=(7,))
        t8 = threading.Thread(target=Register_Bot, args=(8,))
        t9 = threading.Thread(target=Register_Bot, args=(9,))
        t0.start()
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()

        t0.join()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()

    else:
        t0 = threading.Thread(target=Create_Bot, args=(0,))
        time.sleep(1)
        t1 = threading.Thread(target=Create_Bot, args=(1,))
        time.sleep(1)
        t2 = threading.Thread(target=Create_Bot, args=(2,))
        time.sleep(1)
        t3 = threading.Thread(target=Create_Bot, args=(3,))
        time.sleep(1)
        t4 = threading.Thread(target=Create_Bot, args=(4,)) 
        time.sleep(1)
        t5 = threading.Thread(target=Create_Bot, args=(5,))
        time.sleep(1)
        t6 = threading.Thread(target=Create_Bot, args=(6,))
        time.sleep(1)
        t7 = threading.Thread(target=Create_Bot, args=(7,))
        time.sleep(1)
        t8 = threading.Thread(target=Create_Bot, args=(8,))
        time.sleep(1)
        t9 = threading.Thread(target=Create_Bot, args=(9,))
        time.sleep(1)
        t0.start()
        time.sleep(2)
        t1.start()
        time.sleep(2)
        t2.start()
        time.sleep(2)
        t3.start()
        time.sleep(2)
        t4.start()
        time.sleep(2)
        t5.start()
        time.sleep(2)
        t6.start()
        time.sleep(2)
        t7.start()
        time.sleep(2)
        t8.start()
        time.sleep(2)
        t9.start()
        time.sleep(2)

        t0.join()
        time.sleep(2)
        t1.join()
        time.sleep(2)
        t2.join()
        time.sleep(2)
        t3.join()
        time.sleep(2)
        t4.join()
        time.sleep(2)
        t5.join()
        time.sleep(2)
        t6.join()
        time.sleep(2)
        t7.join()
        time.sleep(2)
        t8.join()
        time.sleep(2)
        t9.join()
        

if sys.argv[2:]:
    if sys.argv[1:]:
        number=sys.argv[2:]
        number= str(number)
        number=number.replace('[','')
        number=number.replace(']','')
        number=number.replace("'","")
        method=sys.argv[1:][0]
        method= str(method)
        method=method.replace('[','')
        method=method.replace(']','')
        method=method.replace("'","")
        print(method + " | " + number)
        Function_Call(method,number)
    else:
        print("Missing Arguement")

else:
    print("Missing Arguement")




