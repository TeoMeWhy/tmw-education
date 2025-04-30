import pandas as pd
import streamlit as st

from databases import models
from login import twitch_login

db = models.SessionLocal()
models.create_tables()

st.set_page_config(page_title="TMW - Education", page_icon="🧙‍♂️", initial_sidebar_state="collapsed")

st.cache_resource()
def load_skills():
    if db.query(models.Skill).count() == 0:
        df_skills = pd.read_csv("data/skills.csv", sep=";")
        models.ingest_skills(db, df_skills)

    if db.query(models.RoleSkills).count() == 0:
        df_role_skills = pd.read_csv("data/role_skills.csv", sep=";")
        models.ingest_role_skill(db, df_role_skills)


def home():

    twitch_login.twitch_login(db)

    st.markdown("# Boas vindas")

    st.image("assets/banner_home.png")

    st.markdown("""
                
    ## Plataforma de cursos Téo Me Why

    Por aqui você encontrará todo o material que tenho disponível na internet, principalmente em formato de vídeos. Você pode conferir o conteúdo completo, ou navegar entre as diferentes trilhas de conhecimento.
    """)

    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("Siga as trilhas de conhecimento que mais tem interesse!")
            
        with cols[1]:
            cols = st.columns(3)
            with cols[-1]:
                b1 = st.button("Trilhas")
                if b1:
                    st.switch_page("./pages/trilhas.py")


    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("Caso esteja em dúvida por onde seguir, realize nosso Plano de Desenvolvimento Individual (PDI) para escolher a trilhar correta.")
        
        with cols[-1]:
            cols = st.columns(3)
            with cols[-1]:
                b_pdi = st.button("PDI")
                if b_pdi:
                    st.switch_page("./pages/pdi.py")


    st.markdown("Você também pode conferir todo material separo anualmente:")
        
    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("Confira nossos cursos futuros e que já aconteceram durante este ano.")
            
        with cols[1]:
            cols = st.columns(3)
            with cols[-1]:
                b1 = st.button("2025")
                if b1:
                    st.switch_page("./pages/material_2025.py")

    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("Aqui você encontra tudo que rolou em 2024, cursos e projetos")
            
        with cols[1]:
            cols = st.columns(3)
            with cols[-1]:
                b2 = st.button("2024")
                if b2:
                    st.switch_page("./pages/material_2024.py")




def main():
    load_skills()
    home()

if __name__ == "__main__":
    main()
    