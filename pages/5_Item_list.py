import streamlit as st
import pandas as pd
from Home import get_json_data

# FastAPI connection
API_BASE = "http://localhost:8000"
API_GET_ITEMS_LIST = API_BASE + "/dqm1/items/"

# dummy data test
# with open('json_test_files/items_dummy_data.json') as json_file:
#     item_data = pd.read_json(json_file)

st.markdown("## Items Table")
item_data = get_json_data(API_GET_ITEMS_LIST)
st.table(item_data)
# problems --> integers are defaulting to float
# also need to remove id column
