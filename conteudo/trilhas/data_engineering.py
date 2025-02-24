import pandas as pd
from sqlalchemy import orm
import streamlit as st

from ..ano_2024.projetos import lago_do_mago, trampar_lakehouse


from ..utils import get_courses_dataframe
    

def data_engineering(db:orm.Session):
    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("""
    ### Data Engineering!
                
    Embora não tenhamos um curso específico de Data Engineering, realizamos alguns projetos que podem te aprensentar a área de Engenharia de Dados de uma maneira única!
                
    São projetos reais, realizando ingestão de dados em um ambiente cloud com uma das melhores ferramentas do mercado: Databricks.
    """)

    with st.expander("Lago do Mago"):
        lago_do_mago(
            db,
            courses_progress[
                courses_progress["courseSlug"] == "lago-mago-2024"
            ],
        )

    with st.expander("Trampar de Lakehouse"):
        trampar_lakehouse(
            db,
            courses_progress[
                courses_progress["courseSlug"] == "trampar-lakehouse-2024"
            ],
        )