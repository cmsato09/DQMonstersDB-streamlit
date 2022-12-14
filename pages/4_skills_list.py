import streamlit as st
import pandas as pd
from helper_functions import get_skills_list, hide_table_index

# TODO refactor page configuration into function (?)


def make_clickable(idx, name):
    return f'<a target="_blank" href="skill_detail?id={idx}">{name}</a>'


def reformat_skills_df(json_data):
    df = pd.DataFrame(json_data)
    df['link'] = df.apply(lambda x: make_clickable(x['id'], x['old_name']), axis=1)

    df = df[['link', 'category_type', 'family_type', 'description',
             'mp_cost', 'required_level', 'required_hp', 'required_mp',
             'required_attack', 'required_defense', 'required_speed',
             'required_intelligence']]
    df = df.astype({'required_hp': 'Int64', 'required_mp': 'Int64',
                    'required_attack': 'Int64', 'required_defense': 'Int64',
                    'required_speed': 'Int64',
                    'required_intelligence': 'Int64'})
    return df


def query_skill_data(df):
    if category_type_search and family_type_search:
        df = df.query(
            "category_type == @category_type_search & family_type == @family_type_search")
    elif category_type_search:
        df = df.query("category_type == @category_type_search")
    elif family_type_search:
        df = df.query("family_type == @family_type_search")

    return df


if __name__ == "__main__":
    skill_data = get_skills_list()
    skill_data = reformat_skills_df(skill_data)

    st.markdown("## Skills Table")
    category_type_search = \
        st.multiselect(label="Search by category type",
                       options=skill_data["category_type"].unique())
    family_type_search = \
        st.multiselect(label="Search by family type",
                       options=skill_data["family_type"].unique())

    skill_data = query_skill_data(skill_data)
    hide_table_index()
    # TODO: table too wide now, apply css?
    st.write(skill_data.to_html(escape=False, index=False), unsafe_allow_html=True)
