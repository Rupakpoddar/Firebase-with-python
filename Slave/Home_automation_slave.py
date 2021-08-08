"""
It is recommended to use the master script and press all the buttons one-by-one
for the first time before using this script. Doing this will add the right
datatypes to the realtime-database and prevent errors while using this script
"""

#############################################
##         Written by Rupak Poddar         ##
#############################################

import requests
import json
import time

######### Your project ID goes here #########
project_ID = "YOUR PROJECT ID GOES HERE"
#############################################

url = "https://"+project_ID+".firebaseio.com/cmd"

def get_loads():
    client = requests.get(url+".json")
    decider = json.loads(client.text)

    if (decider["Device1"] == "ON"):
        #Command if device 1 is on
        print("Device 1 : ON")
    if (decider["Device1"] == "OFF"):
        #Command if device 1 is off
        print("Device 1 : OFF")

    if (decider["Device2"] == "ON"):
        #Command if device 2 is on
        print("Device 2 : ON")
    if (decider["Device2"] == "OFF"):
        #Command if device 2 is off
        print("Device 2 : OFF")

    if (decider["Device3"] == "ON"):
        #Command if device 3 is on
        print("Device 3 : ON")
    if (decider["Device3"] == "OFF"):
        #Command if device 3 is off
        print("Device 3 : OFF")

    if (decider["Device4"] == "ON"):
        #Command if device 4 is on
        print("Device 4 : ON")
    if (decider["Device4"] == "OFF"):
        #Command if device 4 is off
        print("Device 4 : OFF")

    return client.text

while True:
    data = get_loads()
    print("\n\n")
    time.sleep(2)
