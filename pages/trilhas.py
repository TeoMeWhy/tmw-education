import streamlit as st
from streamlit.components.v1 import html

from sqlalchemy import orm

from conteudo.trilhas import basico_tech, data_science_analytics, data_engineering
from conteudo import livros

from databases.models import SessionLocal
from login import twitch_login

db = SessionLocal()

def show_trilhas(db:orm.Session):
    twitch_login.twitch_login(db)
    
    txt = """
    Não faz ideia por onde começar em dados e tecnologia?
    Organizamos nosso material de uma maneira sequencial para você aprender tópico por tópico, ferramenta por ferramenta, conceito por conceito.
    
    Vamos explorar o básico em tecnologia, pra depois nos especializarmos.
    
    O conteúdo é composto por aulas (cursos) e projetos. Todos os cursos são gratuitos, e projetos são destinados à apoiadores do nosso canal no YouTube.

    Confira uma sugestão de roadmap abaixo:
    """

    st.markdown(txt)

    with st.expander("Roadmap", expanded=False):
        st.image("assets/fluxograma.png")

    videos, books = st.tabs(["Vídeos", "Livros"])

    with videos:

        st.markdown("""

    ## Overview
                
    #### Início em Tecnologia:
    
    Comece por aqui, aprendendo os fundamentos básicos de tecnologia e programação.

    #### Data Science & Analytics:
    
    Agora entramos na área de dados. Você conhecerá bibliotecas e conceitos específicos da área de dados, independente se pretende seguir com Data Science ou Analytics. Vale dizer que muitos desses conceitos te tornarão uma pessoa profissional mais completa, ainda que queira seguir em engenharia de dados.
                
    Quando finalizar todos os cursos e se sentir confortável suficiente para seguir, recomento realizar os projetos. Eles podem te inspirar para criar seu próprio portfólio, como também dar uma boa noção de quais são as etapas e tarefas do dia a dia de uma pessoa na área.
    
    #### Data Engineering

    Minha carreira sempre foi voltada à Data Science, construindo modelos preditivos. Mas sempre busquei ter autonomia em minhas entregas e assim acabei conhecendo a área de engenharia de dados. Essa sessão é focada em projetos que tem como entregável final, um produto de dados de Data Science, mas o caminho é repleto por tarefas e questões de engenharia de dados.
                
    Ou seja, embora nosso foco não seja exatamente os fundamentos de engenharia, você aprenderá *muito* sobre este universo e terá condições de aplicar no dia a dia, seja para seguir na carreira de Engenharia ou de Data Science/Analytics.

    """)

        with st.container(border=True):
            basico_tech.basico_tech(db)

        with st.container(border=True):
            data_science_analytics.data_science_analytics(db)

        with st.container(border=True):
            data_engineering.data_engineering(db)
    
    with books:
        livros.livros_bd()
        livros.livros_programacao()
        livros.livros_estat()
        livros.livros_ml()
        livros.livros_de()
        livros.livros_cultura()



show_trilhas(db)