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

    Aqui você encontrará todo o material que tenho disponível na internet em formato de vídeos. Acesse o conteúdo completo, ou navegue entre as diferentes trilhas de conhecimento.
    """)

    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("Siga as trilhas de conhecimento que mais tem interesse!")
            
        with cols[1]:
            cols = st.columns(2)
            with cols[-1]:
                b1 = st.button("Trilhas", use_container_width=True)
                if b1:
                    st.switch_page("./pages/trilhas.py")


    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("Não sabe por onde começar? Realize nosso Plano de Desenvolvimento Individual (PDI)!")
        
        with cols[-1]:
            cols = st.columns(2)
            with cols[-1]:
                b_pdi = st.button("PDI", use_container_width=True)
                if b_pdi:
                    st.switch_page("./pages/pdi.py")


    st.markdown("Você também pode conferir todo material anual:")
        
    with st.container(border=True):
        cols = st.columns(5)
        with cols[1]:
            b2 = st.button("2024", use_container_width=True)
            if b2:
                st.switch_page("./pages/material_2024.py")
        with cols[3]:
            b1 = st.button("2025", use_container_width=True)
            if b1:
                st.switch_page("./pages/material_2025.py")



def main():
    load_skills()
    home()

if __name__ == "__main__":
    main()
    