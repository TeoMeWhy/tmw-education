import streamlit as st
import requests

import os

def get_retro(uuid, name):
    uri = os.getenv("RETRO_URI")
    resp = requests.get(f"{uri}/retro?id={uuid}&name={name}&source=streamlit")
    if resp.status_code < 400:
        return resp.json()
    else:
        print(resp.text)
        return False