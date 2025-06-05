import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, load_and_show_course


def projetos_2025(db: orm.Session):

    user_courses_progress = pd.DataFrame(
        columns=["userID", "courseSlug", "epSlug", "createdAt"]
    )

    if "user" in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown(
    """
    ### Projetos
                
    Acompanhe aqui nossos todos os projetos que estamos relizamos na divididos entre as subárea que temos em Dados. Seja membro do YouTube para conseguir acessar o conteúdo destes materiais.
                    
    Os projetos construídos a partir de 2025, terão as gravações disponíveis exclusivamente no YouTube.
    
    """)

    st.markdown("#### Data Engineering")
    load_and_show_course(db=db, course_slug="data-platform-2025", user_courses_progress=user_courses_progress)


    st.markdown("#### Inteligência Artificial")
    load_and_show_course(db=db, course_slug="ia-canal-2025", user_courses_progress=user_courses_progress)

