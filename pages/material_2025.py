import streamlit as st
from sqlalchemy import orm

from conteudo.ano_2025.cursos import cursos_2025
from conteudo.ano_2025.projetos import projetos_2025
from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_cursos_2025(db:orm.Session):
    st.set_page_config(page_title="Téo Me Why - 2025", page_icon="🧙‍♂️")
    st.title("Téo Me Why - 2025")
    twitch_login.twitch_login(db)
    st.markdown("Boas vindas ao nosso calendário de cursos! Por aqui você poderá tanto acompanhar nossa agenda, mas tambem conferir todos conteúdos que geramos em 2025.")
    cursos_2025(db)
    projetos_2025(db)

show_cursos_2025(db)