import streamlit as st

from databases import models
from login import twitch_login

db = models.SessionLocal()
models.create_tables()

st.set_page_config(page_title="TMW - Education", page_icon="📘", initial_sidebar_state="collapsed")


def home():

    twitch_login.twitch_login(db)

    with open("./home.md") as openfile:
        txt = openfile.read()
    st.markdown(txt)

    with st.container(border=True):
        row1 = st.columns(3, vertical_alignment="center")
        row2 = st.columns(3)
        
        with row1[0]:
                st.markdown("Confira nosso cursos futuros e que já aconteceram durante este ano.")
            
        with row2[0]:
            cols = st.columns(3)
            with cols[1]:
                b1 = st.button("2025")
                if b1:
                    st.switch_page("./pages/cursos_2025.py")

        with row1[1]:
            st.markdown("Aqui você entra tudo que rolou em 2024, cursos e projetos")
            
        with row2[1]:
            cols = st.columns(3)
            with cols[1]:
                b2 = st.button("2024")
                if b2:
                    st.switch_page("./pages/cursos_2024.py")

        with row1[2]:
            st.markdown("Todo material de todos os ano!!")
            
        with row2[2]:
            cols = st.columns(3)
            with cols[1]:
                b3 = st.button("Tudo")
                if b3:
                    st.switch_page("./pages/cursos_2025.py")


    st.markdown("Caso esteja em dúvida por onde seguir, realize nosso Plano de Desenvolvimento Individual (PDI) para escolher a trilhar correta.")

def main():
    home()

if __name__ == "__main__":
    main()
    