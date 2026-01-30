import streamlit as st
from sqlalchemy import orm

from conteudo.ano_2026.cursos import cursos_2026
from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()


def show_cursos_2026(db:orm.Session):
    twitch_login.twitch_login(db)
    st.markdown("Boas vindas ao nosso calendário de cursos! Por aqui você poderá tanto acompanhar nossa agenda, mas tambem conferir todos conteúdos que geramos em 2026.")

    cursos_2026(db)

    st.markdown("""
    ---
                
    ### Calendário

    |Conteúdo| Descrição | Tipo | Data |
    |---|---|:---:|:---:|
    |[Plataforma Machine Learning](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=NW5tYWM5cWY2MzA4OWNkc3VlZjRodjRuMHFfMjAyNjAyMDJUMTIwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL)|Construção de uma plataforma de ML para simplificar deploy e monitoramento de modelos| Projeto | 02/02/2026 9AM |
    |[Fórmula 1](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=M29hZ25pNG10bmIzYm5vNjBjYmM2dXZyazRfMjAyNjAyMjNUMTIwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL)|Criação de Lakehouse na Nekt para dados da Fórmula 1| Projeto | 23/02/2026 9AM |
    |AI for Good / Nomad Digital|Bate papo com [Nelson Buainain](http://linkedin.com/in/nelson-buainain)  | Mesa dos Magos | 23/02/2026 10AM |
    |Decolonize AI|Bate papo com [Nina da Hora](https://www.linkedin.com/in/ninadahora/) | Mesa dos Magos | 21/03/2026 10AM |
    |[Dota2](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=NnVpNGVjYWN1OTY4ZXEycTA0aW0ybWtkNjFfMjAyNjAzMzBUMTIwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL)|Coleta, armazenamento e processamento de dados para criação de Dashboards e Modelos de ML| Projeto | 30/03/2026 9AM |
    |Panorama da AI|Bate papo com [Caio Dallaqua](http://linkedin.com/in/caiodallaqua) | Mesa dos Magos | 25/04/2026 10AM |
    |Fogo Cruzado | Uso de dados abertos de confrontos armados para análises e modelos preditivos | Projeto | - |
    |Projeto de IoT | Projeto para coleta de dados usando dispositivos como esp32 e raspberry pi | Projeto | - |

    """)
    
show_cursos_2026(db)