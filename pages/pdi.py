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
    Pra definir um PDI, temos como primeira tarefa, mapear o nível de cada habilidade.
                
    Para isso, considere a tabela abaixo com a descrição de cada nível.
                
    | Nível            | Descrição                                                    |
    |---               |---                                                           |
    | 00. Não esperada | Não é esperado esta habilidade                               |
    | 01. Aprendiz     | Não tem conhecimento para fazer solo                         |
    | 02. Iniciante    | Consegue encarar desafios menores mas ainda precisa de apoio |
    | 03. Profissional | Tem autonomia para fazer solo                                |
    | 04. Expert       | Domina o assunto e faz com excelência                        |
    | 05. Professor    | É referência no assunto e compartilha conhecimento           |


    Com isso em mente, o próximo passo é escolher qual será a sua jornada. Selecione a profissão que seja seguir e o nível de atuação desejável.
                
    Isto é, `desejo ser uma pessoa em Data Science, nível Jr.`, portanto, selecione `Data Scientist` em **Carreira** e `Jr.` em **Nível**.
                
    Dependendo da carreira e nível escolhido, as habilidades são modificadas, bem como seu nível esperado de cada habilidade.
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
        
        for s in skills:
            for u in user_skills:
                if s["skill"] == u.skillName and u.level != None:
                    s["index"] = int(u.level.split(".")[0])
                    user_skills.remove(u)

    map_levels = dict()

    st.markdown("""
    Agora vem a parte mais trabalhosa e desafiadora. Para cada habilidade, selecione o nível que você se encontra atualmente.
    
    Reforço a importância de usar a tabela apresentada anteriormente como refência durante sua reflexão.                
    """)

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