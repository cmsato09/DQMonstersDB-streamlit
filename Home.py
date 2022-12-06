import requests
import json
import streamlit as st


@st.cache
def get_json_data(endpoint):
    """
    Gets relevant JSON data from FastAPI endpoint
    """
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()


@st.cache
def _monster_list(endpoint: str) -> list[dict]:
    return get_json_data(endpoint)


if __name__ == "__main__":
    st.set_page_config(page_title="DQMDB", layout="centered",
                       initial_sidebar_state="collapsed")
    st.markdown("# Dragon Quest Monsters Database")
    st.markdown("[About](/About)")

