import requests
import os

POINTS_URI = os.getenv("POINTS_URI")

def get_user_points(**kwargs):
    url = f"{POINTS_URI}/customers"
    resp = requests.get(url, params=kwargs)
    
    if resp.status_code == 200:
        return resp.json()
    
    else:
        return {}


def create_user_points(**kwargs):
    url = f"{POINTS_URI}/customers"
    resp = requests.post(url, json=kwargs)
    
    if resp.status_code == 201:
        return resp.json()["customer"]
    
    else:
        return resp.json()