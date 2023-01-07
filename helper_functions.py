import requests
import streamlit as st


class APINames:
    # API_BASE = "http://localhost:8000"
    API_BASE = "https://em4lp8.deta.dev"
    API_GET_MONSTER_LIST = API_BASE + "/dqm1/monsters/"
    API_GET_MONSTER = API_BASE + "/dqm1/monstersandskill/"
    API_GET_BREEDING_COMBO = API_BASE + "/dqm1/breeding/"
    API_GET_SKILLS_LIST = API_BASE + "/dqm1/skills/"
    API_GET_SKILL = API_GET_SKILLS_LIST
    API_GET_ITEMS_LIST = API_BASE + "/dqm1/items/"
    API_GET_MONSTER_IMAGE = API_BASE + "/static/images/dqm1monsters/"


def hide_table_index():
    """
    hides row indices when displaying a dataframe with st.table or st.dataframe
    """
    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)


@st.cache
def _get_json_data(endpoint):
    """
    Gets relevant JSON data from given FastAPI endpoint
    """
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()


@st.cache
def get_monster_list() -> list[dict]:
    return _get_json_data(APINames.API_GET_MONSTER_LIST)


@st.cache
def get_monster(monster_id) -> list[dict]:
    return _get_json_data(f"{APINames.API_GET_MONSTER}{monster_id}")


@st.cache
def get_breeding_results(monster_id) -> list[dict]:
    return _get_json_data(f"{APINames.API_GET_BREEDING_COMBO}{monster_id}")


@st.cache
def get_skills_list() -> list[dict]:
    return _get_json_data(APINames.API_GET_SKILLS_LIST)


@st.cache
def get_skill_detail(skill_id) -> dict:
    return _get_json_data(f"{APINames.API_GET_SKILL}{skill_id}")


@st.cache
def get_items_list() -> list[dict]:
    return _get_json_data(APINames.API_GET_ITEMS_LIST)
