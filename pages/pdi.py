import streamlit as st
from sqlalchemy import orm

from databases import models


from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

level_options = ["00. Não esperada", "01. Aprendiz","02. Iniciante","03. Profissional","04. Expert","05. Professor"]

def save(db:orm.Session, map_levels:dict):
    userId = st.session_state["user"].userID
    models.update_or_insert_user_skills(db=db, userID=userId, skills=map_levels)

def show_pdi():
    st.set_page_config(page_title="Téo Me Why - PDI")
    st.title("Téo Me Why - Plano de Desenvolvimento Individual")
    twitch_login.twitch_login(db)

    st.markdown("""
    Responda cada uma das habilidades abaixo para identificar quais são suas fortalezas de pontos a desenvolver.
                
    Com o intuito de auxiliar na escolha de seu nível, considere a tabela abaixo.
                
    | Nível            | Descrição                                                    |
    |---               |---                                                           |
    | 00. Não esperada | Não é esperado esta habilidade                               |
    | 01. Aprendiz     | Não tem conhecimento para fazer solo                         |
    | 02. Iniciante    | Consegue encarar desafios menores mas ainda precisa de apoio |
    | 03. Profissional | Tem autonomia para fazer solo                                |
    | 04. Expert       | Domina o assunto e faz com excelência                        |
    | 05. Professor    | É referência no assunto e compartilha conhecimento           |


    Mas, o primeiro passo é escolher qual será a sua jornada. Selecione abaixo qual a profissão que seja seguir, e o nível que pretender atingir.
    """)

    with st.container(border=True):
        col1, col2 = st.columns(2)
        role = col1.selectbox("Carreira", options=["Data Analyst", "Data Scientist", "Data Engineer"])
        level = col2.selectbox("Nível", options=["Jr.", "Pl.", "Sr.", "Staff", "Principal"])


    results = (db.query(models.RoleSkills, models.Skill)
                .join(models.Skill, models.RoleSkills.skillName == models.Skill.skillName)
                .filter(models.RoleSkills.roleName==role, models.RoleSkills.roleLevel==f"{level} {role}")
                .all())
    
    skills = []

    for role_skill, skill in results:
        line = {"skill": role_skill.skillName, "description": skill.skillDescription, "index":None, "level":role_skill.level}
        skills.append(line)


    if 'user' in st.session_state:
        user_skills = (db.query(models.UserSkills)
                         .filter(models.UserSkills.userID==st.session_state["user"].userID)
                         .all())
        
        all_skills = []
        for s in skills:
            for u in user_skills:
                if s["skill"] == u.skillName:
                    s["index"] = int(u.level.split(".")[0])
                    all_skills.append(s)
                    user_skills.remove(u)

    map_levels = dict()

    for s in skills:
        with st.container(border=True):
            col1, col2, col3 = st.columns(3)
            map_levels[s["skill"]] = col1.selectbox(s["skill"], options=level_options, placeholder="Selecione seu nível", index=s["index"])
            col2.markdown(s["description"])
            
            if map_levels[s["skill"]] != None and int(map_levels[s["skill"]].split(".")[0]) >= int(s["level"].split(".")[0]):
                col3.success(s["level"])
            elif map_levels[s["skill"]] != None:
                col3.warning(s["level"])
            else:
                col3.code(s["level"])

    if 'user' in st.session_state:
        buttom = st.button(label="Salvar", on_click=lambda: save(db, map_levels))
        
show_pdi()