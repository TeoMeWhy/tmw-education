import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, load_and_show_course
    

def basico_tech(db:orm.Session):
    user_courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""
    ### Início em Tecnologia!
                
    Comece por aqui a aprender sobre dados e tecnologia.""")

    load_and_show_course(db=db, course_slug='github-2025', user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug='python-2025', user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug='sql-2025', user_courses_progress=user_courses_progress)

