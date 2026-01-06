import datetime
import time

from sqlalchemy import orm, select, func

from points import points
from conteudo import utils
from heroes import heroes
from retro import retro

import streamlit as st
import pandas as pd

from databases import models
from login import twitch_login

from databases import models


def show_points_infos(db:orm.Session)->bool:

    tmw_id = st.session_state.get("tmw_id", None)

    if not tmw_id:
        return False
    
    data = points.get_user_points(uuid=tmw_id)[0]
    st.session_state["tmw_user"] = data

    date_start = data["created_at"]
    date_last = data["updated_at"]

    col1, col2, col3 = st.columns([2,1,1])

    col1.markdown(f"""
    Saldo de cubos: {data["points"]}

    Última iteração: {date_last}

    Acumula pontos desde: {date_start}
    """)

    with col2.container(border=True):
        st.success("Ecossistema vinculado!")
        remove_buttom = st.button("Desvincular ecosistema")
        if remove_buttom:
            if models.remove_tmw_id(db, tmw_id):
                st.success("Usuário desvinculado com sucesso!")
                del st.session_state["tmw_user"]
                time.sleep(1)
                st.rerun()

    with col3.container(border=True):
        if st.user.is_logged_in and st.session_state["tmw_user"]:
            
            if st.session_state["tmw_user"]['email'] == st.user.email:
                st.success("Conta Google vinculada!")
                logout_google = st.button("Desvincular Google")
                if logout_google:
                    new_tmw_user = st.session_state["tmw_user"]
                    new_tmw_user["email"] = ""
                    new_tmw_user['youtube'] = ""
                    new_tmw_user['customer_name'] = ""
                    resp = points.update_user_points(**new_tmw_user)
                    if resp.status_code == 200:
                        st.logout()
                        st.success("Conta google desvinculada com sucesso.")

            else:            
                new_tmw_user = st.session_state["tmw_user"]
                new_tmw_user["email"] = st.user.email
                new_tmw_user['youtube'] = st.user.sub
                new_tmw_user['customer_name'] = st.user.name
                resp = points.update_user_points(**new_tmw_user)
                if resp.status_code == 200:
                    st.success("Conta google vinculada com sucesso.")
                    
        else:
            login_youtube = st.button("Vincule sua conta Google", help="Após realizar o login via Google, a página será recarregada e você precisará logar novamente na Twitch.")
            if login_youtube:
                st.login()

    return True
    

def integrate_or_create_tmw(db: orm.Session, user):
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


def show_rpg():

    tmw_id = st.session_state.get("tmw_id", None)
    twitch_name = st.session_state.get("twitch_data", {}).get("display_name", None)

    st.markdown("#### Minigame RPG")

    if not tmw_id or not twitch_name:
        st.warning("Você precisa vincular seu perfil ao ecossistema para acessar o RPG.")
        return

    with st.expander("Personagem RPG", expanded=False):
        char = heroes.get_creature(tmw_id)
        
        if "error" in char:
            heroes.show_create(tmw_id=tmw_id, twitch_name=name)
            return

        tab_char, tab_inventory, tab_store = st.tabs(["Personagem", "Inventário", "Loja"])
        with tab_char:
            heroes.show_char(char)
        
        with tab_inventory:
            heroes.show_inventory(char)

        with tab_store:
            heroes.show_store(char)
        
        return


def show_uncompleted_courses(courses_eps, user_courses_progress):
    courses = courses_eps[courses_eps['pctCompleted'] < 1]
    if courses.shape[0]:
        st.markdown("""### Cursos iniciados""")
        
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


def show_rewards(courses:pd.DataFrame):
    
    st.markdown("#### Recompensas")
    user_rewards = models.get_user_rewards(db, user_id=st.session_state['user'].userID)
    user_rewards = [i.rewardID for i in user_rewards]

    tmw_id = st.session_state.get("tmw_user", {}).get("uuid", None)
    user_id = st.session_state['user'].userID
    if not tmw_id:
        st.warning("Você precisa vincular seu perfil ao ecossistema para resgatar recompensas.")
        return

    courses_slugs = courses[~courses['courseSlug'].isin(user_rewards)]["courseSlug"].tolist()
    courses_slugs = {f"{i.replace('-', ' ').title()}": i for i in courses_slugs}

    if len(courses_slugs) == 0:
        st.markdown("Você não tem recompensas disponíveis. Finalize mais cursos para resgatar novas recompensas!")
        return

    check_reward = st.pills("Você tem recompensas te esperando:", courses_slugs.keys(), selection_mode="multi")

    if len(check_reward) > 0:
        if st.button("Confirme seu resgate!"):

            reward_ids = [courses_slugs[i] for i in check_reward]

            data = points.make_reward_transaction(tmw_id=tmw_id, reward_ids=reward_ids)
            resp = points.post_transaction(**data)
            if "error" in resp:
                st.error(f"Erro ao resgatar recompensas: {resp['error']}")
                return

            new_rewards = [models.UserRewards(userID=user_id, rewardID=i) for i in reward_ids]
            db.add_all(new_rewards)
            db.commit()
            
            st.success(f"Recomensa(s) resgatada(s) com sucesso! Foram adicionados {data['points']} cubos!")
            time.sleep(2)
            st.rerun()


def show_completed_courses(courses_eps:pd.DataFrame, user_courses_progress):
    courses = courses_eps[courses_eps['pctCompleted'] == 1]
    if not courses.empty:
        
        st.markdown("""### Cursos finalizados""")
        for s in courses['courseSlug']:
            utils.load_and_show_course(db, s, user_courses_progress)
        show_rewards(courses)



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


def show_user_progress_courses(db:orm.Session):
    user_id = st.session_state['user'].userID
    user_courses_progress = utils.get_courses_dataframe(db=db, user_id=user_id)
    user_courses_complete = make_user_progress_completed(db=db, user_courses_progress=user_courses_progress)

    if user_courses_complete.shape[0]> 0:
        show_uncompleted_courses(courses_eps=user_courses_complete, user_courses_progress=user_courses_progress)
        show_completed_courses(courses_eps=user_courses_complete, user_courses_progress=user_courses_progress)


def show_retro(userid, username):
    resp  = retro.get_retro(uuid=userid, name=username)
    if resp:
        st.success("Sua retrospectiva 2025 está pronta! Confira!")
        st.markdown(resp['report'])

    return None


db = models.SessionLocal()

twitch_login.twitch_login(db)

if 'user' not in st.session_state:
    st.error("Você não está logado. Por favor, faça login para acessar seu perfil.")
    st.stop()

user = st.session_state["user"]

tmw_id = models.get_tmw_id(db, user.userID)
st.session_state["tmw_id"] = tmw_id

twitch_data = twitch_login.get_twitch_infos(st.session_state['token'])
if "data" in twitch_data and len(twitch_data["data"]) > 0:
    name = twitch_data["data"][0]["display_name"]
    st.session_state["twitch_data"] = twitch_data["data"][0]
else:
    st.error("Não foi possível obter o nome do usuário da Twitch.")

if not show_points_infos(db):
    if st.button("Clique aqui para vincular seu perfil ao ecossistema"):
        integrate_or_create_tmw(db, user)

show_rpg()
show_user_progress_courses(db=db)

