import requests
import streamlit as st


class APINames:
    # API_BASE = "http://localhost:8000"
    API_BASE = "https://em4lp8.deta.dev"
    API_GET_MONSTER_LIST = API_BASE + "/dqm1/monsters/"
    API_GET_MONSTER = API_BASE + "/dqm1/monstersandskill/"
    API_GET_BREEDING_COMBO = API_BASE + "/breeding/"
    API_GET_SKILLS_LIST = API_BASE + "/dqm1/skills/"
    API_GET_ITEMS_LIST = API_BASE + "/dqm1/items/"


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
    return _get_json_data(APINames.API_GET_MONSTER + str(int(monster_id)))


@st.cache
def get_breeding_results(monster_id) -> list[dict]:
    return _get_json_data(
        APINames.API_GET_BREEDING_COMBO + str(int(monster_id))
    )


@st.cache
def get_skills_list() -> list[dict]:
    return _get_json_data(APINames.API_GET_SKILLS_LIST)


@st.cache
def get_items_list() -> list[dict]:
    return _get_json_data(APINames.API_GET_ITEMS_LIST)
