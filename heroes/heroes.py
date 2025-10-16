# %%
import streamlit as st

import pandas as pd

import time

from points import points

from .api import *


def validate_item_inventory(items:pd.DataFrame, inventory:pd.DataFrame):
    group_items = items.groupby("type")["id"].count().reset_index()
    items_double = group_items[group_items["id"] > 1]["type"].tolist()
    items_double = ",".join(items_double)
    if len(items_double) > 0:
        txt = "Você está selecionando mais de um item do mesmo tipo: " + items_double
        return txt    

    if inventory.empty:
        return ""
    
    df_join = pd.merge(inventory, items, how='inner', on="type")
    inventory_double = ",".join(df_join["type"].tolist())
    if len(inventory_double) > 0:
        txt = f"Você já possui itens desses tipos: {inventory_double}. Você só pode ter um item de cada tipo no inventário."
        return txt
    
    return ""


def exec_store_sell(tmw_id, items):
    data = points.make_rpg_store_transaction(tmw_id=tmw_id,
                                             items=items)
    
    st.write(data)
    print(data)
    
    resp = points.post_transaction(**data)
    if "error" in resp:
        st.error(f"Erro ao realizar a transação: {resp['error']}")
    
    else:
        for i in items:
            if create_inventory_item(tmw_id, str(i["id"])):
                continue
            else:
                data = points.make_rpg_store_transaction_refound(tmw_id=tmw_id, items=items)
                resp = points.post_transaction(**data)
                st.error(f"Erro ao adicionar item {i['name']} ao inventário: {resp['error']}")
                return False

        st.success("Transação realizada com sucesso!")
        return True


def exec_inventory_sell(tmw_id, items):
    data = points.make_rpg_store_transaction(tmw_id=tmw_id,
                                             items=items,
                                             buyer=False)
    
    resp = points.post_transaction(**data)
    if "error" in resp:
        st.error(f"Erro ao realizar a transação: {resp['error']}")
        return False
    
    for i in items:
        if remove_item_inventory(tmw_id, str(i["id"])):
            continue
        else:
            data = points.make_rpg_store_transaction(tmw_id=tmw_id,
                                             items=items,
                                             buyer=True)
    
            resp = points.post_transaction(**data)
            st.error(f"Erro ao remover item {i['name']} do inventário: {resp['error']}")
            return False

    st.success("Venda realizada com sucesso!")
    return True


def show_race(race):
    st.markdown(f'##### {race["name"]}')
    st.markdown(race["description"])
    st.markdown("""
|Força|Destreza|Inteligência|Sabedoria|
|:---:|:---:|:---:|:---:|
| {mod_strength} | {mod_dexterity} | {mod_intelligence} | {mod_wisdom} | 
        """.format(**race))


def show_races(races):
    for i in range(len(races)):
        st.markdown(f'##### {races[i]["name"]}')
        st.markdown(races[i]["description"])
        st.markdown("""
|Força|Destreza|Inteligência|Sabedoria|
|:---:|:---:|:---:|:---:|
| {mod_strength} | {mod_dexterity} | {mod_intelligence} | {mod_wisdom} | 
        """.format(**races[i]))
       
def show_class(classe):
    st.markdown(f'##### {classe["name"]}')
    st.markdown(classe["description"])
    st.markdown("""
|Força|Destreza|Inteligência|Sabedoria|
|:---:|:---:|:---:|:---:|
| {init_strength} | {init_dexterity} | {init_intelligence} | {init_wisdom} | 
        """.format(**classe))


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
    races = [r for r in races if r['name'] in ['Humano', 'Elfo', 'Anão', 'Hobbit']]

    classes = get_classes()["classes"]

    
    col1, col2 = st.columns(2)
    raca = col1.selectbox("Escolha uma raça", races, format_func=lambda x: x['name'])
    classe = col2.selectbox("Escolha uma classe", classes, format_func=lambda x: x['name'])
    
    show_race(raca)
    show_class(classe)
    
    criacao = st.button("Criar", help="Criar personagem com a raça e classe selecionadas")

    if criacao:
        data = {
            "id":tmw_id,
            "race":raca["name"],
            "class":classe["name"],
            "name":twitch_name,
        }
        
        response = post_creature(**data)

        if "error" in response:
            st.error(f"Erro ao criar personagem: {response}")
        else:
            st.success("Personagem criado com sucesso!")
            time.sleep(1)
            st.rerun()


