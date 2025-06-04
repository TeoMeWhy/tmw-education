import pandas as pd
import streamlit as st
from sqlalchemy import orm

from ..utils import make_course_ep

def curso_machine_learning(course_eps:pd.DataFrame):

    with st.expander("Machine Learning - 09/06 a 20/06"):

        about = """
        Curso completo e gratuito de Machine Learning para pessoas iniciantes na área da Ciência de Dados.

        As aulas acontecerão nos dias 09/06 e 20/06 às 9AM, ao vivo na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

        O uso de técnicas voltadas à Aprendizado de Máquina tem sido cada dia mais comuns em diferentes mercados e indústricas. Dominar os principais conceitos te ajudará a alcançar não só objetivos da sua empresa, mas também, de crescimento profissional.
        Neste curso, você aprenderá os principais conceitos de Machine Learning, mais do que apenas apertar os botões corretos. Falaremos sobre realmente como a máquina aprender e como podemos avaliar esse aprendizados a partir de diferentes métricas.

        Você entenderá de uma vez por todas como cada técnica funciona, e as métricas de performance. Quando falarem sobre curva ROC, você terá condições de explicar como funciona e porque normalmente é uma métrica melhor que a acurácia. 

        [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=M2Fqc2hkajVxazhsOHFkNDFxdG4yOTg1aGZfMjAyNTA2MDlUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
        """
        st.markdown(about)
