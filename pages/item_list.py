import streamlit as st
import pandas as pd

st.markdown("## Items Table")

with open('json_test_files/items_dummy_data.json') as json_file:
    item_data = pd.read_json(json_file)


st.table(item_data)
# problems --> integers are defaulting to float
# also need to remove id column
