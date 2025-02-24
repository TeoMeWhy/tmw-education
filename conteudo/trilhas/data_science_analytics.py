import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..ano_2024.programacao import curso_pandas
from ..ano_2024.estatistica import curso_estatistica
from ..ano_2024.machine_learning import curso_machine_learning
from ..ano_2024.projetos import data_science_pontos, data_science_databricks, rec_sys_trampar_casa, tse_analytics


from ..utils import get_courses_dataframe
    

def data_science_analytics(db:orm.Session):
    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""
    ### Data Science & Analytics!
                
    Vamos aprender sobre a área de dados, suas principais bibliotecas e conceitos.
    """)

    cursos, projetos = st.tabs(["Cursos", "Projetos"])

    with cursos:
        st.markdown("""
        #### Cursos

        Os cursos já estão em ordem de prioridade para fazer sentido seu aprendizado.
        """)

        with st.expander("Pandas"):
            curso_pandas(db, courses_progress[courses_progress['courseSlug']=='pandas-2024'])

        with st.expander("Estatística"):
            curso_estatistica(db, courses_progress[courses_progress['courseSlug']=='estatistica-2024'])

        with st.expander("Machine Learning para Pôneis"):
            curso_machine_learning(db, courses_progress[courses_progress['courseSlug']=='ml-2024'])


    with projetos:

        st.markdown("""
        #### Projetos
                    
        Acompanhe os projetos para entender como é a vida real de uma pessoa que trabalha com Data Science e Analytics.    
        """)

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
                db,courses_progress[courses_progress["courseSlug"] == "matchmaking-trampar-de-casa-2024"],
            )

        with st.expander("TSE Analytics"):
            tse_analytics(
                db, courses_progress[courses_progress["courseSlug"] == "tse-analytics-2024"],
            )