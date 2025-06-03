import datetime
import time

from sqlalchemy import orm

import points.points
import streamlit as st
import pandas as pd
import points

from databases import models
from login import twitch_login


def show_profile_infos(db:orm.Session, tmw_id:str)->bool:

    if not tmw_id:
        return False
    
    data = points.points.get_user_points(uuid=tmw_id)[0]
    st.session_state["tmw_user"] = data

    date = datetime.datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_start = date.strftime("%Y-%m-%d %H:%M:%S")

    date = datetime.datetime.strptime(data["updated_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_last = date.strftime("%Y-%m-%d %H:%M:%S")

    col1, col2 = st.columns(2)

    col1.markdown(f"""
    Saldo de pontos: {data["points"]}

    Última iteração: {date_last}

    Acumula pontos desde: {date_start}
    """)
        
    with col2:
        remove_buttom = col2.button("Clique para desvincular seu perfil do ecosistema")
        if remove_buttom:
            if models.remove_tmw_id(db, tmw_id):
                st.success("Usuário desvinculado com sucesso!")
                del st.session_state["tmw_user"]
                time.sleep(1)
                st.rerun()

    return True
    

def integrate_or_create_tmw(user):
    data = points.points.get_user_points(id_twitch=user.platformUserID)
    if len(data) == 1:
        models.integrate_tmw_id(db=db, userID=user.userID, tmwID=data[0]["uuid"])

    else:
        payload = {user.platformName:user.platformUserID}
        data = points.points.create_user_points(**payload)
        models.integrate_tmw_id(db=db, userID=user.userID, tmwID=data["uuid"])

    st.success("Perfil vinculado com sucesso!")
    time.sleep(1)
    st.rerun()



db = models.SessionLocal()


st.set_page_config(page_title="Téo Me Why - Perfil", page_icon="🧙‍♂️")
twitch_login.twitch_login(db)

st.markdown(
"""
# Seu perfil aqui!
"""
)


if 'user' not in st.session_state:
    st.error("Você não está logado. Por favor, faça login para acessar seu perfil.")
    st.stop()

user = st.session_state["user"]
platform_name = user.platformName
platform_user_id = user.platformUserID

tmw_id = models.get_tmw_id(db, user.userID)

if show_profile_infos(db, tmw_id):
    pass

else:
    b = st.button("Clique aqui para vincular seu perfil ao ecossistema")
    if b:
        integrate_or_create_tmw(user)
