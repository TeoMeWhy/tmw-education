import streamlit as st
from sqlalchemy import orm

from conteudo.ano_2025.cursos import cursos_2025
from conteudo.ano_2025.projetos import projetos_2025
from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_cursos_2025(db:orm.Session):
    twitch_login.twitch_login(db)
    st.markdown("""
                
    Nosso foco em 2025 foi trazer material didático para sua formação na área de dados.
                
    Seguindo esse material você terá todas as habilidades necessárias para realizar projetos que envolver Análise, Ciência e Engenharia de Dados.
    """)
    
    cursos_2025(db)
    projetos_2025(db)

show_cursos_2025(db)