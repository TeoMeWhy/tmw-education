import requests

import os

def get_retro(uuid, name):
    uri = os.getenv("RETRO_URI")
    resp = requests.get(f"{uri}/retro?name={uuid}&name={name}&source=streamlit")
    if resp.status_code == 202:
        return resp.json()
    else:
        print(resp.text)
        return False