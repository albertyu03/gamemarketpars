from IPfunc import *
from script import *
import time
import requests
import json

#reset_json()

timesRan = 0


update_ip()

while (True):  
  mainQ()
  time.sleep(2)
  timesRan = timesRan + 1
  print("TIMESRAN:" + str(timesRan))



