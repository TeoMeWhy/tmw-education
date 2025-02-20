import pandas as pd
from sqlalchemy import orm
import streamlit as st

from .estatistica import curso_estatistica_pt01, curso_estatistica_pt02
from .git_github import git_github
from .machine_learning import curso_machine_learning, mlflow
from .programacao import curso_python, curso_pandas

from ..utils import get_courses_dataframe
    

def cursos_2025(db:orm.Session):

    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""### Cursos
                
Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.
    """)

    with st.expander("MLFlow"):
        mlflow(db, courses_progress[courses_progress['courseSlug']=='mlflow-2025'])

    with st.expander("Git e GitHub"):
        git_github(db, courses_progress[courses_progress['courseSlug']=='github-2025'])

    with st.expander("Python"):
        curso_python(db, courses_progress[courses_progress['courseSlug']=='python-2025'])

    with st.expander("Pandas - 10/03 a 14/03"):
        curso_pandas(courses_progress[courses_progress['courseSlug']=='pandas'])

    with st.expander("Estatística: Parte 01 - 31/03 a 04/04"):
        curso_estatistica_pt01(courses_progress[courses_progress['courseSlug']=='estatistica-01'])

    with st.expander("Estatística: Parte 02 - 14/04 a 18/04"):
        curso_estatistica_pt02(courses_progress[courses_progress['courseSlug']=='estatistica-02'])

    with st.expander("Machine Learning - 05/05 a 16/05"):
        curso_machine_learning(courses_progress[courses_progress['courseSlug']=='machine-learning'])
