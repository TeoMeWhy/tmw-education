import pandas as pd
from sqlalchemy import orm
import streamlit as st

from .estatistica import curso_estatistica
from .git_github import git_github
from .machine_learning import curso_machine_learning
from .programacao import curso_python, curso_pandas, coleta_dados

from ..utils import get_courses_dataframe
    

def cursos_2024(db:orm.Session):

    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""### Cursos
                
Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.
    """)

    with st.expander("Git e GitHub"):
        git_github(db, courses_progress[courses_progress['courseSlug']=='github-2024'])

    with st.expander("Python"):
        curso_python(db, courses_progress[courses_progress['courseSlug']=='python-2024'])

    with st.expander("Desbravando Pandas"):
        curso_pandas(db, courses_progress[courses_progress['courseSlug']=='pandas-2024'])

    with st.expander("Coleta de Dados"):
        coleta_dados(db, courses_progress[courses_progress['courseSlug']=='coleta-dados-2024'])

    with st.expander("Estatística Básica"):
        curso_estatistica(db, courses_progress[courses_progress['courseSlug']=='estatistica-2024'])

    with st.expander("Machine Learning para Poneis"):
        curso_machine_learning(db, courses_progress[courses_progress['courseSlug']=='ml-2024'])
