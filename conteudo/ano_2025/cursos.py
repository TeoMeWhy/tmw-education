import pandas as pd
from sqlalchemy import orm
import streamlit as st

from .machine_learning import curso_machine_learning
from .programacao import curso_sql

from ..utils import get_courses_dataframe, load_and_show_course
    

def cursos_2025(db:orm.Session):

    user_courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""### Cursos
                
Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.
    """)
    
    load_and_show_course(db=db, course_slug='mlflow-2025', user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug='github-2025', user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug='python-2025', user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug='pandas-2025', user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug='estatistica-2025', user_courses_progress=user_courses_progress)
    curso_machine_learning(user_courses_progress[user_courses_progress['courseSlug']=='machine-learning-2025'])
    curso_sql(user_courses_progress[user_courses_progress['courseSlug']=='sql-2025'])