import os
import requests

import streamlit as st

HEROES_CUBE_URI = os.getenv("HEROES_CUBE_URI", "http://heroes-cube:8080")

def get_races():
    url = f"{HEROES_CUBE_URI}/api/v1/races"
    return requests.get(url).json()

def get_classes():
    url = f"{HEROES_CUBE_URI}/api/v1/classes"
    return requests.get(url).json()

def get_items():
    url = f"{HEROES_CUBE_URI}/api/v1/items"
    return requests.get(url).json()

def post_creature(**params):
    if "class_" in params:
        params["class"] = params.pop("class_")

    url = f"{HEROES_CUBE_URI}/api/v1/creatures"
    response = requests.post(url, json=params)
    if response.status_code == 201:
        return response.json()
    else:
        return {"error": response.text}
    
def get_creature(id):
    url = f"{HEROES_CUBE_URI}/api/v1/creatures/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

def get_creature_damage(id):
    url = f"{HEROES_CUBE_URI}/api/v1/creatures/{id}/damage"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}


def delete_creature(id):
    url = f"{HEROES_CUBE_URI}/api/v1/creatures/{id}"
    response = requests.delete(url)
    if response.status_code == 200:
        return {"success": "Creature deleted successfully"}
    else:
        return {"error": response.text}


def create_inventory_item(inventory_id, item_id):
    url = f"{HEROES_CUBE_URI}/api/v1/inventory/{inventory_id}/item"
    data = {"id": item_id}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return True
    else:
        st.warning(response.text)
        return False


def remove_item_inventory(inventory_id, item_id):
    url = f"{HEROES_CUBE_URI}/api/v1/inventory/{inventory_id}/item/{item_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        return True
    else:
        st.warning(response.text)
        return False
