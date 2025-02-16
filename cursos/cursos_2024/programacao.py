import pandas as pd
import streamlit as st
from sqlalchemy import orm

from ..utils import make_course_ep


def curso_python(db:orm.Session, course_eps:pd.DataFrame):
    about = """
    Realizamos um curso de Python Básico, aprendendo os primeiros passos na área de Lógica e Programação.
    Conhecemos a sintaxe da linguagem mais utilizada na área de dados. Ensinamos desde a instalação, principais estruturas de dados, laços de repetição, função, importação e instalação de pacotes.
    """
    st.markdown(about)

    slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,6)}

    make_course_ep(course_slug="python-2024",
                   title="Introdução à Programação com Python - Dia 01",
                   youtube_id="asUCVFBUyfY",
                   ep_slug="ep-01",
                   slug_flag=slugs_flags["ep-01"],
                   db=db)
    
    make_course_ep(course_slug="python-2024",
                   title="Introdução à Programação com Python - Dia 02",
                   youtube_id="hOuiT8Oby6c",
                   ep_slug="ep-02",
                   slug_flag=slugs_flags["ep-02"],
                   db=db)

    make_course_ep(course_slug="python-2024",
                   title="Introdução à Programação com Python - Dia 03",
                   youtube_id="gA4inE1n1SI",
                   ep_slug="ep-03",
                   slug_flag=slugs_flags["ep-03"],
                   db=db)

    make_course_ep(course_slug="python-2024",
                   title="Introdução à Programação com Python - Dia 04",
                   youtube_id="BUmXQUA12KU",
                   ep_slug="ep-04",
                   slug_flag=slugs_flags["ep-04"],
                   db=db)

    make_course_ep(course_slug="python-2024",
                   title="Introdução à Programação com Python - Dia 05",
                   youtube_id="SXTXuCPPuxo",
                   ep_slug="ep-05",
                   slug_flag=slugs_flags["ep-05"],
                   db=db)


def curso_pandas(db:orm.Session, course_eps:pd.DataFrame):
    about = """
    Para manipulação de dados, por hora, não ha biblioteca mais popular do que Pandas! Por isso ministramos um treinamento com 15hr dessa biblioteca.
    Começamos com o básico, navegando em Series e Dataframes, para depois realizar manipulações mais complexas para nossas análises.
    """

    st.markdown(about)

    slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,8)}

    make_course_ep(course_slug="pandas-2024",
                   title="Desbravando Pandas - Dia 01",
                   youtube_id="fLvMKsgHP0o",
                   ep_slug="ep-01",
                   slug_flag=slugs_flags["ep-01"],
                   db=db)
    
    make_course_ep(course_slug="pandas-2024",
                    title="Desbravando Pandas - Dia 02",
                    youtube_id="CgkM0FQ-wuk",
                    ep_slug="ep-02",
                    slug_flag=slugs_flags["ep-02"],
                    db=db)

    make_course_ep(course_slug="pandas-2024",
                    title="Desbravando Pandas - Dia 03",
                    youtube_id="8pEkvlQtwBk",
                    ep_slug="ep-03",
                    slug_flag=slugs_flags["ep-03"],
                    db=db)

    make_course_ep(course_slug="pandas-2024",
                    title="Desbravando Pandas - Dia 04",
                    youtube_id="ebuEZrE9OEo",
                    ep_slug="ep-04",
                    slug_flag=slugs_flags["ep-04"],
                    db=db)

    make_course_ep(course_slug="pandas-2024",
                    title="Desbravando Pandas - Dia 05",
                    youtube_id="LbO5xQouOEw",
                    ep_slug="ep-05",
                    slug_flag=slugs_flags["ep-05"],
                    db=db)

    make_course_ep(course_slug="pandas-2024",
                    title="Desbravando Pandas - Stack e Unstack",
                    youtube_id="x1MWHD9dfqU",
                    ep_slug="ep-06",
                    slug_flag=slugs_flags["ep-06"],
                    db=db)

    make_course_ep(course_slug="pandas-2024",
                    title="Desbravando Pandas - Explode",
                    youtube_id="VDL-1yIvNkE",
                    ep_slug="ep-07",
                    slug_flag=slugs_flags["ep-07"],
                    db=db)

    st.markdown(about)


def coleta_dados(db:orm.Session, course_eps:pd.DataFrame):

    txt = """Agora, como sabemos o mínimo de como manipular dados no computador utilizando uma linguagem de programação, vamos coletar dados!
    Essa playlist trouxe algumas alternativas de como podemos obter dados na internet: crawlers, APIs, FTP. Como exemplo, consumimos dados do
    [Resident Evil Database](https://www.residentevildatabase.com/), [Pokemon API](https://pokeapi.co/), [TabNews](https://www.tabnews.com.br/), etc.
    Além disso, demos uma breve introdução de como essas ingestão podem ser realizadas em um Datalake com Databricks.
    """

    st.markdown(txt)
    slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,5)}

    make_course_ep(course_slug="coleta-dados-2024",
                title="Coleta de dados - Resident Evil Database",
                youtube_id="K-bIZt_hSBo",
                ep_slug="ep-01",
                slug_flag=slugs_flags["ep-01"],
                db=db)
    
    make_course_ep(course_slug="coleta-dados-2024",
                title="Coleta de dados - TabNews e Jovem Nerd",
                youtube_id="JqBLUi9vqgM",
                ep_slug="ep-02",
                slug_flag=slugs_flags["ep-02"],
                db=db)

    make_course_ep(course_slug="coleta-dados-2024",
                title="Coleta de dados - Datalake Databricks",
                youtube_id="cnbw1ySYOOs",
                ep_slug="ep-03",
                slug_flag=slugs_flags["ep-03"],
                db=db)

    make_course_ep(course_slug="coleta-dados-2024",
                title="Coleta de dados - Pokemon e Databricks",
                youtube_id="QyiItDCqClU",
                ep_slug="ep-04",
                slug_flag=slugs_flags["ep-04"],
                db=db)