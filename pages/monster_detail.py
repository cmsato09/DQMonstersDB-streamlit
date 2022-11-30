import json
import streamlit as st

st.markdown("# Monster Detail Info Page Example")

with open('json_test_files/monsterandskill_example.json') as json_file:
    monster_data = json.load(json_file)

st.image("https://lh3.googleusercontent.com/cdNCaeyTOJ1ynJkTn9-wpZJIAFHiej1-DGvGHq1us3JTPwZtcII7bbUBr0Fpaqhh8pIXBou2__z-I1yPc85mBS-EYuoTnDNRZHaT3sxU81T6=w200-s0")
st.write(f"Game Name: {monster_data['old_name']}")
st.write(f"Revised Name: {monster_data['new_name']}")
st.write(f"Family: {monster_data['family']['family_eng']}")
st.write(f"Description: {monster_data['description']}")

#  want these texts to hyperlink to skill table
st.write(f"Skills: {monster_data['skills'][0]['old_name']}, "
         f"{monster_data['skills'][1]['old_name']}, "
         f"{monster_data['skills'][2]['old_name']} ")
