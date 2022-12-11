import streamlit as st
import pandas as pd
from helper_functions import get_items_list

# dummy data test
# with open('json_test_files/items_dummy_data.json') as json_file:
#     item_data = pd.read_json(json_file)

if __name__ == "__main__":
    item_data = get_items_list()
    df = pd.DataFrame(item_data)

    st.markdown("## Items Table")
    category_search = st.multiselect(label="Search by category",
                                     options=df["item_category"].unique(),)
    shop_search = st.multiselect(label="Search by category",
                                 options=df["sell_location"].unique(),)

    if category_search and shop_search:
        df = df.query(
            "item_category == @category_search & sell_location == @shop_search"
        )
    elif category_search:
        df = df.query("item_category == @category_search")
    elif shop_search:
        df = df.query("sell_location == @shop_search")

    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    df.rename(
        columns={
            'item_name': 'ITEM', 'item_category': 'CATEGORY',
            'item_description': 'DESCRIPTION', 'price': 'PRICE',
            'sell_price': 'SELL PRICE', 'sell_location': 'SHOP'},
        inplace=True)

    # df = df.fillna(0)
    df['PRICE'] = df['PRICE'].astype('Int64')
    df['SELL PRICE'] = df['SELL PRICE'].astype('Int64')

    item_selection = df[['ITEM', 'CATEGORY', 'DESCRIPTION', 'PRICE',
                         'SELL PRICE', 'SHOP']]
    st.table(item_selection)
