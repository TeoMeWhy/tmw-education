import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, load_and_show_course

def ia_engineering(db:orm.Session):
    user_courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""
    ### IA Engineering!
    
    Projetos integrando IA com engenharia e ciência de dados.
    
    """)

    st.markdown("""
    ### Projetos
    
    Com base nos fundamentos apresentados nos cursos gratuitos e conceitos de engenharia de dados, é criamos algumas aplicações de IA reais e que fazem sentido para o nosso contexto.
    
    """)
    
    load_and_show_course(db=db, course_slug="ragia", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug="meu-agente", user_courses_progress=user_courses_progress)
