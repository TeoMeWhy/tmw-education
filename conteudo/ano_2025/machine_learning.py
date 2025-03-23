import pandas as pd
import streamlit as st
from sqlalchemy import orm

from ..utils import make_course_ep

def curso_machine_learning(course_eps:pd.DataFrame):

    with st.expander("Machine Learning - 09/06 a 20/06"):

        about = """
        Curso completo e gratuito de Machine Learning para pessoas iniciantes na área da Ciência de Dados.

        As aulas acontecerão nos dias 09/06 e 20/06, ai vivo na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

        O uso de técnicas voltadas à Aprendizado de Máquina tem sido cada dia mais comuns em diferentes mercados e indústricas. Dominar os principais conceitos te ajudará a alcançar não só objetivos da sua empresa, mas também, de crescimento profissional.
        Neste curso, você aprenderá os principais conceitos de Machine Learning, mais do que apenas apertar os botões corretos. Falaremos sobre realmente como a máquina aprender e como podemos avaliar esse aprendizados a partir de diferentes métricas.

        Você entenderá de uma vez por todas como cada técnica funciona, e as métricas de performance. Quando falarem sobre curva ROC, você terá condições de explicar como funciona e porque normalmente é uma métrica melhor que a acurácia. 

        [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=M2Fqc2hkajVxazhsOHFkNDFxdG4yOTg1aGZfMjAyNTA2MDlUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
        """
        st.markdown(about)



def mlflow(db: orm.Session, course_eps: pd.DataFrame):

    with st.expander("MLFlow"):

        txt = """
        MLFlow é uma peça fundamental para se ganhar produtividade em projetos de Machine Learning e Inteligência Artificial.
        Com esse poderoso framework, se pode fazer uma ótima gestão de seus modelos preditivos, LLMs e demais algoritmos de aprendizado de máquina.
        """

        st.markdown(txt)
        data = [
            {
                "title": "O que é MLFlow e como Instalar",
                "youtube_id": "W8bxk42C9UE",
            },
            {
                "title": "Tracking de Modelos com MLFlow",
                "youtube_id": "V-Zc_T6iuJc",
            },
            {
                "title": "Registrando e consumindo modelos no MLFlow",
                "youtube_id": "K2MYiW5m5Ug",
            },
            {
                "title": "Atualização automática de modelos com MLFlow",
                "youtube_id": "KdnRZSH6Drk",
            },
        ]

        slugs_flags = {f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count() == 1 for i in range(1, len(data) + 1)}

        for i in range(len(data)):
            make_course_ep(
                course_slug="mlflow-2025",
                title=data[i]["title"],
                youtube_id=data[i]["youtube_id"],
                ep_slug=list(slugs_flags.items())[i][0],
                slug_flag=list(slugs_flags.items())[i][1],
                db=db,
            )

