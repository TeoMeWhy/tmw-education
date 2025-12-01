import streamlit as st
from sqlalchemy import orm

from conteudo.ano_2024.cursos import cursos_2024
from conteudo.ano_2024.projetos import projetos_2024

from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_cursos_2024(db:orm.Session):
    twitch_login.twitch_login(db)
    
    st.markdown("""
Este ano foi um ano que tomamos coragem para ter dedicação exclusiva ao projeto.
A partir disso, tivemos muitas realizações junto à comunidade, por isso gostaríamos de compartilhar estes feitos.
Nossa motivação não apenas para mostrar o nosso trabalho, mas também engajar novas pessoas aos estudos na área de dados e tecnologia, como também, compartilharem seus avanços, aprendizados e lutas.

Lembramos que o projeto [Téo Me Why](https://teomewhy.org) é parceiro do [Instituto Aaron Swartz](https://institutoasw.org) na luta pela emancipação do conhecimento.

## Sumário

No total, realizamos seis treinamentos para te ajudar nos conhecimentos básicos na área de dados.
Além disso, realizamos seis projetos completamente mão na massa para você aplicar todos conhecimentos adquiridos anteriormente, além de te inspirar a caçar mais dados para crescer o seu portfólio. 
Confira abaixo a lista de tudo isso que você pode e deve aproveitar.
                
""")

    cursos_2024(db)
    projetos_2024(db)
    


show_cursos_2024(db)