import streamlit as st
from streamlit.components.v1 import html

from sqlalchemy import orm

from conteudo.trilhas import basico_tech, data_science_analytics, data_engineering

from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_trilhas(db:orm.Session):
    twitch_login.twitch_login(db)
    
    txt = """
    Não faz ideia por onde começar em dados e tecnologia?
    Organizamos nosso material de uma maneira sequencial para você aprender tópico por tópico, ferramenta por ferramenta, conceito por conceito.
    
    Vamos explorar o básico em tecnologia, pra depois nos especializarmos.
    
    O conteúdo é composto por aulas (cursos) e projetos. Todos os cursos são gratuitos, e projetos são destinados à apoiadores do nosso canal no YouTube.

    Confira uma sugestão de roadmap abaixo:
    """

    st.markdown(txt)

    with st.expander("Roadmap", expanded=False):
        st.image("assets/fluxograma.png")

    with st.container(border=True):
        basico_tech.basico_tech(db)

    with st.container(border=True):
        data_science_analytics.data_science_analytics(db)

    with st.container(border=True):
        data_engineering.data_engineering(db)


show_trilhas(db)