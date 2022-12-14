import streamlit as st
from helper_functions import get_monster, get_breeding_results

st.markdown("## Monster Detail Info Page Example")

params = st.experimental_get_query_params()
if "id" in params:
    monster_id = params["id"][0]
else:
    monster_id = st.number_input(
        label="Input monster ID",
        min_value=1, max_value=215
    )

if monster_id:
    monster_data = get_monster(monster_id)
    breeding_data = get_breeding_results(monster_id)

# dummy test data
# with open('json_test_files/monsterandskill_example.json') as json_file:
#     monster_data = json.load(json_file)

st.image("https://lh3.googleusercontent.com/cdNCaeyTOJ1ynJkTn9-wpZJIAFHiej1-DGvGHq1us3JTPwZtcII7bbUBr0Fpaqhh8pIXBou2__z-I1yPc85mBS-EYuoTnDNRZHaT3sxU81T6=w200-s0")
st.caption("Image is a placeholder")

# Monster Info
st.write(f"Game Name: {monster_data['old_name']}")
st.write(f"Updated Name: {monster_data['new_name']}")
st.write(f"Family: {monster_data['family']['family_eng']}")
st.write(f"Description: {monster_data['description']}")

#  want these texts to hyperlink to skill table
st.write(f"Skills: {monster_data['skills'][0]['old_name']}, "
         f"{monster_data['skills'][1]['old_name']}, "
         f"{monster_data['skills'][2]['old_name']} ")

#  Start of Breeding Combo Table
pedigree_column, partner_column = st.columns(2)
pedigree_column.markdown("##### Pedigree")
partner_column.markdown("##### Partner")

for combo_entry in breeding_data:
    if combo_entry['pedigree_id']:
        idx = combo_entry['pedigree']['id']
        name = combo_entry['pedigree']['old_name']
        pedigree_column.write(
            f"<a target='_self' href='monster_detail?id={idx}'>{name}</a>",
            unsafe_allow_html=True
        )
    else:
        pedigree_column.write(
            combo_entry['pedigree_family']['family_eng'] + " FAMILY"
        )

    if combo_entry['parent2_id']:
        idx = combo_entry['parent2']['id']
        name = combo_entry['parent2']['old_name']
        partner_column.write(
            f"<a target='_self' href='monster_detail?id={idx}'>{name}</a>",
            unsafe_allow_html=True
        )
    else:
        partner_column.write(combo_entry['family2']['family_eng'] + " FAMILY")
