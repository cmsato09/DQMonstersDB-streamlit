import pandas as pd
import streamlit as st

from helper_functions import get_skills_list, hide_table_index

# TODO refactor page configuration into function (?)


def make_clickable(idx, name):
    return f'<a target="_self" href="skill_detail?id={idx}">{name}</a>'


def reformat_skills_df(json_data):
    df = pd.DataFrame(json_data)

    # creates hyperlinkable text using name of skill
    df["link"] = df.apply(lambda x: make_clickable(x["id"], x["old_name"]), axis=1)

    df.rename(
        columns={
            "link": "NAME",
            "category_type": "CATEGORY",
            "family_type": "FAMILY",
            "description": "DESCRIPTION",
            "mp_cost": "MP COST",
        },
        inplace=True,
    )
    df = df[["NAME", "CATEGORY", "FAMILY", "DESCRIPTION", "MP COST"]]

    return df


def query_skill_data(df, category_type_search, family_type_search):
    if category_type_search and family_type_search:
        df = df.query(
            "CATEGORY == @category_type_search & " "FAMILY == @family_type_search"
        )
    elif category_type_search:
        df = df.query("CATEGORY == @category_type_search")
    elif family_type_search:
        df = df.query("FAMILY == @family_type_search")

    return df


if __name__ == "__main__":
    skill_data = get_skills_list()
    skill_data = reformat_skills_df(skill_data)

    st.markdown("## Skills Table")
    category_type_searchbox = st.multiselect(
        label="Search by category type", options=skill_data["CATEGORY"].unique()
    )
    family_type_searchbox = st.multiselect(
        label="Search by family type", options=skill_data["FAMILY"].unique()
    )

    skill_data = query_skill_data(
        skill_data, category_type_searchbox, family_type_searchbox
    )
    hide_table_index()

    st.write(skill_data.to_html(escape=False, index=False), unsafe_allow_html=True)
