import streamlit as st
from helper_functions import get_monster, get_breeding_results, APINames

# TODO refactor to make it readable

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

st.image(f"{APINames.API_GET_MONSTER_IMAGE}{monster_data['old_name']}.png")

# Monster Info
st.write("##### Basic Info")
st.write(f"Game Name : **{monster_data['old_name']}**")
st.write(f"Updated Name : {monster_data['new_name']}")
st.write(f"Family : {monster_data['family']['family_eng']}")
st.write(f"Description : {monster_data['description']}")
st.write('\n')

st.write("##### Skills")
for skill in monster_data['skills']:
    st.write(
            f"<a target='_blank' href='skill_detail?id={skill['id']}'>"
            f"{skill['old_name']}</a> -- {skill['description']}",
            unsafe_allow_html=True
        )
st.write('\n')

#  Start of Breeding Combo Table
st.write("##### Breeding Combinations")
pedigree_column, partner_column, result_column = st.columns(3)
pedigree_column.markdown("##### Pedigree")
partner_column.markdown("##### Partner")
result_column.markdown("##### Resulting Child")

for combo_entry in breeding_data:
    if combo_entry['pedigree_id']:
        idx = combo_entry['pedigree']['id']
        name = combo_entry['pedigree']['old_name']
        if idx == monster_data['id']:
            pedigree_column.write(name)
        else:
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
        if idx == monster_data['id']:
            partner_column.write(name)
        else:
            partner_column.write(
                f"<a target='_self' href='monster_detail?id={idx}'>{name}</a>",
                unsafe_allow_html=True
            )
    else:
        partner_column.write(combo_entry['family2']['family_eng'] + " FAMILY")

    if combo_entry['child_id'] == monster_data['id']:
        result_column.write(combo_entry['child']['old_name'])
    else:
        idx = combo_entry['child']['id']
        name = combo_entry['child']['old_name']
        result_column.write(
            f"<a target='_self' href='monster_detail?id={idx}'>{name}</a>",
            unsafe_allow_html=True
        )
