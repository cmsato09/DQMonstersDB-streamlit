import streamlit as st
import pandas as pd

st.markdown("# Skills Table")

with open('json_test_files/skills_dummy_data.json') as json_file:
    skill_data = pd.read_json(json_file)

st.dataframe(skill_data)
