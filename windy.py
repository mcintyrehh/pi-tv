import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

#Load env vars
WINDY_API_KEY=os.getenv("WINDY_API_KEY")
nyc_lat=40.71
nyc_long=74.01
km_radius=1000.0

def get_cams():
    windy_url = f"https://api.windy.com/api/webcams/v2/list/country=US?show=webcams:location,image"
    res = requests.get(windy_url, headers={"x-windy-key": WINDY_API_KEY})
    print("windy response: ", json.dumps(res.json(), indent=4))

def get_cam():
    windy_url = f"https://api.windy.com/api/webcams/v2/list?show=webcams:url"
    res = requests.get(windy_url, headers={"x-windy-key": WINDY_API_KEY})
    print("windy cam: ", json.dumps(res.json(), indent=4))

#get_cams()
get_cam()