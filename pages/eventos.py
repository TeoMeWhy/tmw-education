import streamlit as st

from sqlalchemy import orm

from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_calendar(db:orm.Session):
    twitch_login.twitch_login(db)
    
    txt = """
    Confira os eventos que estarei presente durante o ano de 2026.
    """

    st.markdown(txt)


    table = """
    |Evento| Data | Cidade/UF | Palestra/Keynote |
    |:---|:---:|:---:|:---:|
    |[Python Sul](https://sul.python.org.br/)|01/05 - 03/05|Londrina/PR|Keynote|
    |[The Developer's Life Weekend 2026](https://weekend.developerslife.tech/evento/9/the-developers-life-weekend-2026-maringa-pr)|30/05|Maringá/PR|Palestrante|
    |[Caipyra](https://2026.caipyra.python.org.br/)|04/06 - 07/06|São Carlos/SP|❌|
    |[CodeCon Summit](https://eventos.codecon.dev/eventos/codecon-summit-26)|14/08 e 15/08|Curitiba/PR|Palestrante|
    |[Python Brasil 2026](https://2026.pythonbrasil.org.br/)|14/10 - 19/10|Florianopólis/SC|❌|
    """

    st.markdown(table)


show_calendar(db)