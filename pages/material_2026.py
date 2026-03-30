import streamlit as st
from sqlalchemy import orm

from conteudo.ano_2026.cursos import cursos_2026
from conteudo.ano_2026.projetos import projetos_2026
from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()


def show_cursos_2026(db:orm.Session):
    twitch_login.twitch_login(db)
    st.markdown("Boas vindas ao nosso calendário de cursos! Por aqui você poderá tanto acompanhar nossa agenda, mas tambem conferir todos conteúdos que geramos em 2026.")

    cursos_2026(db)

    projetos_2026(db)

    st.markdown("""
    ---
                
    ### Calendário

    |Conteúdo| Descrição | Tipo | Data |
    |---|---|:---:|:---:|
    |Physical AI|Bate papo com [Daniel Rometo](https://www.linkedin.com/in/infoslack/) | Mesa dos Magos | 25/03/2026 10AM |
    |Fogo Cruzado | Uso de dados abertos de confrontos armados para análises e modelos preditivos | Projeto | - |
    |Projeto de IoT | Projeto para coleta de dados usando dispositivos como esp32 e raspberry pi | Projeto | - |

    """)
    
show_cursos_2026(db)