def show_char(char):
    st.markdown(f"#### {char['name']}")

    damage = get_creature_damage(char['id'])
    
    col1, col2, col3 = st.columns(3)

    col1.markdown(f'''
    **Raça**: {char['race_name']}
    
    **Classe**: {char['class_name']}''')

    col2.markdown(f'''
    ❤️ **Pontos de Vida**: {char['pts_hit_points']}
    
    ⭐ **Experiência**: {char['pts_experience']}
    
    ✨ **Pontos Habilidade Livres**: {char['pts_skill']}

    ⚔️ **Dano Básico**: {damage['base_damage']}

    💫 **Dano Especial**: {damage['special_damage']}
    ''')


    mod_strength = char['race']['mod_strength'] + sum(item['mod_strength'] for item in char['inventory']['items'])
    mod_dexterity = char['race']['mod_dexterity'] + sum(item['mod_dexterity'] for item in char['inventory']['items'])
    mod_intelligence = char['race']['mod_intelligence'] + sum(item['mod_intelligence'] for item in char['inventory']['items'])
    mod_wisdom = char['race']['mod_wisdom'] + sum(item['mod_wisdom'] for item in char['inventory']['items'])

    col3.markdown(f'''    
    💪 **Força**: {char['pts_strength']} (+{mod_strength})
    
    🎯 **Destreza**: {char['pts_dexterity']} (+{mod_dexterity})
    
    🧠 **Inteligência**: {char['pts_intelligence']} (+{mod_intelligence})
    
    📖 **Sabedoria**: {char['pts_wisdom']} (+{mod_wisdom})
    ''')

    if st.button("Excluir personagem"):
        resp = delete_creature(char['id'])
        if "success" in resp:
            st.success("Personagem excluído com sucesso!")
            time.sleep(1)
            st.rerun()
        else:
            st.error(f"Erro ao excluir personagem: {resp['error']}")


def show_inventory(char):
    st.markdown("### Inventário")
    df = pd.DataFrame(char["inventory"]['items'])
    if df.empty:
        st.markdown("Você ainda não possui itens no inventário.")
    else:
        show_items(char["inventory"]['items'])
        names = df["name"].tolist()
        items_selected = st.multiselect("Selecione os itens que deseja comprar:", names)
        df_items_selected = df[df["name"].isin(items_selected)].copy()
        total_price = df_items_selected["price"].sum()
        st.markdown(f"**Preço total:** {total_price} cubos")

        if not df_items_selected.empty:
            if st.button("Vender"):
                if exec_inventory_sell(char["id"], df_items_selected.to_dict(orient="records")):
                    time.sleep(1)
                    st.rerun()


def show_store(char):
    st.markdown("### Loja de Itens")
    items = get_items()["items"]

    show_items(items)

    df = pd.DataFrame(items)
    names = df["name"].tolist()
    items_selected = st.multiselect("Selecione os itens que deseja comprar:", names)


    df_items_selected = df[df["name"].isin(items_selected)].copy()
    total_price = df_items_selected["price"].sum()
    st.markdown(f"**Preço total:** {total_price} cubos")

    txt = validate_item_inventory(df_items_selected, pd.DataFrame(char["inventory"]['items']))
    if txt != "":
        st.error(txt)
    
    elif total_price > st.session_state["tmw_user"]["points"]:
        st.error("Você não possui cubos suficientes para comprar esses itens.")

    elif not df_items_selected.empty:
        if st.button("Comprar"):
            items_payload = df_items_selected.to_dict(orient="records")
            if exec_store_sell(char["id"], items_payload):
                time.sleep(1)
                st.rerun()


def show_items(items):
    df = pd.DataFrame(items)
    df["id"] = df["id"].astype(int)
    df.sort_values(by="id", inplace=True)

    df.columns = ["ID",
                    "Nome",
                    "Descrição",
                    "Categoria",
                    "Tipo",
                    "Peso",
                    "Preço",
                    "Dano",
                    "Força",
                    "Destreza",
                    "Inteligência",
                    "Sabedoria"]
    
    df = df.drop("ID", axis=1)
    
    st.dataframe(df, hide_index=True, use_container_width=True)