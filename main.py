import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(initial_sidebar_state='auto')

nav = get_nav_from_toml(".streamlit/pages_sections.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()