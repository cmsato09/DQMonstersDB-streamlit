import streamlit as st
import pandas as pd
from helper_functions import APINames, get_items_list

# dummy data test
# with open('json_test_files/items_dummy_data.json') as json_file:
#     item_data = pd.read_json(json_file)

st.markdown("## Items Table")
item_data = get_items_list()
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
