# %%
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

# %%

def show_races(races):
    cols = st.columns(len(races))
    for i in range(len(races)):

        txt = '''
        ### {name}
        

        {description}

        
        - **Força**: {mod_strength}
        - **Destreza**: {mod_dexterity}
        - **Inteligência**: {mod_intelligence}
        - **Sabedoria**: {mod_wisdom}
        
        '''.format(**races[i])

        cols[i].markdown(txt)