import streamlit as st
import pandas as pd
from helper_functions import APINames, get_items_list

# dummy data test
# with open('json_test_files/items_dummy_data.json') as json_file:
#     item_data = pd.read_json(json_file)

if __name__ == "__main__":
    st.markdown("## Items Table")
    category_search = st.selectbox("Search by category",
                                   ['recovery', 'meat', 'dungeon use', 'staff',
                                    'book', 'seed'])
    shop_search = st.selectbox("Search by shop",
                               ['Bazaar shop 1', 'Bazaar shop 2',
                                'Bazaar shop 3', 'Bazaar shop 4', 'Field shop',
                                'found in field'])
    item_data = get_items_list()

    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

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
