import pandas as pd
import streamlit as st
from sqlalchemy import orm

from ..utils import make_course_ep


def curso_python(db:orm.Session, course_eps:pd.DataFrame):
    
    with st.expander("Python"):
    
        about = """
        Curso completo e gratuito de Python para pessoas iniciantes na área da programação.

        Python é uma das linguagens mais utilizadas no mundo da computação. Não apenas para criar sites, mas também para análise, engenha e ciência de dados.
        Bem como, tem grande aplicações científicas no meio acadêmico, além, é claro de vasta aplicação com inteligência artificial.

        A ideia principal deste curso é fornecer o conhecimento mínimo sobre lógica de programação, sintaxe da linguagem Python e suas principais estruturas de dados e controle de fluxo, como laços de repetição e operadores lógicos/condicionais.

        """
        st.markdown(about)

        slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,13)}
            

        make_course_ep(course_slug="python-2025",
                    title="Conceitos de Programação e Instalação",
                    youtube_id="OeKzVjiiRm4",
                    ep_slug="ep-01",
                    slug_flag=slugs_flags["ep-01"],
                    db=db)

        make_course_ep(course_slug="python-2025",
                    title="Primeiros Comandos",
                    youtube_id="wp23DUYKQt4",
                    ep_slug="ep-02",
                    slug_flag=slugs_flags["ep-02"],
                    db=db)

        make_course_ep(course_slug="python-2025",
                    title="Recebendo Dados",
                    youtube_id="_40Lzu_C_Ko",
                    ep_slug="ep-03",
                    slug_flag=slugs_flags["ep-03"],
                    db=db)
    
        make_course_ep(course_slug="python-2025",
                    title="IF, ELIF, ELSE",
                    youtube_id="FV9Pzj3BIuU",
                    ep_slug="ep-04",
                    slug_flag=slugs_flags["ep-04"],
                    db=db)

        make_course_ep(course_slug="python-2025",
                    title="Laços de Repetição",
                    youtube_id="HcCH_xXwOcA",
                    ep_slug="ep-05",
                    slug_flag=slugs_flags["ep-05"],
                    db=db)
        
        make_course_ep(course_slug="python-2025",
                    title="Listas",
                    youtube_id="deWlTenrlv4",
                    ep_slug="ep-06",
                    slug_flag=slugs_flags["ep-06"],
                    db=db)

        make_course_ep(course_slug="python-2025",
                    title="Dicionários e Tuplas",
                    youtube_id="EueiZ_TXe_c",
                    ep_slug="ep-07",
                    slug_flag=slugs_flags["ep-07"],
                    db=db)

        make_course_ep(course_slug="python-2025",
                    title="Criano Funções",
                    youtube_id="JZlJ1otXBD8",
                    ep_slug="ep-08",
                    slug_flag=slugs_flags["ep-08"],
                    db=db)

        make_course_ep(course_slug="python-2025",
                    title="Módulos",
                    youtube_id="7U_NG78HuA4",
                    ep_slug="ep-09",
                    slug_flag=slugs_flags["ep-09"],
                    db=db)
        
        make_course_ep(course_slug="python-2025",
                    title="Lidando com Arquivos",
                    youtube_id="3h15kc10fCY",
                    ep_slug="ep-10",
                    slug_flag=slugs_flags["ep-10"],
                    db=db)

        make_course_ep(course_slug="python-2025",
                    title="Desafio Loteria da Babilônia",
                    youtube_id="lIczWRig7S8",
                    ep_slug="ep-11",
                    slug_flag=slugs_flags["ep-11"],
                    db=db)
        
        make_course_ep(course_slug="python-2025",
                    title="Consumindo dados de API",
                    youtube_id="iBsyZ0RQCqc",
                    ep_slug="ep-12",
                    slug_flag=slugs_flags["ep-12"],
                    db=db)

