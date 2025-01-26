from typing import Dict, List

import pandas as pd
import streamlit as st

from helper_functions import (
    APINames,
    get_breeding_results,
    get_monster,
    make_clickable_monster_name,
)


def reformat_breeding_list(json_data: List[Dict], monster_page_id: int) -> pd.DataFrame:
    """
    makes new reformatted dataframe from breeding data for display
    :param json_data: JSON data from API
    :param monster_page_id: monster_id of current page to prevent making a
    hyperlink back to the same page
    :return: reformatted data as a dataframe with three columns
    """

    reformat_list = []
    for combo in json_data:
        entry = {}
        if combo["pedigree_id"]:
            name_x = combo["pedigree"]["old_name"]
            if combo["pedigree_id"] == monster_page_id:
                entry["PEDIGREE"] = name_x
            else:
                temp_id_x = combo["pedigree_id"]
                entry["PEDIGREE"] = make_clickable_monster_name(temp_id_x, name_x)
        else:
            entry["PEDIGREE"] = combo["pedigree_family"]["family_eng"] + " FAMILY"

        if combo["parent2_id"]:
            name_y = combo["parent2"]["old_name"]
            if combo["parent2_id"] == monster_page_id:
                entry["PARTNER"] = name_y
            else:
                temp_id_y = combo["parent2_id"]
                entry["PARTNER"] = make_clickable_monster_name(temp_id_y, name_y)
        else:
            entry["PARTNER"] = combo["family2"]["family_eng"] + " FAMILY"

        if combo["child_id"] == monster_page_id:
            entry["OFFSPRING"] = combo["child"]["old_name"]
        else:
            temp_id_z = combo["child_id"]
            name_z = combo["child"]["old_name"]
            entry["OFFSPRING"] = make_clickable_monster_name(temp_id_z, name_z)

        reformat_list.append(entry)
    return pd.DataFrame(reformat_list)


if __name__ == "__main__":
    params = st.query_params
    if "id" in params:
        monster_id = int(params["id"])
    else:
        monster_id = st.number_input(
            label="Input monster ID", min_value=1, max_value=215
        )

    if monster_id:
        monster_data = get_monster(monster_id)
        breeding_data = get_breeding_results(monster_id)

    st.markdown(f"## Monster Detail ~ {monster_data['old_name']}")
    st.image(f"{APINames.API_GET_MONSTER_IMAGE}{monster_data['old_name']}.png")

    # Monster Info
    st.write("##### Basic Info")
    st.write(f"Game Name : **{monster_data['old_name']}**")
    st.write(f"Updated Name : {monster_data['new_name']}")
    st.write(f"Family : {monster_data['family']['family_eng']}")
    st.write(f"Description : {monster_data['description']}")
    st.write("\n")

    st.write("##### Skills")
    for skill in monster_data["skills"]:
        st.write(
            f"<a target='_self' href='skill_detail?id={skill['id']}'>"
            f"{skill['old_name']}</a> -- {skill['description']}",
            unsafe_allow_html=True,
        )
    st.write("\n")

    #  Start of Breeding Combo Table
    st.write("##### Breeding Combinations")

    # hide_table_index()
    breed_data_df = reformat_breeding_list(breeding_data, monster_id)
    st.write(breed_data_df.to_html(escape=False, index=False), unsafe_allow_html=True)
