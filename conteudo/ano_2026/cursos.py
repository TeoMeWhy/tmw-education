import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, load_and_show_course
    

def cursos_2026(db:orm.Session):

    user_courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""### Cursos
                
Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.
    """)
    
    load_and_show_course(db=db, course_slug='go-2026', user_courses_progress=user_courses_progress)
    