import requests
import json
import streamlit as st


@st.cache
def get_json_data(source) -> json:
    """
    Gets relevant JSON data from FastAPI endpoint
    'source' == endpoint
    """
    response = requests.get(source)
    response.raise_for_status()
    return response.json()


st.markdown("# Dragon Quest Monsters Database")
st.markdown("[About](/About)")
