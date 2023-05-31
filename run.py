#! /usr/bin/env python3

import os
import requests
import json

fdict = {}
url="http://146.148.95.124/feedback"

for file in os.listdir("/data/feedback"):
    with open("/data/feedback/" + file, "r") as f:
        fdict["title"]=f.readline().strip()
        fdict["name"]=f.readline().strip()
        fdict["date"]=f.readline().strip()
        fdict["feedback"]=f.readline().strip()


#    fdict_json=json.dumps(fdict) 
#    print(fdict_json)
    res = requests.post(url,json=fdict)
    
    if not res.status_code == 201:
        print('Something went wrong')
