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
df = pd.DataFrame(item_data)

df.rename(
    columns={
        'item_name': 'ITEM', 'item_category': 'CATEGORY',
        'item_description': 'DESCRIPTION', 'price': 'PRICE',
        'sell_price': 'SELL PRICE', 'sell_location': 'SHOP'},
    inplace=True)

df = df.fillna(0)
df['PRICE'] = df['PRICE'].astype(int)
df['SELL PRICE'] = df['SELL PRICE'].astype(int)

item_selection = df[['ITEM', 'CATEGORY', 'DESCRIPTION', 'PRICE',
                     'SELL PRICE', 'SHOP']]
st.table(item_selection)
