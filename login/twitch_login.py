import requests
from requests_oauthlib import OAuth2Session
from sqlalchemy import orm
import streamlit as st

import configs.settings as settings
from databases import models 

def get_twitch_infos(token:str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": settings.TWITCH_CLIENT_ID,
    }
    user_response = requests.get(settings.TWITCH_USER_URL, headers=headers).json()
    return user_response


def twitch_login(db:orm.Session):

    twitch = OAuth2Session(settings.TWITCH_CLIENT_ID, redirect_uri=settings.REDIRECT_URI)

    if "code" in st.query_params and "token" not in st.session_state:
        code = st.query_params["code"]

        token_response = requests.post(
            settings.TWITCH_TOKEN_URL,
            data={
                "client_id": settings.TWITCH_CLIENT_ID,
                "client_secret": settings.TWITCH_CLIENT_SECRET,
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": settings.REDIRECT_URI,
            },
        ).json()

        try:
            token = token_response["access_token"]
            st.session_state["token"] = token
            twitch_user_data = get_twitch_infos(token)
            user = models.get_or_create_user(db, "twitch", twitch_user_data["data"][0]["id"])
            st.session_state["user"] = user

        except Exception as err:
            pass

    if "token" not in st.session_state:
        auth_url, state = twitch.authorization_url(settings.TWITCH_AUTHORIZATION_BASE_URL)
        st.session_state["state"] = state
        st.warning("Para ter uma experiência melhor, salvando o progresso de seus estudos, realize o login com a Twitch")
        st.markdown(f"[Clique aqui para entrar com Twitch]({auth_url})")

    else:
        data = get_twitch_infos(st.session_state['token'])
        
        if "data" in data and len(data["data"]) > 0:
            twitch_user = data["data"][0]
            print(twitch_user)
            user = models.get_or_create_user(db, "twitch", twitch_user["id"])
            st.session_state["user"] = user
            st.success(f"Login bem-sucedido! Boas vindas, {twitch_user['display_name']} 👋")