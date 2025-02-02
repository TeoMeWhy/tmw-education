import streamlit as st
import requests

import settings
from cursos import cursos
from login import twitch_login


st.title("Téo Me Why - 2025")
st.markdown("Boas vindas ao nosso calendário de cursos! Por aqui você poderá tanto acompanhar nossa agenda, mas tambem conferir todos conteúdos que geramos em 2025.")

twitch_login.twitch_login()

cursos.cursos()