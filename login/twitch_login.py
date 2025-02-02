import requests
import streamlit as st

from requests_oauthlib import OAuth2Session


import settings

def twitch_login():

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
            st.session_state["token"] = token_response["access_token"]
        except:
            print(token_response)

    if "token" not in st.session_state:
        auth_url, state = twitch.authorization_url(settings.TWITCH_AUTHORIZATION_BASE_URL)
        st.session_state["state"] = state
        st.warning("Para ter uma experiência melhor, salvando o progresso de seus estudos, realize o login com a Twitch")
        st.markdown(f"[Clique aqui para entrar com Twitch]({auth_url})")

    else:
        headers = {
            "Authorization": f"Bearer {st.session_state['token']}",
            "Client-Id": settings.TWITCH_CLIENT_ID,
        }
        user_response = requests.get(settings.TWITCH_USER_URL, headers=headers).json()

        print(user_response)
        
        if "data" in user_response and len(user_response["data"]) > 0:
            user = user_response["data"][0]
            st.success(f"Login bem-sucedido! Bem-vindo, {user['display_name']} 👋")