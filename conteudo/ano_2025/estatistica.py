import pandas as pd
import streamlit as st

from sqlalchemy import orm

from ..utils import make_course_ep


def curso_estatistica(db:orm.Session, course_eps:pd.DataFrame):

    with st.expander("Aprenda Estatística Básica"):

        about = """
        Curso gratuido de Estatística (Parte I) para pessoas iniciantes na área de dados.

        Essas aulas acontecerão ao vivo entre os dias 05/05 e 16/05, na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

        Estatística é uma das principais disciplinas para a área de dados. Desde análise simples, mas tambem, toda base para avançarmos em aprendizado de máquina, se faz necessário o conhecimento de métodos e modelos estatísticos.
        
        Vamos fornecer o conhecimento sobre Estatística de forma introdutória. Mas não subestime nosso material. Cobriremos:

        - Conceitos de população (parâmetro) e amostra (estimadores);
        - Estatística descritiva;
        - Representações gráficas;
        - Probabilidade;
        - Intervalo de confiânça;
        - Testes de hipótese;

        Depois de passarmos por todos esses conceitos teóricos, vamos aplica-los via programação em Python.

        """
        st.markdown(about)

        data = [
            {
                "title": "APRENDA ESTATÍSTICA 01: População e Amostra",
                "youtube_id": "4CcgZXXIl7o",
            },
            {
                "title": "APRENDA ESTATÍSTICA 02: Tipos de Variáveis",
                "youtube_id": "FPZBAp8QSRM",
            },
            {
                "title": "APRENDA ESTATÍSTICA 03: Tabela de Frequência",
                "youtube_id": "qca5fOJ2TTg",
            },
            {
                "title": "APRENDA ESTATÍSTICA 04: Tabela de Frequência na PRÁTICA",
                "youtube_id": "cVpO7V0fu_s",
            },
            {
                "title": "APRENDA ESTATÍSTICA 05: Somatórios e Média",
                "youtube_id": "D0hlGcAmc94",
            },
            {
                "title": "APRENDA ESTATÍSTICA 06: Mediana e Quartis",
                "youtube_id": "sL5tbdc2rCE",
            },
            {
                "title": "APRENDA ESTATÍSTICA 07: Medidas de Resumo na Prática (PLANILHAS)",
                "youtube_id": "hgxLeea6Hr8",
            },
            {
                "title": "APRENDA ESTATÍSTICA 08: Medidas de Resumo na Prática (PYTHON)",
                "youtube_id": "9D_c_22lRL8",
            },
            {
                "title": "APRENDA ESTATÍSTICA 09: Medidas de Resumo na Prática (SQL)",
                "youtube_id": "eTBXmQmyqMc",
            },
            {
                "title": "APRENDA ESTATÍSTICA 10: Medidas de Dispersão",
                "youtube_id": "0kdgO0E4Rg8",
            },
            {
                "title": "APRENDA ESTATÍSTICA 11: Medidas de Dispersão (PLANILHAS)",
                "youtube_id": "BCAbwdkdfhM",
            },
            {
                "title": "APRENDA ESTATÍSTICA 12: Medidas de Dispersão (PYTHON)",
                "youtube_id": "aZ7ufhnsblY",
            },
            {
                "title": "APRENDA ESTATÍSTICA 13: Gráficos",
                "youtube_id": "BAhz7OgJyAQ",
            },
            {
                "title": "APRENDA ESTATÍSTICA 14: Gráficos (PLANILHAS)",
                "youtube_id": "ZmYG2dPJxfw",
            },
            {
                "title": "APRENDA ESTATÍSTICA 15: Gráficos (PYTHON)",
                "youtube_id": "_PzfSLBn22k",
            },
            {
                "title": "APRENDA ESTATÍSTICA 16: Probabilidade",
                "youtube_id": "cZyp6Tq9V-0",
            },
            {
                "title": "APRENDA ESTATÍSTICA 17: Probabilidade (PLANILHAS)",
                "youtube_id": "P48vFrhhKf0",
            },
            {
                "title": "APRENDA ESTATÍSTICA 18: Distribuição Bernoulli",
                "youtube_id": "QoMwhXw5aD4",
            },
            {
                "title": "APRENDA ESTATÍSTICA 19: Distribuição Normal",
                "youtube_id": "pbN-W7gV_kM",
            },
            {
                "title": "APRENDA ESTATÍSTICA 20: Intervalo de Confiança",
                "youtube_id": "Xy2esjcmcdI",
            },
            {
                "title": "APRENDA ESTATÍSTICA 21: Teste de Hipótese",
                "youtube_id": "qrv5rFhrM4Q",
            },

        ]

        slugs_flags = { f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count() == 1 for i in range(1, len(data) + 1) }

        for i in range(len(data)):
            make_course_ep(
                course_slug="estatistica-2025",
                title=data[i]["title"],
                youtube_id=data[i]["youtube_id"],
                ep_slug=list(slugs_flags.items())[i][0],
                slug_flag=list(slugs_flags.items())[i][1],
                db=db,
            )
