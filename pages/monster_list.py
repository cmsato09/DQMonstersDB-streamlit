import json
import requests
import streamlit as st

st.markdown("## Monster List")

# dummy data with test files
# with open('json_test_files/read_monsters.json') as json_file:
#     monster_list = json.load(json_file)

# FastAPI connection
API_BASE = "http://localhost:8000"
API_GET_MONSTER_LIST = API_BASE + "/dqm1/monsters/"


@st.cache
def get_json_data(source) -> json:
    """
    Gets relevant JSON data from FastAPI endpoint
    'source' == endpoint
    """
    response = requests.get(source)
    response.raise_for_status()
    return response.json()


monster_list = get_json_data(API_GET_MONSTER_LIST)

name_search = st.text_input("Search by Name")
family_search = st.selectbox("Search by Family",
                             ['SLIME', 'DRAGON', 'BEAST', 'BIRD', 'PLANT',
                              'BUG', 'DEVIL', 'UNDEAD', 'MATERIAL', '???'])

# Set up column table
name_column, family_column = st.columns(2)
name_column.subheader('Monster Name')
family_column.subheader('Family Type')

for monster in monster_list:
    name_column.write(monster['old_name'])  # make this text hyperlinkable to detail page
    family_column.write(monster['family']['family_eng'])
