import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import make_course_ep


def curso_machine_learning(db:orm.Session, course_eps:pd.DataFrame):
    about = """
Com a base estatística e computacional, podemos apresentar os principais modelos de Machine Learning, bem como as métricas de ajuste.
De maneira bem didática e divertida, aprendemos a fazer alguns modelos "na mão" para depois aplicar utilizando o `scikit-learn` com várias dicas de utilização,
 como a estrutura de pipelines e transformadores de variáveis para pre-processamento dos dados.
"""
    st.markdown(about)

    data = [
        {
            "title":"Machine Learning - Como ensinar a máquina",
            "youtube_id":"oj0ACpEHpS0",
        },
        {
            "title":"Machine Learning - Classificação e Regressão",
            "youtube_id":"N5ZNjET5GQc",
        },
        {
            "title":"Machine Learning - Classificação",
            "youtube_id":"13Ba9mEndgU",
        },
        {
            "title":"Machine Learning - Métricas de Performance",
            "youtube_id":"q7O-H96rp1o",
        },
        {
            "title":"Machine Learning - Projeto Sistema de Pontos",
            "youtube_id":"glXCHPy2-cE",
        },
        {
            "title":"Machine Learning - Métrica de KS",
            "youtube_id":"V1QWx3KZ9AA",
        },
        {
            "title":"Machine Learning - Recomendação de Produtos",
            "youtube_id":"IseLPDxkh88",
        },
    ]

    slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,len(data)+1)}

    for i in range(len(data)):
        make_course_ep(course_slug="ml-2024",
                title=data[i]["title"],
                youtube_id=data[i]["youtube_id"],
                ep_slug=list(slugs_flags.items())[i][0],
                slug_flag=list(slugs_flags.items())[i][1],
                db=db)
