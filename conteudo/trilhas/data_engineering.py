import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, load_and_show_course
from conteudo.ano_2026.cursos import cursos_2026
    

def data_engineering(db:orm.Session):
    user_courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""
    ### Data Engineering!
    
    Como conteúo adicional, pensando no diferencial que uma pessoa de dados mais sênior pode ter, criamos um curso de Go. É bem provável que usaremos Go em alguns de nossos projetos para criação de APIs, por exemplo.            
    
    """)

    cursos_2026(db=db)

    st.markdown("""
    ### Projetos
                
    Embora não tenhamos um curso específico de Data Engineering, realizamos alguns projetos que podem te aprensentar a área de Engenharia de Dados de uma maneira única!
                
    São projetos reais, realizando ingestão de dados em um ambiente cloud com as das melhores ferramentas do mercado.
    """)
    

    load_and_show_course(db=db,course_slug="speed-f1", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug="nekt-2025", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug="plataforma-ml-2026", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db,course_slug="lago-mago-2024", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db,course_slug="trampar-lakehouse-2024", user_courses_progress=user_courses_progress)
