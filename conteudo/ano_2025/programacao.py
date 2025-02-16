import pandas as pd
import streamlit as st
from sqlalchemy import orm

from ..utils import make_course_ep



def curso_python(db:orm.Session, course_eps:pd.DataFrame):
    about = """
    Curso completo e gratuito de Python para pessoas iniciantes na área da programação.

    As aulas de Python acontecerão entre os dias 10/02 e 14/02, ai vivo na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

    Python é uma das linguagens mais utilizadas no mundo da computação. Não apenas para criar sites, mas também para análise, engenha e ciência de dados.
    Bem como, tem grande aplicações científicas no meio acadêmico, além, é claro de vasta aplicação com inteligência artificial.

    A ideia principal deste curso é fornecer o conhecimento mínimo sobre lógica de programação, sintaxe da linguagem Python e suas principais estruturas de dados e controle de fluxo, como laços de repetição e operadores lógicos/condicionais.

    [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=Mm9laTlqaWlwOWxucjJrbDFkbnFzdjJham5fMjAyNTAyMTBUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
    """
    st.markdown(about)

    slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,8)}
        

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


def curso_pandas(course_eps:pd.DataFrame):
    about = """
    Curso completo e gratuito de Pandas para pessoas iniciantes na área de dados.

    As aulas acontecerão entre os dias 10/03 e 14/03, ao vivo na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

    Pandas é uma biblioteca do ecossistema Python, uma das mais utilizadas e melhores documentadas para se trabalhar com processamento e análise de dados.
    Ela é o primeiro passo para qualquer pessoa que tem interesse pela área de dados poder realizar manipulações de dados de maneira digital e automalizar processos.

    Durante este curso, navegaremos entre os principais tipos de objetos do Pandas (Series e Dataframes), bem como seus métodos para relizar uma análise completa a partir de dados reais.
    Usamos formatos de arquivos csv, parquet e excel, bem como integrações com bancos de dados SQL para ingestão, coleta e processamento de dados usando queries. 

    [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=NWlwNzdub2IyNTlibGFzdHY3MWVsajZtNzBfMjAyNTAzMTBUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
    """
    st.markdown(about)
