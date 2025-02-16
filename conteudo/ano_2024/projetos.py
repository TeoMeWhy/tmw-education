import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..utils import get_courses_dataframe, make_course_ep


def projetos_2024(db: orm.Session):

    courses_progress = pd.DataFrame(
        columns=["userID", "courseSlug", "epSlug", "createdAt"]
    )
    if "user" in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown(
        """### Projetos
                
Acompanhe aqui nossos todos os projetos que relizamos na área de dados durante o nosso ano de 2024. Você pode acompanhar por aqui, sendo memrbo do YouTube.
                
Para Subs da Twitch, vamos deixar o link das playlist para você acompanhar por lá.

"""
    )

    st.markdown("#### Data Science")

    with st.expander("Data Science e Pontos"):
        data_science_pontos(
            db, courses_progress[courses_progress["courseSlug"] == "ds-pontos-2024"]
        )

    with st.expander("Data Science no Databricks"):
        data_science_databricks(
            db, courses_progress[courses_progress["courseSlug"] == "ds-databricks-2024"]
        )

    with st.expander("Matchmaking de Vagas"):
        rec_sys_trampar_casa(
            db,
            courses_progress[
                courses_progress["courseSlug"] == "matchmaking-trampar-de-casa-2024"
            ],
        )


def rec_sys_trampar_casa(db: orm.Session, course_eps: pd.DataFrame):

    txt = """
    Graças a visibilidade com o apoio da comunidade, fomos convidados a realizar nosso primeiro freelance!
    A iniciativa [Trampar de Casa](https://www.trampardecasa.com.br/) necessitava de uma upgrade para seu sistema de recomendações das vagas.
    Isto é, com base nas skills requisitadas de cada vaga, como podemos recomendar a melhor lista de vagas para o usuário que está procurando vagas para se candidatar?
    Foi com isso em mente que criamos um algoritmos para rankear as melhores vagas para cada usuário da plataforma. Ficou bem legal e tivemos um ótimo feedback!

    Confira esse desenvolvimento: [RecSys de Vagas](https://www.youtube.com/playlist?list=PLvlkVRRKOYFTT7O8f-8oQQ1it3AH1gSfm)
    """

    st.markdown(txt)
    data = [
        {
            "title": "Matchmaking de Vagas - Parte I",
            "youtube_id": "STI-WMd7APY",
        },
        {
            "title": "Matchmaking de Vagas - Parte II",
            "youtube_id": "uiAIVGg3k8U",
        },
        {
            "title": "API para Matchmaking de Vagas",
            "youtube_id": "tjlUJG1sVks",
        },
    ]

    slugs_flags = {
        f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count()
        == 1
        for i in range(1, len(data) + 1)
    }

    for i in range(len(data)):
        make_course_ep(
            course_slug="matchmaking-trampar-de-casa-2024",
            title=data[i]["title"],
            youtube_id=data[i]["youtube_id"],
            ep_slug=list(slugs_flags.items())[i][0],
            slug_flag=list(slugs_flags.items())[i][1],
            db=db,
        )


