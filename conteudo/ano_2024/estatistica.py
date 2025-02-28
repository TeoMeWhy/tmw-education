import pandas as pd
import streamlit as st
from sqlalchemy import orm

from ..utils import make_course_ep

def curso_estatistica(db:orm.Session, course_eps:pd.DataFrame):

    with st.expander("Estatística Básica"):

        about = """
        Avançandos nos pilares de Data Science, a disciplina de Estatística não poderia ficar de fora.
        Realizamos cinco lives apresentando os principais conceitos, desde tabelas de frequência, medidas de posição e dispersão, conceitos de amostragem vs população, 
        probabilidade, inferência de parâmetros e testes de hipóteses."""
        st.markdown(about)

        slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,8)}

        make_course_ep(course_slug="estatistica-2024",
                    title="Estatística Básica - Introdução e tabelas de frequência",
                    youtube_id="onOgEotiuMw",
                    ep_slug="ep-01",
                    slug_flag=slugs_flags["ep-01"],
                    db=db)

        make_course_ep(course_slug="estatistica-2024",
                    title="Tabela de frequencia no SQL",
                    youtube_id="HZH3OWLq7Ew",
                    ep_slug="ep-02",
                    slug_flag=slugs_flags["ep-02"],
                    db=db)

        make_course_ep(course_slug="estatistica-2024",
                    title="Estatística Básica - Medidas de Posição e Dispersão",
                    youtube_id="ZOvIGIBmHyo",
                    ep_slug="ep-03",
                    slug_flag=slugs_flags["ep-03"],
                    db=db)

        make_course_ep(course_slug="estatistica-2024",
                    title="Medidas de Resumo no SQL",
                    youtube_id="9XUJ5PNj9tw",
                    ep_slug="ep-04",
                    slug_flag=slugs_flags["ep-04"],
                    db=db)

        make_course_ep(course_slug="estatistica-2024",
                    title="Estatística Básica - Gráficos e Probabilidade",
                    youtube_id="8rgAG58SJS8",
                    ep_slug="ep-05",
                    slug_flag=slugs_flags["ep-05"],
                    db=db)

        make_course_ep(course_slug="estatistica-2024",
                    title="Estatística Básica - Probabilidade",
                    youtube_id="9Lbvj6JzgII",
                    ep_slug="ep-06",
                    slug_flag=slugs_flags["ep-06"],
                    db=db)

        make_course_ep(course_slug="estatistica-2024",
                    title="Estatística Básica - Intervalo de Confiança",
                    youtube_id="-IMEseOJs2c",
                    ep_slug="ep-07",
                    slug_flag=slugs_flags["ep-07"],
                    db=db)

