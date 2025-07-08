# %%
import os
import requests
import streamlit as st

import time

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

def delete_creature(id):
    url = f"{HEROES_CUBE_URI}/api/v1/creatures/{id}"
    response = requests.delete(url)
    if response.status_code == 200:
        return {"success": "Creature deleted successfully"}
    else:
        return {"error": response.text}

# %%

def show_races(races):
    
    cols = st.columns(len(races))
    for i in range(len(races)):
        with cols[i].container(border=True, height=300):

            row1 = st.columns(1)[0]
            row2 = st.columns(1)[0]
            row3 = st.columns(1)[0]

            row1.markdown(f'### {races[i]["name"]}')
            row2.markdown(races[i]["description"])
            row3.markdown("""
            - **Força**: {mod_strength}
            - **Destreza**: {mod_dexterity}
            - **Inteligência**: {mod_intelligence}
            - **Sabedoria**: {mod_wisdom}
            """.format(**races[i]))
            

def show_classes(classes):
    cols = st.columns(len(classes))
    for i in range(len(classes)):
         with cols[i].container(border=True, height=300):
             
            row1 = st.columns(1)[0]
            row2 = st.columns(1)[0]
            row3 = st.columns(1)[0]

            row1.markdown(f'### {classes[i]["name"]}')

            row2.markdown(classes[i]["description"])

            row3.markdown('''
            - **Força**: {init_strength}
            - **Destreza**: {init_dexterity}
            - **Inteligência**: {init_intelligence}
            - **Sabedoria**: {init_wisdom}
            '''.format(**classes[i]))


def show_create(tmw_id, twitch_name):
    st.error("Você ainda não possui um personagem criado. Deseja criar um?")
            
    races = get_races()["races"]
    classes = get_classes()["classes"]

    tab_race, tab_class = st.tabs(["Raças", "Classes"])
    with tab_race:
        show_races(races)

    with tab_class:
        show_classes(classes)

    col1, col2, _, col4 = st.columns(4)
    raca = col1.selectbox("Escolha uma raça", races, format_func=lambda x: x['name'])
    classe = col2.selectbox("Escolha uma classe", classes, format_func=lambda x: x['name'])
    col4.text("Confirme a criação do personagem:")
    criacao = col4.button("Criar")

    if criacao:
        data = {
            "id":tmw_id,
            "race":raca["name"],
            "class":classe["name"],
            "name":twitch_name,}
        
        response = post_creature(**data)

        if "error" in response:
            st.error(f"Erro ao criar personagem: {response}")
        else:
            st.success("Personagem criado com sucesso!")
            time.sleep(2)
            st.rerun()


def show_char(char):
    st.markdown(f"#### {char['name']}")
    
    col1, col2, col3 = st.columns(3)

    col1.markdown(f'''
    **Raça**: {char['race_name']}
    
    **Classe**: {char['class_name']}''')

    col2.markdown(f'''
    ❤️ **Pontos de Vida**: {char['pts_hit_points']}
    
    ⭐ **Experiência**: {char['pts_experience']}
    
    ✨ **Pontos Habilidade Livres**: {char['pts_skill']}
    ''')

    col3.markdown(f'''    
    💪 **Força**: {char['pts_strength']} (+{char['race']['mod_strength']})
    
    🎯 **Destreza**: {char['pts_dexterity']} (+{char['race']['mod_dexterity']})
    
    🧠 **Inteligência**: {char['pts_intelligence']} (+{char['race']['mod_intelligence']})
    
    📖 **Sabedoria**: {char['pts_wisdom']} (+{char['race']['mod_wisdom']})
    ''')

    if st.button("Excluir personagem"):
        resp = delete_creature(char['id'])
        if "success" in resp:
            st.success("Personagem excluído com sucesso!")
            time.sleep(2)
            st.rerun()
        else:
            st.error(f"Erro ao excluir personagem: {resp['error']}")