def data_science_pontos(db: orm.Session, course_eps: pd.DataFrame):

    txt = """
    Para colocar em prática tudo que aprendemos até aqui, criamos um projeto de Data Science completo, de início ao fim em ambiente local.
    Projeto foi completo mesmo! Desde a definição do problema de negócio e features, construção das feature store de diferentes contextos, treinamento de diferentes algoritmos, e deploy realizado utilizando o model registry do MLFlow em nosso BOT com uma API em GoLang.
    E ah, tudo isso com dados reais do nosso sistema de pontos da live!

    Se liga nesse projeto que você pode fazer na sua própria máquina [Sub Twitch](https://www.twitch.tv/collections/jg9itHOO1ReLcw)
    """

    st.markdown(txt)
    data = [
        {
            "title": "DS e Pontos - Qual o Problema de Negócio?",
            "youtube_id": "3HijJaRhPP0",
        },
        {
            "title": "DS e Pontos - Primeira Feature Store",
            "youtube_id": "KC-P8DwffA0",
        },
        {
            "title": "DS e Pontos - Últimas Feature Store",
            "youtube_id": "qoOzKaCr1Rk",
        },
        {
            "title": "DS e Pontos - Criação da ABT",
            "youtube_id": "VzcQvGyeAO0",
        },
        {
            "title": "DS e Pontos - Treinamento e Deploy",
            "youtube_id": "1TcFBmjwYlk",
        },
        {
            "title": "DS e Pontos - Integrando com MLFlow",
            "youtube_id": "v5b66aO3PHw",
        },
        {
            "title": "DS e Pontos - O que e SEMMA?",
            "youtube_id": "kyj8oY3d7oM",
        },
        {
            "title": "DS e Pontos - Segmentação RFV",
            "youtube_id": "8hjRYjgrivA",
        },
    ]

    slugs_flags = {
        f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count()
        == 1
        for i in range(1, len(data) + 1)
    }

    for i in range(len(data)):
        make_course_ep(
            course_slug="ds-pontos-2024",
            title=data[i]["title"],
            youtube_id=data[i]["youtube_id"],
            ep_slug=list(slugs_flags.items())[i][0],
            slug_flag=list(slugs_flags.items())[i][1],
            db=db,
        )


def data_science_databricks(db: orm.Session, course_eps: pd.DataFrame):

    txt = """
    Construção completa de um projeto de Data Science do início ao fim em ambiente cloud! Vamos usar as principais ferramentas de Data Science no Databricks, como Feature Store, Workflows e MLFlow para ciclo de vida dos modelos.
    Tudo isso utilizando o Unity Catalog para tracking dos dados e modelos.
    Esse projeto e uma continuação do Lago do Mago, porém, voltado à Cientista de Dados.
    Uma boa forma de entender isso, é como se fizéssemos o projeto Data Science & Pontos não mais localmente, mas sim, no Databricks.

    Caso seja Sub, aproveite para assistir na Twitch: [Sub Twitch](https://www.twitch.tv/collections/ghcAz7_75hfrgQ)
    """

    st.markdown(txt)
    data = [
        {
            "title": "Data Science no Databricks: Planejamento",
            "youtube_id": "zwbqdxwV7JU",
        },
        {
            "title": "Data Science no Databricks: Primeiras Features",
            "youtube_id": "DUeO5SayXhg",
        },
        {
            "title": "Data Science no Databricks: Mais Features",
            "youtube_id": "MterMkuY6to",
        },
        {
            "title": "Data Science no Databricks: Features Lookups",
            "youtube_id": "p6NSppyDvUo",
        },
        {
            "title": "Data Science no Databricks: SEMMA",
            "youtube_id": "kLb6ak54p10",
        },
        {
            "title": "Data Science no Databricks: MLFlow Parte I",
            "youtube_id": "Dq7JKI16aRI",
        },
        {
            "title": "Data Science no Databricks: MLFlow Parte II",
            "youtube_id": "d07mlt4mdv4",
        },
        {
            "title": "Data Science no Databricks: Model Tuning",
            "youtube_id": "3bfclSSevfk",
        },
        {
            "title": "Data Science no Databricks: Predições",
            "youtube_id": "6wAzGB7NZ38",
        },
        {
            "title": "Data Science no Databricks: Deploy com API em Go",
            "youtube_id": "YbZcLUQdDcg",
        },
    ]

    slugs_flags = { f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count() == 1 for i in range(1, len(data) + 1) }

    for i in range(len(data)):
        make_course_ep(
            course_slug="ds-databricks-2024",
            title=data[i]["title"],
            youtube_id=data[i]["youtube_id"],
            ep_slug=list(slugs_flags.items())[i][0],
            slug_flag=list(slugs_flags.items())[i][1],
            db=db,
        )
