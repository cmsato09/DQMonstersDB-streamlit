import streamlit as st
from helper_functions import get_skills_list

st.markdown("## Skills Table")

skill_data = get_skills_list()
st.dataframe(skill_data)
