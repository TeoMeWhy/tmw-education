import streamlit as st
from sqlalchemy import orm

from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_cursos_2026(db:orm.Session):
    twitch_login.twitch_login(db)
    st.markdown("Boas vindas ao nosso calendário de cursos! Por aqui você poderá tanto acompanhar nossa agenda, mas tambem conferir todos conteúdos que geramos em 2026.")

    st.markdown("""

    |Conteúdo| Descrição | Tipo | Data |
    |---|---|---|---|
    |[Introdução a Go](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=NzExazg2MXRxdnR2MnVvaDgyZmFzazdoMThfMjAyNjAxMTlUMTIwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL)|Curso introdutório da sintaxe e particularidades da linguagem Go, com uma visão de uma pessoa de Dados.| Curso | 19/01/2026 9AM |
    |[Plataforma Machine Learning](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=NW5tYWM5cWY2MzA4OWNkc3VlZjRodjRuMHFfMjAyNjAyMDJUMTIwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL)|Construção de uma plataforma de ML para simplificar deploy e monitoramento de modelos| Projeto | 02/02/2026 9AM |
    |[Fórmula 1](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=M29hZ25pNG10bmIzYm5vNjBjYmM2dXZyazRfMjAyNjAyMjNUMTIwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL)|Criação de Lakehouse na Nekt para dados da Fórmula 1| Projeto | 23/02/2026 9AM |
    |[Dota2](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=NnVpNGVjYWN1OTY4ZXEycTA0aW0ybWtkNjFfMjAyNjAzMzBUMTIwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL)|Coleta, armazenamento e processamento de dados para criação de Dashboards e Modelos de ML| Projeto | 30/03/2026 9AM |
    |Fogo Cruzado | Uso de dados abertos de confrontos armados para análises e modelos preditivos | Projeto | - |
    |Projeto de IoT | Projeto para coleta de dados usando dispositivos como esp32 e raspberry pi | Projeto | - |
                
    """)
    
show_cursos_2026(db)