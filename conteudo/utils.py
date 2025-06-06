import pandas as pd
from sqlalchemy import orm
import streamlit as st

from sqlalchemy import orm, select

from databases.models import Course, CourseEps
from databases import models


def load_and_show_course(db:orm.Session, course_slug:str, user_courses_progress:pd.DataFrame, alt_text=""):

    course = db.scalar(select(Course).where(Course.slug==course_slug))
    course_eps = db.scalars(select(CourseEps).where(CourseEps.slug==course_slug))
    user_course_data = user_courses_progress[user_courses_progress['courseSlug']==course_slug]

    with st.expander(course.name + alt_text):
        st.markdown(course.description)

        for c in course_eps:
            ep_slug = f'ep-{c.ep:02}'
            ep_slug_flag = ep_slug in user_course_data['epSlug'].tolist()

            make_course_ep(
                course_slug=c.slug ,
                title=c.title,
                youtube_id=c.youtube_id,
                ep_slug=ep_slug,
                slug_flag=ep_slug_flag,
                db=db,
            )


def get_courses_dataframe(db:orm.Session, user_id:str)->pd.DataFrame:
    courses_progress = pd.DataFrame(columns=["userID","courseSlug","epSlug","createdAt"])
    resp = models.get_courses_complet_by_user(db, user_id=user_id)
    if len(resp) > 0:
        courses_progress = pd.DataFrame([{
                            "userID": i.userID,
                            "courseSlug": i.courseSlug,
                            "epSlug": i.epSlug,
                            "createdAt": i.createdAt,
        } for i in resp])
    return courses_progress


def make_course_ep(course_slug:str, title:str, youtube_id:str, ep_slug:str, slug_flag:bool, db:orm.Session):
    ep_title = ep_slug.replace("-", " ").title()
    st.markdown(f"#### {ep_title} - {title.title()}")
    html_code = f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube_id}" 
    frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen loading="lazy"></iframe>
    """
    st.components.v1.html(html_code, height=315)
    label = f"{course_slug.replace("-", " ").title()} {ep_title} Feito!"
    checkbox_ep = st.checkbox(label=label, value=slug_flag)
    if checkbox_ep != slug_flag and 'user' in st.session_state:
        if checkbox_ep:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug=course_slug, ep_slug=ep_slug)
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug=course_slug, ep_slug=ep_slug)
        