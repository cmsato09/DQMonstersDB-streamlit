from Home import get_json_data
import streamlit as st
import pandas as pd


# FastAPI connection
API_BASE = "http://localhost:8000"
API_GET_SKILLS_LIST = API_BASE + "/dqm1/skills/"

st.markdown("## Skills Table")

# dummy json data test
# with open('json_test_files/skills_dummy_data.json') as json_file:
#     skill_data = pd.read_json(json_file)

skill_data = get_json_data(API_GET_SKILLS_LIST)
st.dataframe(skill_data)
