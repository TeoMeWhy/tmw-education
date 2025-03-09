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
                
Acompanhe aqui nossos todos os projetos que relizamos na área de dados durante o nosso ano de 2024. Você pode acompanhar por aqui, sendo membro do YouTube.
                
Para Subs da Twitch, vamos deixar o link das playlist para você acompanhar por lá.

"""
    )

    st.markdown("#### Data Science")
    
    data_science_pontos(db, courses_progress[courses_progress["courseSlug"] == "ds-pontos-2024"])
    data_science_databricks(db, courses_progress[courses_progress["courseSlug"] == "ds-databricks-2024"])
    rec_sys_trampar_casa(db,courses_progress[courses_progress["courseSlug"] == "matchmaking-trampar-de-casa-2024"])
    tse_analytics(db,courses_progress[courses_progress["courseSlug"] == "tse-analytics-2024"])

    st.markdown("#### Data Engineering")

    lago_do_mago(db,courses_progress[courses_progress["courseSlug"] == "lago-mago-2024"])
    trampar_lakehouse(db,courses_progress[courses_progress["courseSlug"] == "trampar-lakehouse-2024"])


def rec_sys_trampar_casa(db: orm.Session, course_eps: pd.DataFrame):

    with st.expander("Matchmaking de Vagas"):

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

    with st.expander("Data Science e Pontos"):
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


    with st.expander("Data Science no Databricks"):

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


def tse_analytics(db:orm.Session, course_eps:pd.DataFrame):

    with st.expander("TSE Analytics"):
        
        txt = """
        Análise dos partidos políticos e suas candidaturas para eleições municipais brasileiras em 2024.
        Todas dados são originários do [TSE](https://dados.gov.br/dados/conjuntos-dados/candidatos-2024).
        Além da criação do app, migramos toda parte de ingestão e tratamento dos dados para nosso ambiente cloud no Databricks.
        """

        st.markdown(txt)
        data = [
            {
                "title": "TSE Analytics - Dia 01 parte 01",
                "youtube_id": "gc6Xy_1cFkU",
            },
            {
                "title": "TSE Analytics - Dia 01 parte 02",
                "youtube_id": "we0Z2Fiu1TY",
            },
            {
                "title": "TSE Analytics - Dia 02",
                "youtube_id": "RqkJE4Z4q3o",
            },
            {
                "title": "TSE Analytics - Dia 03",
                "youtube_id": "osAqr2JGTNU",
            },
            {
                "title": "TSE Analytics - Dia 04",
                "youtube_id": "N5y_jAzjl3g",
            },
            {
                "title": "TSE Analytics - Dia 05",
                "youtube_id": "QY2mXevGp5U",
            },
            {
                "title": "TSE Analytics - Dia 06",
                "youtube_id": "dBetGOdXgDw",
            },
            {
                "title": "TSE Analytics - Dia 07",
                "youtube_id": "aFtytaIc46w",
            },
            
        ]

        slugs_flags = { f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count() == 1 for i in range(1, len(data) + 1) }

        for i in range(len(data)):
            make_course_ep(
                course_slug="tse-analytics-2024",
                title=data[i]["title"],
                youtube_id=data[i]["youtube_id"],
                ep_slug=list(slugs_flags.items())[i][0],
                slug_flag=list(slugs_flags.items())[i][1],
                db=db,
            )



def lago_do_mago(db: orm.Session, course_eps: pd.DataFrame):

    with st.expander("Lago do Mago"):
        txt = """
        Construção de um Datalake e Lake house completamente do zero, desde a criação do ambiente na AWS e Databricks até a criação de dashboard.
        Utilizamos dados reais de nosso sistema de pontos, realizando ingestão na camada RAW. Para consumo e consolidação dos dados em BRONZE, utilizamos leitura dos dados FULL-LOAD e CDC (Change Data Capture) em streaming realizando UPSERT em DELTA. Para camada SILVER, utilizamos novamente Streaming, mas desta vez com CDF (Change Data Feed).
        Em GOLD criamos alguns CUBOS para relatórios em dashboards.

        É Sub da Twitch? Confira aqui: [Sub Twitch](https://www.twitch.tv/collections/2e8D0Vgd3hf04g)
        """

        st.markdown(txt)
        data = [
            {
                "title": "Setup DATABRICKS + UNITY CATALOG",
                "youtube_id": "a1qACiucvzM",
            },
            {
                "title": "Lendo aqruivos FULL LOAD + CDC",
                "youtube_id": "YhgUm9zmhZ8",
            },
            {
                "title": "CDC com Streaming",
                "youtube_id": "1C8rY5g5Cqo",
            },
            {
                "title": "Criando uma classe de ingestão",
                "youtube_id": "MpDcDHE93XA",
            },
            {
                "title": "GitHub Actions para atualizar Worflows",
                "youtube_id": "961sbn71Mqg",
            },
            {
                "title": "Full-Load em Silver",
                "youtube_id": "NBfEb2TkRe8",
            },
            {
                "title": "Change Data Feed",
                "youtube_id": "YY7jJhUlu0k",
            },
            {
                "title": "Custos e Tipos de Clusters",
                "youtube_id": "C6E2U6U4BCw",
            },
            {
                "title": "Camada Gold",
                "youtube_id": "REGzXzp7PSU",
            },
            {
                "title": "Dash Executivo",
                "youtube_id": "uPwtZ9WENfY",
            },
        ]

        slugs_flags = { f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count() == 1 for i in range(1, len(data) + 1) }

        for i in range(len(data)):
            make_course_ep(
                course_slug="lago-mago-2024",
                title=data[i]["title"],
                youtube_id=data[i]["youtube_id"],
                ep_slug=list(slugs_flags.items())[i][0],
                slug_flag=list(slugs_flags.items())[i][1],
                db=db,
            )


def trampar_lakehouse(db: orm.Session, course_eps: pd.DataFrame):

    with st.expander("Trampar de Lakehouse"):

        txt = """
        Dado o bom trabalho que realizamos em conjunto com Trampar de Casa no sistema de recomendação de vagas, surgiu uma nova oportunidade pra construção de um datalake e BI para eles acompanharem as principais métricas da operação que estão tocando. O desenvolvimento consistiu em: criação de um Lakehouse com camadas bronze, silver e gold para criação de relatórios e dashboards. Usamos:
        - AWS S3 para armazenamento dos dados em Raw
        - Databricks como plataforma de dados
        - Apache Spark para leitura, processamento e gravação dos dados
        - SQL para criação de queries e regras de negócios e qualidade de dados
        - Python para orquestração das etapas de ETL
        - Databricks Workflows para orquestração de todas ingestões e transformações de dados
        """

        st.markdown(txt)
        data = [
            {
                "title": "Trampar de lakehouse - Parte 01",
                "youtube_id": "3iqHKRjfyA4",
            },
            {
                "title": "Trampar de lakehouse - Parte 02",
                "youtube_id": "2XQy-UIOyUw",
            },
            {
                "title": "Trampar de lakehouse - Parte 03",
                "youtube_id": "p2DpMP8oiCw",
            },
        ]

        slugs_flags = { f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count() == 1 for i in range(1, len(data) + 1) }

        for i in range(len(data)):
            make_course_ep(
                course_slug="trampar-lakehouse-2024",
                title=data[i]["title"],
                youtube_id=data[i]["youtube_id"],
                ep_slug=list(slugs_flags.items())[i][0],
                slug_flag=list(slugs_flags.items())[i][1],
                db=db,
            )
