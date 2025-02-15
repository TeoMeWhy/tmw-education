import pandas as pd
from sqlalchemy import orm
import streamlit as st

from databases import models

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
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """
    st.components.v1.html(html_code, height=315)
    label = f"{course_slug.replace("-", " ").title()} {ep_title} Feito!"
    checkbox_ep = st.checkbox(label=label, value=slug_flag)
    if checkbox_ep != slug_flag and 'user' in st.session_state:
        if checkbox_ep:
            models.insert_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug=course_slug, ep_slug=ep_slug)
        else:
            models.delete_user_course_ep(db, user_id=st.session_state['user'].userID, course_slug=course_slug, ep_slug=ep_slug)
        