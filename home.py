import streamlit as st

from databases import models
from login import twitch_login

db = models.SessionLocal()
models.create_tables()



def home():

    st.markdown("""
    <style>
        .center-button {
            display: flex;
            justify-content: center;
        }
    </style>
    """, unsafe_allow_html=True)
    

    twitch_login.twitch_login(db)

    with open("./home.md") as openfile:
        txt = openfile.read()
    st.markdown(txt)

    with st.container(border=True):
        row1 = st.columns(3)
        row2 = st.columns(3)
        
        with row1[0]:
                st.markdown("Confira nosso cursos futuros e que já aconteceram durante este ano.")
            
        with row2[0]:
            st.markdown('<div class="center-button">', unsafe_allow_html=True)
            b1 = st.button("2025")
            st.markdown('</div>', unsafe_allow_html=True)
            if b1:
                st.switch_page("./pages/cursos_2025.py")

        with row1[1]:
            st.markdown("Aqui você entra tudo que rolou em 2024, cursos e projetos")
            
        with row2[1]:
            st.markdown('<div class="center-button">', unsafe_allow_html=True)
            b2 = st.button("2024")
            st.markdown('</div>', unsafe_allow_html=True)
            if b2:
                st.switch_page("./pages/cursos_2025.py")

        with row1[2]:
            st.markdown("Todo material de todos os ano!!")
            
        with row2[2]:
            st.markdown('<div class="center-button">', unsafe_allow_html=True)
            b3 = st.button("Tudo")
            st.markdown('</div>', unsafe_allow_html=True)
            if b3:
                st.switch_page("./pages/cursos_2025.py")


    st.markdown("Caso esteja em dúvida por onde seguir, realize nosso Plano de Desenvolvimento Individual (PDI) para escolher a trilhar correta.")

def main():
    home()

if __name__ == "__main__":
    main()
    