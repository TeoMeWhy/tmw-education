import pandas as pd
from sqlalchemy import orm
import streamlit as st

from databases import models


def git_github(db:orm.Session, course_eps:pd.DataFrame):
    about = """
    Curso completo e gratuito de Git e Github para pessoas iniciantes na área da programação.
    O material e aulas foram realizadas ao vivo na [Twitch](https://twitch.tv/teomewhy) entre os dias 27/01 e 30/01, onde também está disponibilizado no [YouTube](https://youtube.com/@teomewhy).

    Se você tem interesse pela área de tecnologia ou dados, Git será uma ferramenta bastante companheira. Tenho certeza que nosso material poderá te ajudar nessa tragetória.

    Começamos do básico, conhecendo os comandos de `bash` no terminal, bem como as primeiras operações de Git (add, commit, status, etc), até realizarmos contribuições em repositórios remotos abertos para a comunidade.

    Confira o material da [apresentação aqui](https://docs.google.com/presentation/d/1a2tlT1-EtM8m_8NPvrU6rGpzFXROl_5e/edit?usp=sharing&ouid=109225010112567180899&rtpof=true&sd=true)

    Ao final de cada dia, há um checkbox para você salvar seu progresso durante este curso.
    """
    st.markdown(about)

    slugs_flags = {
        "ep-01": course_eps[course_eps['epSlug']=="ep-01"]['epSlug'].count() == 1,
        "ep-02": course_eps[course_eps['epSlug']=="ep-02"]['epSlug'].count() == 1,
        "ep-03": course_eps[course_eps['epSlug']=="ep-03"]['epSlug'].count() == 1,
        "ep-04": course_eps[course_eps['epSlug']=="ep-04"]['epSlug'].count() == 1,
        "ep-05": course_eps[course_eps['epSlug']=="ep-05"]['epSlug'].count() == 1,
        "ep-06": course_eps[course_eps['epSlug']=="ep-06"]['epSlug'].count() == 1,
        "ep-07": course_eps[course_eps['epSlug']=="ep-07"]['epSlug'].count() == 1,
        "ep-08": course_eps[course_eps['epSlug']=="ep-08"]['epSlug'].count() == 1,
    }


    # Ep 01
    st.markdown("#### Ep 01 - Instalação e Primeiros Conceitos")
    youtube_dia_01 = "84FhNXNWoig"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_01}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    checkbox_ep_01 = st.checkbox(label="Episódio 01 feito!", value=slugs_flags["ep-01"])
    if checkbox_ep_01 != slugs_flags["ep-01"] and 'user' in st.session_state:
        if checkbox_ep_01:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-01")
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-01")
            

    # Ep 02
    st.markdown("#### Ep 02 - Primeiros Comandos Git")
    youtube_dia_02 = "RZ0g18hstwQ"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_02}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    checkbox_ep_02 = st.checkbox(label="Episódio 02 feito!", value=slugs_flags["ep-02"])
    if checkbox_ep_02 != slugs_flags["ep-02"] and 'user' in st.session_state:
        if checkbox_ep_02:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-02")
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-02")
            

    # Ep 03
    st.markdown("#### Ep 03 - Lidando com Branches")
    youtube_dia_03 = "pzjdEQOmsLA"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_03}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    checkbox_ep_03 = st.checkbox(label="Episódio 03 feito!", value=slugs_flags["ep-03"])
    if checkbox_ep_03 != slugs_flags["ep-03"] and 'user' in st.session_state:
        if checkbox_ep_03:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-03")
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-03")
            

    # Ep 04
    st.markdown("#### Ep 04 - Resolvendo Conflitos")
    youtube_dia_04 = "IRmjluONHxU"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_04}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    checkbox_ep_04 = st.checkbox(label="Episódio 04 feito!", value=slugs_flags["ep-04"])
    if checkbox_ep_04 != slugs_flags["ep-04"] and 'user' in st.session_state:
        if checkbox_ep_04:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-04")
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-04")
            

    # Ep 05
    st.markdown("#### Ep 05 - Realizando Pull Requests")
    youtube_dia_05 = "Y_fFZjzw-D4"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_05}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    checkbox_ep_05 = st.checkbox(label="Episódio 05 feito!", value=slugs_flags["ep-05"])
    if checkbox_ep_05 != slugs_flags["ep-05"] and 'user' in st.session_state:
        if checkbox_ep_05:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-05")
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-05")
            

    # Ep 06
    st.markdown("#### Ep 06 - Criando FORK")
    youtube_dia_06 = "vWtrTmjis2w"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_06}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    checkbox_ep_06 = st.checkbox(label="Episódio 06 feito!", value=slugs_flags["ep-06"])
    if checkbox_ep_06 != slugs_flags["ep-06"] and 'user' in st.session_state:
        if checkbox_ep_06:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-06")
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-06")
            
    
    # Ep 07
    st.markdown("#### Ep 07 - Integração com Visual Studio Code")
    youtube_dia_07 = "M-mBmYj7Jh4"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_07}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    checkbox_ep_07 = st.checkbox(label="Episódio 07 feito!", value=slugs_flags["ep-07"])
    if checkbox_ep_07 != slugs_flags["ep-07"] and 'user' in st.session_state:
        if checkbox_ep_07:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-07")
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-07")
            

    # Ep 08
    st.markdown("#### Ep 08 - Git Flow")
    youtube_dia_08 = "l44uGe-sxgM"
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_dia_08}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    checkbox_ep_08 = st.checkbox(label="Episódio 08 feito!", value=slugs_flags["ep-08"])
    if checkbox_ep_08 != slugs_flags["ep-08"] and 'user' in st.session_state:
        if checkbox_ep_08:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-08")
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug="github", ep_slug="ep-08")
            