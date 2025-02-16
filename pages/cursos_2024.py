import streamlit as st
from sqlalchemy import orm

from cursos.cursos_2024.cursos import cursos_2024
from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_cursos_2024(db:orm.Session):
    st.set_page_config(page_title="Téo Me Why - 2024")
    st.title("Téo Me Why - 2024")
    twitch_login.twitch_login(db)
    cursos_2024(db)

show_cursos_2024(db)