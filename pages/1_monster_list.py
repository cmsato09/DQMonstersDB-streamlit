import pandas as pd
import streamlit as st

from helper_functions import (
    get_monster_list,
    hide_table_index,
    make_clickable_monster_name,
)


def reformat_monster_list(json_data):
    df = pd.json_normalize(json_data)

    # creates hyperlinkable name text
    df['link'] = df.apply(
        lambda x: make_clickable_monster_name(x['id'], x['old_name']), axis=1
    )

    df.rename(
        columns={
            'link': 'NAME',
            'family.family_eng': 'FAMILY'
        },
        inplace=True
    )
    df = df[['NAME', 'FAMILY']]
    return df


def query_monster_list(df, name_search, family_search):
    if name_search and family_search:
        df = df[(df['NAME'].str.lower().str.contains(name_search.lower())) &
                (df['FAMILY'] == family_search)]
    elif name_search:
        df = df[df['NAME'].str.lower().str.contains(name_search.lower())]
    elif family_search:
        df = df[df['FAMILY'] == family_search]
    return df


if __name__ == "__main__":
    monster_list = get_monster_list()
    monster_list = reformat_monster_list(monster_list)

    st.markdown("## Monster List")
    name_searchbox = st.text_input("Search by Name")
    family_searchbox = st.selectbox(label="Search by Family",
                                    options=['', 'SLIME', 'DRAGON', 'BEAST',
                                             'BIRD', 'PLANT', 'BUG', 'DEVIL',
                                             'UNDEAD', 'MATERIAL', '???']
                                    )

    monster_list = query_monster_list(monster_list, name_searchbox,
                                      family_searchbox)
    hide_table_index()

    st.write(
        monster_list.to_html(escape=False, index=True),
        unsafe_allow_html=True
    )
