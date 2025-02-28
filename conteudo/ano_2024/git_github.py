import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import make_course_ep


def git_github(db:orm.Session, course_eps:pd.DataFrame):

    with st.expander("Git e GitHub"):

        about = """
    Dando início às nossas atividades na trilha de dados, começamos com Git & GitHub para versionamento e organização de nossos códigos Abordamos tanto no ambiente local, como repositórios remotos.
    Foram dois dias intensos aprendendo sobre essa ferramenta muito utilizada no dia a dia na área de dados e tecnologia.
        """
        st.markdown(about)
        slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,10)}
            
        make_course_ep(course_slug="github-2024",
                    title="Introdução ao Git e GitHub",
                    youtube_id="napLViBKAtA",
                    ep_slug="ep-01",
                    slug_flag=slugs_flags["ep-01"],
                    db=db)

        make_course_ep(course_slug="github-2024",
                    title="Introdução ao Git e GitHub - Dia 02",
                    youtube_id="n58LxenCnYs",
                    ep_slug="ep-02",
                    slug_flag=slugs_flags["ep-02"],
                    db=db)

        make_course_ep(course_slug="github-2024",
                    title="Introdução ao Git e GitHub - Gitignore Gitkeep",
                    youtube_id="AljGpIviLyE",
                    ep_slug="ep-03",
                    slug_flag=slugs_flags["ep-03"],
                    db=db)
