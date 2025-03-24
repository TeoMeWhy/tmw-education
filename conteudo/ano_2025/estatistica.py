import pandas as pd
import streamlit as st

def curso_estatistica(course_eps:pd.DataFrame):

    with st.expander("Estatística Básica: 05/05 a 16/05"):

        about = """
        Curso gratuido de Estatística (Parte I) para pessoas iniciantes na área de dados.

        Essas aulas acontecerão ao vivo entre os dias 05/05 e 16/05, na [Twitch](https://twitch.tv/teomewhy), onde, posteriormente será disponibilizado no [YouTube](https://youtube.com/@teomewhy).

        Estatística é uma das principais disciplinas para a área de dados. Desde análise simples, mas tambem, toda base para avançarmos em aprendizado de máquina, se faz necessário o conhecimento de métodos e modelos estatísticos.
        
        Vamos fornecer o conhecimento sobre Estatística de forma introdutória. Mas não subestime nosso material. Cobriremos:

        - Conceitos de população (parâmetro) e amostra (estimadores);
        - Estatística descritiva;
        - Representações gráficas;
        - Probabilidade;
        - Intervalo de confiânça;
        - Testes de hipótese;

        Depois de passarmos por todos esses conceitos teóricos, vamos aplica-los via programação em Python.

        [Adicione na sua agenda](https://calendar.google.com/calendar/event?action=TEMPLATE&tmeid=Njc2YjJ0YXEyYXYyZG1xcTVxOGRjc2llbDBfMjAyNTA1MDVUMTEwMDAwWiB0ZW9AdGVvbWV3aHkub3Jn&tmsrc=teo%40teomewhy.org&scp=ALL) para participar conosco ao vivo.
        """
        st.markdown(about)
