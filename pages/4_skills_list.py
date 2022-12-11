import streamlit as st
import pandas as pd
from helper_functions import get_skills_list

# TODO add skill hyperlink to skill_detail page
# TODO refactor page configuration into function (?)


def reformat_skills_df(json_data):
    df = pd.DataFrame(json_data)
    df = df[['old_name', 'category_type', 'family_type', 'description',
             'mp_cost']]
    return df


if __name__ == "__main__":
    skill_data = get_skills_list()
    skill_data = reformat_skills_df(skill_data)

    st.markdown("## Skills Table")
    category_search = st.multiselect(label="Search by category type",
                                     options=skill_data["category_type"].unique())
    shop_search = st.multiselect(label="Search by family type",
                                 options=skill_data["family_type"].unique())
    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.table(skill_data)
