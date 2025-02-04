import streamlit as st
import pandas as pd

from cursos import cursos
from login import twitch_login


from databases import models

db = models.SessionLocal()
models.create_tables()

st.set_page_config(page_title="Téo Me Why - 2025")
st.title("Téo Me Why - 2025")
st.markdown("Boas vindas ao nosso calendário de cursos! Por aqui você poderá tanto acompanhar nossa agenda, mas tambem conferir todos conteúdos que geramos em 2025.")

twitch_login.twitch_login(db)
cursos.cursos(db)
