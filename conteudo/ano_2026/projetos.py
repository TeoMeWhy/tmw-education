import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, load_and_show_course


def projetos_2026(db: orm.Session):

    user_courses_progress = pd.DataFrame(
        columns=["userID", "courseSlug", "epSlug", "createdAt"]
    )

    if "user" in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown(
    """
    ### Projetos
                
    Confira os projetos que já realizamos em 2026!
    
    """)
    
    st.markdown("#### Plataforma de Machine Learning")
    load_and_show_course(db=db, course_slug="plataforma-ml-2026", user_courses_progress=user_courses_progress)
    
