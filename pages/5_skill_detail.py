import streamlit as st
from helper_functions import get_skill_detail


if __name__ == "__main__":
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

    st.markdown(f"## Skill Detail Page ~ {skill_data['old_name']} ")

    st.write(f"Game Name :", 8 * "&nbsp;", f"**{skill_data['old_name']}**")
    st.write(f"Updated Name :", 2 * "&nbsp;", f"*{skill_data['new_name']}*")
    st.write(f"Category type :", 4 * "&nbsp;",
             f"{skill_data['category_type']}")
    st.write(f"Family type :", 9 * "&nbsp;", f"{skill_data['family_type']}")
    st.write(f"Description : &nbsp; {skill_data['description']}")
    st.write(f"MP Cost :", 2 * "&nbsp;", f"{skill_data['mp_cost']}")

    if skill_data['upgrade_from']:
        idx = skill_data['upgrade_from']['id']
        upgrade_from_name = skill_data['upgrade_from']['old_name']
        st.write(f"Upgrades from :", 2 * "&nbsp;",
                 f"<a target='_self' href='skill_detail?id={idx}'>",
                 f"{upgrade_from_name}</a>",
                 unsafe_allow_html=True)

    if skill_data['upgrade_to']:
        idy = skill_data['upgrade_to']['id']
        upgrade_to_name = skill_data['upgrade_to']['old_name']
        st.write(f"Upgrades to : ", 7 * "&nbsp;",
                 f"<a target='_self' href='skill_detail?id={idy}'>"
                 f"{upgrade_to_name}</a>",
                 unsafe_allow_html=True)

    st.write("Required stats to learn skill")

    lvl = skill_data['required_level']
    hp = skill_data['required_hp'] \
        if skill_data['required_hp'] is not None else ""
    mp = skill_data['required_mp'] \
        if skill_data['required_mp'] is not None else ""
    atk = skill_data['required_attack'] \
        if skill_data['required_attack'] is not None else ""
    defense = skill_data['required_defense'] \
        if skill_data['required_defense'] is not None else ""
    spd = skill_data['required_speed'] \
        if skill_data['required_speed'] is not None else ""
    intel = skill_data['required_intelligence'] \
        if skill_data['required_intelligence'] is not None else ""

    st.markdown(
        f"Level | HP  | MP | ATK | DEF     | AGL | INT  \n"
        f"------|-----|----|-----|---------|-----|----- \n"
        f"{lvl} |{hp} |{mp}|{atk}|{defense}|{spd}|{intel} "
    )
