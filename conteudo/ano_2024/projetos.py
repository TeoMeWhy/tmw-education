import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, load_and_show_course


def projetos_2024(db: orm.Session):

    user_courses_progress = pd.DataFrame(
        columns=["userID", "courseSlug", "epSlug", "createdAt"]
    )
    if "user" in st.session_state:
        user_courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown(
        """### Projetos
                
Acompanhe aqui nossos todos os projetos que relizamos na área de dados durante o nosso ano de 2024. Você pode acompanhar por aqui, sendo membro do YouTube.
                
Para Subs da Twitch, vamos deixar o link das playlist para você acompanhar por lá.

"""
    )

    st.markdown("#### Data Science")
    load_and_show_course(db=db, course_slug="ds-pontos-2024", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug="ds-databricks-2024", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug="matchmaking-trampar-de-casa-2024", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug="tse-analytics-2024", user_courses_progress=user_courses_progress)

    st.markdown("#### Data Engineering")
    load_and_show_course(db=db, course_slug="lago-mago-2024", user_courses_progress=user_courses_progress)
    load_and_show_course(db=db, course_slug="trampar-lakehouse-2024", user_courses_progress=user_courses_progress)
    
