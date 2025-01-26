import streamlit as st
from git_github import git_github
from programacao import curso_pandas, curso_python
from estatistica import curso_estatistica_pt01, curso_estatistica_pt02

st.markdown("# Téo Me Why - 2025")

st.markdown("## Cursos")
st.markdown("Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.")

with st.expander("Git e GitHub - Em andamento"):
    git_github()

with st.expander("Python - 10/02 a 14/02"):
    curso_python()

with st.expander("Pandas - 10/03 a 14/03"):
    curso_pandas()

with st.expander("Estatística: Parte 01 - 31/03 a 04/04"):
    curso_estatistica_pt01()

with st.expander("Estatística: Parte 02 - 14/04 a 18/04"):
    curso_estatistica_pt02()