import streamlit as st
import pandas as pd
from helper_functions import get_skill_detail

st.markdown('## Skill Detail Info Page Example')

params = st.experimental_get_query_params()
if "id" in params:
    skill_id = params["id"]
else:
    skill_id = st.number_input(
        label="Input skill ID",
        min_value=1, max_value=154
    )

if skill_id:
    skill_data = get_skill_detail(skill_id)

st.write(f"Game Name:  **{skill_data['old_name']}**")
