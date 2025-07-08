import datetime
import time

from sqlalchemy import orm, select, func

from points import points
from conteudo import utils
from heroes import heroes

import streamlit as st
import pandas as pd

from databases import models
from login import twitch_login

from databases import models


def show_points_infos(db:orm.Session, tmw_id:str)->bool:

    if not tmw_id:
        return False
    
    data = points.get_user_points(uuid=tmw_id)[0]
    st.session_state["tmw_user"] = data

    date = datetime.datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_start = date.strftime("%Y-%m-%d %H:%M:%S")

    date = datetime.datetime.strptime(data["updated_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_last = date.strftime("%Y-%m-%d %H:%M:%S")

    col1, col2 = st.columns(2)

    col1.markdown(f"""
    Saldo de cubos: {data["points"]}

    Última iteração: {date_last}

    Acumula pontos desde: {date_start}
    """)
        
    with col2:
        remove_buttom = col2.button("Clique para desvincular seu perfil do ecosistema")
        if remove_buttom:
            if models.remove_tmw_id(db, tmw_id):
                st.success("Usuário desvinculado com sucesso!")
                del st.session_state["tmw_user"]
                time.sleep(1)
                st.rerun()

    return True
    

def integrate_or_create_tmw(user):
    payload = {user.platformName:user.platformUserID}
    
    data = points.get_user_points(**payload)
    if len(data) == 1:
        models.integrate_tmw_id(db=db, userID=user.userID, tmwID=data[0]["uuid"])

    else:
        data = points.create_user_points(**payload)
        models.integrate_tmw_id(db=db, userID=user.userID, tmwID=data["uuid"])

    st.success("Perfil vinculado com sucesso!")
    time.sleep(1)
    st.rerun()

def show_rpg(tmw_id:str, twitch_name:str):

    with st.expander("Personagem RPG", expanded=False):
        char = heroes.get_creature(tmw_id)
        
        if "error" in char:
            heroes.show_create(tmw_id=tmw_id, twitch_name=name)
            return

        heroes.show_char(char)
        return


def show_uncompleted_courses(courses_eps, user_courses_progress):
    courses = courses_eps[courses_eps['pctCompleted'] < 1]
    if courses.shape[0]:
        st.markdown("""## Cursos iniciados""")
        
        for i in courses.index:
            line = courses.loc[i]
            slug = line['courseSlug']
            qtdUser = line['qtdeEpsUser']
            qtdCourse = line['qtdEpsCourse']
            pct = line['pctCompleted']

            alt_text = f"  -  {pct*100:.2f}% ({qtdUser:.0f}/{qtdCourse:.0f})"

            utils.load_and_show_course(db=db,
                                       course_slug=slug,
                                       user_courses_progress=user_courses_progress,
                                       alt_text=alt_text)


def show_completed_courses(courses_eps, user_courses_progress):
    courses = courses_eps[courses_eps['pctCompleted'] == 1]
    if courses.shape[0]:
        st.markdown("""## Cursos finalizados""")
        for s in courses['courseSlug']:
            utils.load_and_show_course(db, s, user_courses_progress)


def make_user_progress_completed(db: orm.Session, user_courses_progress:pd.DataFrame):

    user_courses_complete = (user_courses_progress.groupby('courseSlug')['epSlug']
                                           .count()
                                           .reset_index()
                                           .rename(columns={"epSlug":"qtdeEpsUser"}))

    query = (select(models.CourseEps.slug, func.count())
            .where(models.CourseEps.slug
                        .in_(user_courses_complete['courseSlug'].tolist()))
            .group_by(models.CourseEps.slug))

    user_courses_complete = (user_courses_complete.merge(pd.read_sql_query(query, db.get_bind())
                                                         .rename(columns={"count_1": "qtdEpsCourse"}),
                                                         how='inner',
                                                         left_on='courseSlug',
                                                         right_on='slug')
                                                 .drop("slug", axis=1))

    user_courses_complete['pctCompleted'] = user_courses_complete['qtdeEpsUser'] / user_courses_complete['qtdEpsCourse']
    return user_courses_complete


def show_user_progress_courses(db:orm.Session, user_id):
    user_courses_progress = utils.get_courses_dataframe(db=db, user_id=user_id)
    user_courses_complete = make_user_progress_completed(db=db, user_courses_progress=user_courses_progress)

    if user_courses_complete.shape[0]> 0:
        show_uncompleted_courses(courses_eps=user_courses_complete, user_courses_progress=user_courses_progress)
        show_completed_courses(courses_eps=user_courses_complete, user_courses_progress=user_courses_progress)


db = models.SessionLocal()

twitch_login.twitch_login(db)

st.markdown(
"""
# Seu perfil aqui!
"""
)

if 'user' not in st.session_state:
    st.error("Você não está logado. Por favor, faça login para acessar seu perfil.")
    st.stop()

user = st.session_state["user"]
tmw_id = models.get_tmw_id(db, user.userID)

twitch_data = twitch_login.get_twitch_infos(st.session_state['token'])
if "data" in twitch_data and len(twitch_data["data"]) > 0:
    name = twitch_data["data"][0]["display_name"]
else:
    st.error("Não foi possível obter o nome do usuário da Twitch.")

if not show_points_infos(db, tmw_id):
    b = st.button("Clique aqui para vincular seu perfil ao ecossistema", on_click=lambda: integrate_or_create_tmw(user))

show_rpg(tmw_id=tmw_id, twitch_name=name)

show_user_progress_courses(db=db, user_id=user.userID)

