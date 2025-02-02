import streamlit as st


def git_github():
    about = """
    Curso completo e gratuito de Git e Github para pessoas iniciantes na área da programação.
    O material e aulas foram realizadas ao vivo na [Twitch](https://twitch.tv/teomewhy) entre os dias 27/01 e 30/01, onde também está disponibilizado no [YouTube](https://youtube.com/@teomewhy).

    Se você tem interesse pela área de tecnologia ou dados, Git será uma ferramenta bastante companheira. Tenho certeza que nosso material poderá te ajudar nessa tragetória.

    Começamos do básico, conhecendo os comandos de `bash` no terminal, bem como as primeiras operações de Git (add, commit, status, etc), até realizarmos contribuições em repositórios remotos abertos para a comunidade.

    Confira o material da [apresentação aqui](https://docs.google.com/presentation/d/1a2tlT1-EtM8m_8NPvrU6rGpzFXROl_5e/edit?usp=sharing&ouid=109225010112567180899&rtpof=true&sd=true)

    Ao final de cada dia, há um checkbox para você salvar seu progresso durante este curso.
    """
    st.markdown(about)

    # DIA 01
    st.markdown("#### Dia 01 - Instalação e Primeiros Conceitos")
    youtube_dia_01 = "84FhNXNWoig"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_01}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    st.checkbox(label="Dia 01 feito!")

    # DIA 02
    st.markdown("#### Dia 02 - Primeiros Comandos Git")
    youtube_dia_02 = "RZ0g18hstwQ"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_02}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    st.checkbox(label="Dia 02 feito!")

    # DIA 03
    st.markdown("#### Dia 03 - Lidando com Branches")
    youtube_dia_03 = "pzjdEQOmsLA"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_03}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    st.checkbox(label="Dia 03 feito!")

    # DIA 04
    st.markdown("#### Dia 04 - Resolvendo Conflitos")
    youtube_dia_04 = "IRmjluONHxU"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_04}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    st.checkbox(label="Dia 04 feito!")

    # DIA 05
    st.markdown("#### Dia 05 - Realizando Pull Requests")
    youtube_dia_05 = "Y_fFZjzw-D4"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_05}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    st.checkbox(label="Dia 05 feito!")

    # DIA 06
    st.markdown("#### Dia 06 - Criando FORK")
    youtube_dia_06 = "vWtrTmjis2w"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_06}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    st.checkbox(label="Dia 06 feito!")
    
    # DIA 07
    st.markdown("#### Dia 07 - Criando FORK")
    youtube_dia_07 = "M-mBmYj7Jh4"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_07}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    st.checkbox(label="Dia 07 feito!")

    # DIA 08
    st.markdown("#### Dia 08 - Git Flow")
    youtube_dia_08 = "l44uGe-sxgM"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_08}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    st.checkbox(label="Dia 08 feito!")