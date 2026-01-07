import streamlit as st
from points import points

def login():
    login_google = st.button("Vincule sua conta Google", help="Após realizar o login via Google, a página será recarregada e você precisará logar novamente na Twitch.")
    if login_google:
        st.login()


def register_google_infos():
    new_tmw_user = st.session_state["tmw_user"]
    new_tmw_user["email"] = st.user.email
    new_tmw_user['youtube'] = st.user.sub
    new_tmw_user['customer_name'] = st.user.name
    resp = points.update_user_points(**new_tmw_user)
    if resp.status_code != 200:
        st.error("Erro ao vincular sua conta. Entre em contato conosco.")
        return False
    
    return True

def remove_google_infos():
    logout_google = st.button("Desvincular Google")
    if logout_google:
        new_tmw_user = st.session_state["tmw_user"]
        new_tmw_user["email"] = ""
        new_tmw_user['youtube'] = ""
        new_tmw_user['customer_name'] = ""
        resp = points.update_user_points(**new_tmw_user)
    
        if resp.status_code == 200:
            st.logout()
            st.success("Conta google desvinculada com sucesso.")