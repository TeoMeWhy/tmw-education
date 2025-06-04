import pandas as pd
import streamlit as st
from sqlalchemy import orm


def curso_sql(course_eps:pd.DataFrame):

    with st.expander("SQL - 07/07 a 18/07"):

        about = """
        Curso completo e gratuito de SQL para pessoas iniciantes na área de Dados.

        As aulas acontecerão nos dias 07/07 e 18/07 às 9AM, ao vivo na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

        SQL é uma das principais linguagens de consulta para bancos de dados relacionais. Se você deseja trabalhar com dados, é fundamental que você saiba como realizar consultas, inserções, atualizações e exclusões em um banco de dados.
        Além de ser uma das principais ferramentas no dia a dia de qualquer profissional da área de dados. Seja engenharia, ciência ou análise de dados, todos precisam saber SQL.

        Vamos pegar na sua mão e ensinar do básico até consultas mais complexas!

        [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=M2Fqc2hkajVxazhsOHFkNDFxdG4yOTg1aGZfMjAyNTA2MDlUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
        """
        st.markdown(about)
