import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, load_and_show_course
    

def data_science_analytics(db:orm.Session):
    user_courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""
    ### Data Science & Analytics!
                
    Vamos aprender sobre a área de dados, suas principais bibliotecas e conceitos.
    """)

    cursos, projetos = st.tabs(["Cursos", "Projetos"])

    with cursos:
        st.markdown("""
        #### Cursos

        Os cursos já estão em ordem de prioridade para fazer sentido seu aprendizado.
        """)

        load_and_show_course(db=db, course_slug='pandas-2025', user_courses_progress=user_courses_progress)
        load_and_show_course(db=db, course_slug='estatistica-2025', user_courses_progress=user_courses_progress)
        load_and_show_course(db, course_slug='ml-2024', user_courses_progress=user_courses_progress)
        load_and_show_course(db=db, course_slug='mlflow-2025', user_courses_progress=user_courses_progress)


    with projetos:

        st.markdown("""
        #### Projetos
                    
        Acompanhe os projetos para entender como é a vida real de uma pessoa que trabalha com Data Science e Analytics.    
        """)

        load_and_show_course(db=db,course_slug="ds-pontos-2024", user_courses_progress=user_courses_progress)
        load_and_show_course(db=db,course_slug="ds-databricks-2024", user_courses_progress=user_courses_progress)
        load_and_show_course(db=db,course_slug="matchmaking-trampar-de-casa-2024", user_courses_progress=user_courses_progress)
        load_and_show_course(db=db,course_slug="tse-analytics-2024", user_courses_progress=user_courses_progress)