from QUERYfunc import *
from READfunc import *
from WRITEfunc import *
from ERRORthrow import *
from script import *
import time
import requests
import json

#reset_json()

timesRan = 0
#ip = requests.get('https://api.ipify.org').text
#print('My public IP address is: {}'.format(ip))

while (True):  
  mainQ()
  time.sleep(2)
  timesRan = timesRan + 1
  print("TIMESRAN:" + str(timesRan))



