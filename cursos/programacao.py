import pandas as pd
import streamlit as st

def curso_python(course_eps:pd.DataFrame):
    about = """
    Curso completo e gratuito de Python para pessoas iniciantes na área da programação.

    As aulas de Python acontecerão entre os dias 10/02 e 14/02, ai vivo na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

    Python é uma das linguagens mais utilizadas no mundo da computação. Não apenas para criar sites, mas também para análise, engenha e ciência de dados.
    Bem como, tem grande aplicações científicas no meio acadêmico, além, é claro de vasta aplicação com inteligência artificial.

    A ideia principal deste curso é fornecer o conhecimento mínimo sobre lógica de programação, sintaxe da linguagem Python e suas principais estruturas de dados e controle de fluxo, como laços de repetição e operadores lógicos/condicionais.

    [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=Mm9laTlqaWlwOWxucjJrbDFkbnFzdjJham5fMjAyNTAyMTBUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
    """
    st.markdown(about)


def curso_pandas(course_eps:pd.DataFrame):
    about = """
    Curso completo e gratuito de Pandas para pessoas iniciantes na área de dados.

    As aulas acontecerão nos dias 10/03 e 14/03, ai vivo na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

    Pandas é uma biblioteca do ecossistema Python, uma das mais utilizadas e melhores documentadas para se trabalhar com processamento e análise de dados.
    Ela é o primeiro passo para qualquer pessoa que tem interesse pela área de dados poder realizar manipulações de dados de maneira digital e automalizar processos.

    Durante este curso, navegaremos entre os principais tipos de objetos do Pandas (Series e Dataframes), bem como seus métodos para relizar uma análise completa a partir de dados reais.
    Usamos formatos de arquivos csv, parquet e excel, bem como integrações com bancos de dados SQL para ingestão, coleta e processamento de dados usando queries. 

    [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=NWlwNzdub2IyNTlibGFzdHY3MWVsajZtNzBfMjAyNTAzMTBUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
    """
    st.markdown(about)
