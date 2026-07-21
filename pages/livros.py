import streamlit as st

from sqlalchemy import orm

from conteudo import livros

from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_livros(db:orm.Session):
    twitch_login.twitch_login(db)
    
    txt = """
    Lista de livros organizada por tema dentro da área de dados e tecnologia.
    
    Mantemos essa lista atualizada, bem como suas marcações de desconto.
    
    Confira a lista completa abaixo:
    """

    st.markdown(txt)

    livros.livros()

show_livros(db)