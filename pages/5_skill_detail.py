import streamlit as st
from helper_functions import get_skill_detail

# TODO - refactor to make it more readable. make functions to chunk lines

st.markdown('## Skill Detail Info Page Example')

params = st.experimental_get_query_params()
if "id" in params:
    skill_id = params["id"][0]
else:
    skill_id = st.number_input(
        label="Input skill ID",
        min_value=1, max_value=154
    )

if skill_id:
    skill_data = get_skill_detail(skill_id)

row_header, row_value = st.columns(2, gap="small")

with row_header:
    st.write("Game Name :")
    st.write("Updated Name :")
    st.write("Category type :")
    st.write("Family type :")
    st.write("Description :")
    st.write("MP Cost: ")

with row_value:
    st.write(f"**{skill_data['old_name']}**")
    st.write(f"*{skill_data['new_name']}*")
    st.write(f"{skill_data['category_type']}")
    st.write(f"{skill_data['family_type']}")
    st.write(f"{skill_data['description']}")
    st.write(f"{skill_data['mp_cost']}")

if skill_data['upgrade_from']:
    idx = skill_data['upgrade_from']['id']
    upgrade_from_name = skill_data['upgrade_from']['old_name']

    row_header.write("Upgrades from :")
    row_value.write(
        f"<a target='_self' href='skill_detail?id={idx}'>"
        f"{upgrade_from_name}</a>",
        unsafe_allow_html=True
    )

if skill_data['upgrade_to']:
    idy = skill_data['upgrade_to']['id']
    upgrade_to_name = skill_data['upgrade_to']['old_name']
    row_header.write("Upgrades to :")
    row_value.write(
        f"<a target='_self' href='skill_detail?id={idy}'>"
        f"{upgrade_to_name}</a>",
        unsafe_allow_html=True
    )

st.write("Required stats to learn")

lvl, hp, mp, attk, defense, spd, intel = st.columns(7, gap="small")
with lvl:
    st.write("Level")
    st.write(f"{skill_data['required_level']}")
with hp:
    st.write("HP")
    st.write(f"{skill_data['required_hp']}")
with mp:
    st.write("MP")
    st.write(f"{skill_data['required_mp']}")
with attk:
    st.write("ATK")
    st.write(f"{skill_data['required_attack']}")
with defense:
    st.write("DEF")
    st.write(f"{skill_data['required_defense']}")
with spd:
    st.write("AGL")
    st.write(f"{skill_data['required_hp']}")
with intel:
    st.write("INT")
    st.write(f"{skill_data['required_intelligence']}")
