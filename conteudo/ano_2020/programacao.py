import pandas as pd
import streamlit as st
from sqlalchemy import orm

from ..utils import make_course_ep


def curso_sql(db:orm.Session, course_eps:pd.DataFrame):
    
    with st.expander("SQL"):
    
        about = """
        Curso completo e gratuito de SQL para pessoas iniciantes na área de Tecnologia e Dados.
        """
        st.markdown(about)

        slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,8)}
            

        make_course_ep(course_slug="sql-2020",
                    title="SELECT FROM WHERE",
                    youtube_id="PXftBr56Tow",
                    ep_slug="ep-01",
                    slug_flag=slugs_flags["ep-01"],
                    db=db)
        
        make_course_ep(course_slug="sql-2020",
                    title="GROUP BY",
                    youtube_id="BPwGCEsPxMI",
                    ep_slug="ep-02",
                    slug_flag=slugs_flags["ep-02"],
                    db=db)
        
        make_course_ep(course_slug="sql-2020",
                    title="CASE WHEN COALESCE",
                    youtube_id="7Ikyb5-5gOQ",
                    ep_slug="ep-03",
                    slug_flag=slugs_flags["ep-03"],
                    db=db)
        
        make_course_ep(course_slug="sql-2020",
                    title="Como fazer JOINS",
                    youtube_id="jJxC0i6OtQQ",
                    ep_slug="ep-04",
                    slug_flag=slugs_flags["ep-04"],
                    db=db)
        
        make_course_ep(course_slug="sql-2020",
                    title="Como funciona SUBQUERIES",
                    youtube_id="1ulTb3u8aPk",
                    ep_slug="ep-05",
                    slug_flag=slugs_flags["ep-05"],
                    db=db)
        
        make_course_ep(course_slug="sql-2020",
                    title="O que são WINDOW FUNCTIONS",
                    youtube_id="v3U5ViG-rkc",
                    ep_slug="ep-06",
                    slug_flag=slugs_flags["ep-06"],
                    db=db)
        
        make_course_ep(course_slug="sql-2020",
                    title="Como fazer CREATE TABLE",
                    youtube_id="K2V0ZJA3yK0",
                    ep_slug="ep-07",
                    slug_flag=slugs_flags["ep-07"],
                    db=db)
    