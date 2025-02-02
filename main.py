import streamlit as st
from cursos.git_github import git_github
from cursos.programacao import curso_pandas, curso_python
from cursos.estatistica import curso_estatistica_pt01, curso_estatistica_pt02
from cursos.machine_learning import curso_machine_learning

st.markdown("# Téo Me Why - 2025")

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