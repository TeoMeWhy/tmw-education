import pandas as pd
from sqlalchemy import orm
import streamlit as st

from .estatistica import curso_estatistica_pt01, curso_estatistica_pt02
from .git_github import git_github
from .machine_learning import curso_machine_learning
from .programacao import curso_python, curso_pandas

from databases import models

def get_courses_dataframe(db:orm.Session, user_id:str)->pd.DataFrame:
    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    resp = models.get_courses_complet_by_user(db, user_id=user_id)
    if len(resp) > 0:
        courses_progress = pd.DataFrame([{
                            "userID": i.userID,
                            "courseSlug": i.courseSlug,
                            "epSlug": i.epSlug,
                            "createdAt": i.createdAt,
        } for i in resp])
    return courses_progress


def cursos(db:orm.Session):

    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("## Cursos")
    st.markdown("Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.")

    with st.expander("Git e GitHub"):
        git_github(db, courses_progress[courses_progress['courseSlug']=='github'])

    with st.expander("Python - 10/02 a 14/02"):
        curso_python(courses_progress[courses_progress['courseSlug']=='python'])

    with st.expander("Pandas - 10/03 a 14/03"):
        curso_pandas(courses_progress[courses_progress['courseSlug']=='pandas'])

    with st.expander("Estatística: Parte 01 - 31/03 a 04/04"):
        curso_estatistica_pt01(courses_progress[courses_progress['courseSlug']=='estatistica-01'])

    with st.expander("Estatística: Parte 02 - 14/04 a 18/04"):
        curso_estatistica_pt02(courses_progress[courses_progress['courseSlug']=='estatistica-02'])

    with st.expander("Machine Learning - 05/05 a 16/05"):
        curso_machine_learning(courses_progress[courses_progress['courseSlug']=='machine-learning'])
