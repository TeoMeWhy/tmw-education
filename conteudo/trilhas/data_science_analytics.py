import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..ano_2024.machine_learning import curso_machine_learning

from ..ano_2025.machine_learning import mlflow as curso_mlflow
from ..ano_2025.programacao import curso_pandas
from ..ano_2025.estatistica import curso_estatistica

from ..ano_2024.projetos import data_science_pontos
from ..ano_2024.projetos import data_science_databricks
from ..ano_2024.projetos import rec_sys_trampar_casa
from ..ano_2024.projetos import tse_analytics

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

        curso_pandas(db, courses_progress[courses_progress['courseSlug']=='pandas-2025'])
        curso_estatistica(db, courses_progress[courses_progress['courseSlug']=='estatistica-2025'])
        curso_machine_learning(db, courses_progress[courses_progress['courseSlug']=='ml-2024'])
        curso_mlflow(db, courses_progress[courses_progress['courseSlug']=='mlflow-2025'])


    with projetos:

        st.markdown("""
        #### Projetos
                    
        Acompanhe os projetos para entender como é a vida real de uma pessoa que trabalha com Data Science e Analytics.    
        """)

        data_science_pontos(db, courses_progress[courses_progress["courseSlug"] == "ds-pontos-2024"])
        data_science_databricks(db, courses_progress[courses_progress["courseSlug"] == "ds-databricks-2024"])
        rec_sys_trampar_casa(db,courses_progress[courses_progress["courseSlug"] == "matchmaking-trampar-de-casa-2024"])
        tse_analytics(db, courses_progress[courses_progress["courseSlug"] == "tse-analytics-2024"])