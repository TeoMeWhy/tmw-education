import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..ano_2020.programacao import curso_sql

from ..utils import get_courses_dataframe, load_and_show_course
    

def basico_tech(db:orm.Session):
    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""
    ### Início em Tecnologia!
                
    Comece por aqui a aprender sobre dados e tecnologia.

    
    """)

    load_and_show_course(db,'github-2025', courses_progress[courses_progress['courseSlug']=='github-2025'])
    load_and_show_course(db,'python-2025', courses_progress[courses_progress['courseSlug']=='python-2025'])
    curso_sql(db, courses_progress[courses_progress['courseSlug']=='sql-2020'])

