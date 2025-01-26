import streamlit as st
from git_github import git_github
from programacao import curso_pandas, curso_python
from estatistica import curso_estatistica_pt01

st.markdown("# Téo Me Why - 2025")

st.markdown("## Cursos")
st.markdown("Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.")

with st.expander("Git e GitHub"):
    git_github()

with st.expander("Python - em breve"):
    curso_python()

with st.expander("Pandas - em breve"):
    curso_pandas()

with st.expander("estatística - em breve"):
    curso_estatistica_pt01()
