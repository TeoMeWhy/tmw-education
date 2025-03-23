import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, make_course_ep


def projetos_2025(db: orm.Session):

    courses_progress = pd.DataFrame(
        columns=["userID", "courseSlug", "epSlug", "createdAt"]
    )

    if "user" in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown(
    """### Projetos
                
    Acompanhe aqui nossos todos os projetos que estamos relizamos na divididos entre as subárea que temos em Dados. Seja membro do YouTube para conseguir acessar o conteúdo destes materiais.
                    
    Os projetos construídos a partir de 2025, terão as gravações disponíveis exclusivamente no YouTube.
    """)

    st.markdown("#### Inteligência Artificial")
    ia_para_canal(db, courses_progress[courses_progress["courseSlug"] == "ia-canal-2025"])


def ia_para_canal(db: orm.Session, course_eps: pd.DataFrame):

    with st.expander("Uma IA para o canal"):

        txt = """
        Temos o interesse de tornar a experiência de quem nos acompanha ainda melhor. Para isso, estamos criando um sistema de Inteligência Artificial usando LLM e RAG com um banco vetorizado (QDrant).
        A ideia é integrar o no nosso chat da Twitch com esse sistema, respondendo de maneira automática algumas perguntas comuns de nossos participantes.

        no futuro, pretendemos estender essa ideia para a nossa plataforma de educação, realizando buscas inteligentes em nosso material didático.
        """

        st.markdown(txt)
        data = [
            {
                "title": "Construindo um Sistema de IA - Bancos Vetoriais",
                "youtube_id": "3aMq_5b6DPY",
            },
            {
                "title": "Construindo um Sistema de IA - Embeddings",
                "youtube_id": "_hvw1oYxLoY",
            },
        ]

        slugs_flags = {
            f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count()
            == 1
            for i in range(1, len(data) + 1)
        }

        for i in range(len(data)):
            make_course_ep(
                course_slug="ia-canal-2025",
                title=data[i]["title"],
                youtube_id=data[i]["youtube_id"],
                ep_slug=list(slugs_flags.items())[i][0],
                slug_flag=list(slugs_flags.items())[i][1],
                db=db,
            )