import streamlit as st

from .estatistica import curso_estatistica_pt01, curso_estatistica_pt02
from .git_github import git_github
from .machine_learning import curso_machine_learning
from .programacao import curso_python, curso_pandas

def cursos():

    st.markdown("## Cursos")
    st.markdown("Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.")

    with st.expander("Git e GitHub"):
        git_github()

    with st.expander("Python - 10/02 a 14/02"):
        curso_python()

    with st.expander("Pandas - 10/03 a 14/03"):
        curso_pandas()

    with st.expander("Estatística: Parte 01 - 31/03 a 04/04"):
        curso_estatistica_pt01()

    with st.expander("Estatística: Parte 02 - 14/04 a 18/04"):
        curso_estatistica_pt02()

    with st.expander("Machine Learning - 05/05 a 16/05"):
        curso_machine_learning()
