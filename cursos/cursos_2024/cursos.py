import pandas as pd
from sqlalchemy import orm
import streamlit as st

from .estatistica import curso_estatistica
from .git_github import git_github
from .machine_learning import curso_machine_learning
from .programacao import curso_python, curso_pandas, coleta_dados

from ..utils import get_courses_dataframe
    

def cursos_2024(db:orm.Session):

    txt = """
Este ano foi um ano que tomamos coragem para ter dedicação exclusiva ao projeto.
A partir disso, tivemos muitas realizações junto à comunidade, por isso gostaríamos de compartilhar estes feitos.
Nossa motivação não apenas para mostrar o nosso trabalho, mas também engajar novas pessoas aos estudos na área de dados e tecnologia, como também, compartilharem seus avanços, aprendizados e lutas.

Lembramos que o projeto [Téo Me Why](https://teomewhy.org) é parceiro do [Instituto Aaron Swartz](https://institutoasw.org) na luta pela emancipação do conhecimento.

## Sumário

No total, realizamos seis treinamentos para te ajudar nos conhecimentos básicos na área de dados.
Além disso, realizamos seis projetos completamente mão na massa para você aplicar todos conhecimentos adquiridos anteriormente, além de te inspirar a caçar mais dados para crescer o seu portfólio. 
Confira abaixo a lista de tudo isso que você pode e deve aproveitar.
"""

    st.markdown(txt)

    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    if 'user' in st.session_state:
        courses_progress = get_courses_dataframe(db, st.session_state["user"].userID)

    st.markdown("### Cursos")
    st.markdown("Acompanhe aqui nossos cursos realizados conforme avançamos e tudo o que nos espera durante este ano.")

    with st.expander("Git e GitHub"):
        git_github(db, courses_progress[courses_progress['courseSlug']=='github-2024'])

    with st.expander("Python"):
        curso_python(db, courses_progress[courses_progress['courseSlug']=='python-2024'])

    with st.expander("Desbravando Pandas"):
        curso_pandas(db, courses_progress[courses_progress['courseSlug']=='pandas-2024'])

    with st.expander("Coleta de Dados"):
        coleta_dados(db, courses_progress[courses_progress['courseSlug']=='coleta-dados-2024'])

    with st.expander("Estatística Básica"):
        curso_estatistica(db, courses_progress[courses_progress['courseSlug']=='estatistica-2024'])

    with st.expander("Machine Learning para Poneis"):
        curso_machine_learning(db, courses_progress[courses_progress['courseSlug']=='ml-2024'])
