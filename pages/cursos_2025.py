import streamlit as st
from sqlalchemy import orm

from cursos import cursos
from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def cursos_2025(db:orm.Session):
    st.set_page_config(page_title="Téo Me Why - 2025")
    st.title("Téo Me Why - 2025")
    st.markdown("Boas vindas ao nosso calendário de cursos! Por aqui você poderá tanto acompanhar nossa agenda, mas tambem conferir todos conteúdos que geramos em 2025.")

    cursos.cursos(db)

cursos_2025(db)