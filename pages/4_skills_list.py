import streamlit as st
from helper_functions import APINames, _get_json_data

st.markdown("## Skills Table")

skill_data = _get_json_data(APINames.API_GET_SKILLS_LIST)
st.dataframe(skill_data)
