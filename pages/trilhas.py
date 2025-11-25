import streamlit as st
from streamlit.components.v1 import html

from sqlalchemy import orm

from conteudo.trilhas import basico_tech, data_science_analytics, data_engineering

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

        def mermaid(code):
            html(
                f"""
                <pre class="mermaid">
                    {code}
                </pre>

                <script type="module">
                    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                    mermaid.initialize({{ startOnLoad: true }});
                </script>
                """,
                width=3000,
                height=650
            )

        mermaid("""
flowchart LR

    A[Python] --> E[Pandas];
    E --> F[Streamlit];
    E --> B[Estatística];
    B --> G[Machine Learning];
    C[SQL] --> B;
    G --> H[MLFlow];

    D[Git/GitHub] --> E
    D --> C

    H --> I{Projetos DS}
    F --> I

    I --> M[Loyalty Predict]
    I --> N[Data Science e Pontos]
    I --> O[Data Science Databricks]
    I --> P[Matchmaking de Vagas]

    C --> K[Apache Spark]
    A --> K

    K --> J{Projetos DE}
    L[Docker] --> J

    J --> R[Lago do mago]
    J --> S[Trampar de Lakehouse]

    I --> Q[TSE Analytics]
    J --> Q
    J --> T[F1]
    I --> T
""")
    

    with st.container(border=True):
        basico_tech.basico_tech(db)

    with st.container(border=True):
        data_science_analytics.data_science_analytics(db)

    with st.container(border=True):
        data_engineering.data_engineering(db)


show_trilhas(db)