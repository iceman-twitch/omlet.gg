import requests
import time
import threading
import sys

class Bot:
    def __init__( self, a, b ):
        self.a = a
        self.b = b
        self.s=requests.Session()
        self.success=False


    
    def reg( self ):
        data= {
            "cpass": self.b,
            "email": "",
            "omid": self.a,
            "pass": self.b
        }
        url = self.s.get("https://idp.omlet.me/auth")

        url = url.url
        self.s.post(url,data=data)
        
if sys.argv[1:]:
    name=sys.argv[1:]
    name=sys.argv[1:]
    name= str(name)
    name=name.replace('[','')
    name=name.replace(']','')
    name=name.replace("'","")
    a=Bot(name,"username")
    a.reg()
else:
    print("Missing Username")
    time.sleep(2)
