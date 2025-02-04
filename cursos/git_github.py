import pandas as pd
from sqlalchemy import orm
import streamlit as st

from .utils import make_course_ep
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

    slugs_flags = {f"ep-{i:02}": course_eps[course_eps['epSlug']==f"ep-{i:02}"]['epSlug'].count() == 1 for i in range(1,10)}
        

    # Ep 01
    make_course_ep(course_slug="github",
                   title="Instalação e Primeiros Conceitos",
                   youtube_id="84FhNXNWoig",
                   ep_slug="ep-01",
                   slug_flag=slugs_flags["ep-01"],
                   db=db)

    make_course_ep(course_slug="github",
                   title="Primeiros Comandos Git",
                   youtube_id="RZ0g18hstwQ",
                   ep_slug="ep-02",
                   slug_flag=slugs_flags["ep-02"],
                   db=db)

    make_course_ep(course_slug="github",
                   title="Lidando com Branches",
                   youtube_id="pzjdEQOmsLA",
                   ep_slug="ep-03",
                   slug_flag=slugs_flags["ep-03"],
                   db=db)
   
    make_course_ep(course_slug="github",
                   title="Resolvendo Conflitos",
                   youtube_id="IRmjluONHxU",
                   ep_slug="ep-04",
                   slug_flag=slugs_flags["ep-04"],
                   db=db)

    make_course_ep(course_slug="github",
                   title="Realizando Pull Requests",
                   youtube_id="Y_fFZjzw-D4",
                   ep_slug="ep-05",
                   slug_flag=slugs_flags["ep-05"],
                   db=db)
    
    make_course_ep(course_slug="github",
                   title="Criando FORK",
                   youtube_id="vWtrTmjis2w",
                   ep_slug="ep-06",
                   slug_flag=slugs_flags["ep-06"],
                   db=db)

    make_course_ep(course_slug="github",
                   title="Integração com Visual Studio Code",
                   youtube_id="M-mBmYj7Jh4",
                   ep_slug="ep-07",
                   slug_flag=slugs_flags["ep-07"],
                   db=db)

    make_course_ep(course_slug="github",
                   title="Git Flow",
                   youtube_id="l44uGe-sxgM",
                   ep_slug="ep-08",
                   slug_flag=slugs_flags["ep-08"],
                   db=db)

    make_course_ep(course_slug="github",
                   title="Gitignore e Gitkeep",
                   youtube_id="spoUnf34R4A",
                   ep_slug="ep-09",
                   slug_flag=slugs_flags["ep-09"],
                   db=db)

