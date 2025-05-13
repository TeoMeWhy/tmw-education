import pandas as pd
from sqlalchemy import orm
import streamlit as st

from .estatistica import curso_estatistica
from .git_github import git_github
from .machine_learning import curso_machine_learning, mlflow
from .programacao import curso_python, curso_pandas, curso_sql

from ..utils import get_courses_dataframe
    

def cursos_2025(db:orm.Session):

    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""### Cursos
                
Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.
    """)
    
    mlflow(db, courses_progress[courses_progress['courseSlug']=='mlflow-2025'])
    git_github(db, courses_progress[courses_progress['courseSlug']=='github-2025'])
    curso_python(db, courses_progress[courses_progress['courseSlug']=='python-2025'])
    curso_pandas(db, courses_progress[courses_progress['courseSlug']=='pandas-2025'])
    curso_estatistica(db, courses_progress[courses_progress['courseSlug']=='estatistica-2025'])
    curso_machine_learning(courses_progress[courses_progress['courseSlug']=='machine-learning-2025'])
    curso_sql(courses_progress[courses_progress['courseSlug']=='sql-2025'])
