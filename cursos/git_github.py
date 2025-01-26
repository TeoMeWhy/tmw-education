import streamlit as st


def git_github():
    about = """
    Curso completo e gratuito de Git e Github para pessoas iniciantes na área da programação.
    O material e aulas foram realizadas ao vivo na [Twitch](https://twitch.tv/teomewhy) entre os dias 27/01 e 30/01, onde também está disponibilizado no [YouTube](https://youtube.com/@teomewhy).

    Se você tem interesse pela área de tecnologia ou dados, Git será uma ferramenta bastante companheira. Tenho certeza que nosso material poderá te ajudar nessa tragetória.

    Começamos do básico, conhecendo os comandos de `bash` no terminal, bem como as primeiras operações de Git (add, commit, status, etc), até realizarmos contribuições em repositórios remotos abertos para a comunidade.
    """
    st.markdown(about)

    st.markdown("#### Dia 01 - Conceitos e primeiros comandos")
    youtube_dia_01 = "PsCJWAkA8S4"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_01}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)

    st.markdown("#### Dia 02 - Conhecendo o GitHub")
    youtube_dia_02 = "PsCJWAkA8S4"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_02}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)

    st.markdown("#### Dia 03 - Fluxo de trabalho com Gitflow")
    youtube_dia_03 = "PsCJWAkA8S4"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_03}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)

    st.markdown("#### Dia 04 - Fluxo de trabalho com Visual Studio Code")
    youtube_dia_04 = "PsCJWAkA8S4"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_04}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)