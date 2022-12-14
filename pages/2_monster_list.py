import streamlit as st
from helper_functions import get_monster_list

# FastAPI connection
monster_list = get_monster_list()

st.markdown("## Monster List")
name_search = st.text_input("Search by Name")
family_search = st.selectbox(label="Search by Family",
                             options=['', 'SLIME', 'DRAGON', 'BEAST', 'BIRD',
                                      'PLANT', 'BUG', 'DEVIL', 'UNDEAD',
                                      'MATERIAL', '???'],
                             )

# Set up column table
name_column, family_column = st.columns(2)
name_column.subheader('Monster Name')
family_column.subheader('Family Type')


def write_monster():
    name_column.write(
        f"<a target='_self' href='monster_detail?id={idx}'>{name}</a>",
        unsafe_allow_html=True
    )
    family_column.write(monster['family']['family_eng'])


for monster in monster_list:
    idx = monster['id']
    name = monster['old_name']

    if name_search and family_search:
        if name_search.lower() in name.lower() and monster['family']['family_eng'] == family_search:
            write_monster()
    elif name_search:
        if name_search.lower() in name.lower():
            write_monster()
    elif family_search:
        if monster['family']['family_eng'] == family_search:
            write_monster()
    else:
        write_monster()
