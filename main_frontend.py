import json
import streamlit as st

st.markdown("# Monster List")

with open('json_test_files/read_monsters.json') as json_file:
    monster_data = json.load(json_file)

name_search = st.text_input("Search by Name")
family_search = st.selectbox("Search by Family",
                             ['SLIME', 'DRAGON', 'BEAST', 'BIRD', 'PLANT',
                              'BUG', 'DEVIL', 'UNDEAD', 'MATERIAL', '???'])

# Set up column table
name_column, family_column = st.columns(2)
name_column.subheader('Monster Name')
family_column.subheader('Family Type')

for monster in monster_data:
    name_column.write(monster['old_name'])  # make this text hyperlinkable to detail page
    family_column.write(monster['family']['family_eng'])

