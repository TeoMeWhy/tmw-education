import pandas as pd
import streamlit as st

from databases import models
from login import twitch_login

db = models.SessionLocal()
models.create_tables()

st.cache_resource(ttl='1d')
def load_skills():
    if db.query(models.Skill).count() == 0:
        df_skills = pd.read_csv("data/skills.csv", sep=";")
        models.ingest_skills(db, df_skills)

    if db.query(models.RoleSkills).count() == 0:
        df_role_skills = pd.read_csv("data/role_skills.csv", sep=";")
        models.ingest_role_skill(db, df_role_skills)

    df_courses = pd.read_csv("data/courses.csv", sep=";")
    models.ingest_courses(db, df_courses, True)
        
    df_courses_eps = pd.read_csv("data/courses_eps.csv", sep=";")
    models.ingest_courses_eps(db, df_courses_eps, True)

    return True


def home():

    twitch_login.twitch_login(db)

    st.image("assets/banner_home.png")

    st.markdown("""
                
    ## Educação que liberta!

    Você acabou de encontrar um espaço dedicado para aprendizado na área de **dados** e **tecnologia**.

    Nossa missão é emancipar o conhecimento, oferencendo cursos gratuitos e projetos práticos para quem nos apoia.
                
    Conheça nossas trilhas de conhecimento e comece sua jornada de aprendizado já!
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


    col1, col2 = st.columns([2,1])
    col1.markdown("""
    ## Apoie quem ensina de graça

    - **Chave Pix**: `pix@teomewhy.org`
    - **LivePix**: [livepix.gg/teomewhy](https://livepix.gg/teomewhy)
    - **GitHub Sponsors**: [github.com/sponsors/TeoMeWhy](https://github.com/sponsors/TeoMeWhy)
    - **ApoiaSe**: [apoia.se/teomewhy](apoia.se/teomewhy)
    - **Membro no YouTube**: [youtube.com/@teomewhy/membership](https://youtube.com/@teomewhy/membership)
    - **Sub na Twitch**: [twitch.tv/teomewhy](https://twitch.tv/teomewhy)
    - **Newsletter**: [teomewhy.substack.com](https://teomewhy.substack.com)
    - **Lojinha na Amazon**: [amazon.com.br/shop/teo.calvo](https://www.amazon.com.br/shop/teo.calvo?ref_=cm_sw_r_cp_ud_aipsfshop_MS3WV3HX76NT92FNB5BC)
    """)

    col2.markdown("""
    \\
    \\
    **QR Code para doação via Pix:**
    """)
    col2.image("assets/pix.png", width=200)


def main():
    load_skills()
    home()

main()