def curso_pandas(db:orm.Session, course_eps:pd.DataFrame):

    with st.expander("Pandas"):

        about = """
        Curso completo e gratuito de Pandas para pessoas iniciantes na área de dados.

        Pandas é uma biblioteca do ecossistema Python, uma das mais utilizadas e melhores documentadas para se trabalhar com processamento e análise de dados.
        Ela é o primeiro passo para qualquer pessoa que tem interesse pela área de dados poder realizar manipulações de dados de maneira digital e automalizar processos.

        Durante este curso, navegaremos entre os principais tipos de objetos do Pandas (Series e Dataframes), bem como seus métodos para relizar uma análise completa a partir de dados reais.
        Usamos formatos de arquivos csv, parquet e excel, bem como integrações com bancos de dados SQL para ingestão, coleta e processamento de dados usando queries. 

        """
        st.markdown(about)

        data = [
            {
                "title": "Ensinando Pandas - Ep 01",
                "youtube_id": "9Cw7iIjFlBc",
            },
            {
                "title": "Ensinando Pandas - Ep 02",
                "youtube_id": "mAR5V-22oA4",
            },
            {
                "title": "Ensinando Pandas - Ep 03",
                "youtube_id": "7E5Cr9lMdpU",
            },
            {
                "title": "Ensinando Pandas - Ep 04",
                "youtube_id": "bMEXh1K17eg",
            },
            {
                "title": "Ensinando Pandas - Ep 05",
                "youtube_id": "GNX0Bvo40M0",
            },
            {
                "title": "Ensinando Pandas - Ep 06",
                "youtube_id": "Tg3NVMbcgHs",
            },
            {
                "title": "Ensinando Pandas - Ep 07",
                "youtube_id": "NluSWHRZPFY",
            },
            {
                "title": "Ensinando Pandas - Ep 08",
                "youtube_id": "fWy5cNTWTeM",
            },
            {
                "title": "Ensinando Pandas - Ep 09",
                "youtube_id": "nN3MmJGDNxM",
            },
            {
                "title": "Ensinando Pandas - Ep 10",
                "youtube_id": "USpeepeztTI",
            },
            {
                "title": "Ensinando Pandas - Ep 11",
                "youtube_id": "OyO7lzlG3r8",
            },
            {
                "title": "Ensinando Pandas - Ep 12",
                "youtube_id": "VKclVgd7kZw",
            },
            {
                "title": "Ensinando Pandas - Ep 13",
                "youtube_id": "w5PLsNnUCTA",
            },
            {
                "title": "Ensinando Pandas - Ep 14",
                "youtube_id": "wOWCd-b8AuE",
            },
        ]

        slugs_flags = { f"ep-{i:02}": course_eps[course_eps["epSlug"] == f"ep-{i:02}"]["epSlug"].count() == 1 for i in range(1, len(data) + 1) }

        for i in range(len(data)):
            make_course_ep(
                course_slug="pandas-2025",
                title=data[i]["title"],
                youtube_id=data[i]["youtube_id"],
                ep_slug=list(slugs_flags.items())[i][0],
                slug_flag=list(slugs_flags.items())[i][1],
                db=db,
            )

def curso_sql(course_eps:pd.DataFrame):

    with st.expander("SQL - 07/07 a 18/07"):

        about = """
        Curso completo e gratuito de SQL para pessoas iniciantes na área de Dados.

        As aulas acontecerão nos dias 07/07 e 18/07, ai vivo na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

        SQL é uma das principais linguagens de consulta para bancos de dados relacionais. Se você deseja trabalhar com dados, é fundamental que você saiba como realizar consultas, inserções, atualizações e exclusões em um banco de dados.
        Além de ser uma das principais ferramentas no dia a dia de qualquer profissional da área de dados. Seja engenharia, ciência ou análise de dados, todos precisam saber SQL.

        Vamos pegar na sua mão e ensinar do básico até consultas mais complexas!

        [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=M2Fqc2hkajVxazhsOHFkNDFxdG4yOTg1aGZfMjAyNTA2MDlUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
        """
        st.markdown(about)
