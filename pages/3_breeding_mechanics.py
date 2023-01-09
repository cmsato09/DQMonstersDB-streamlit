import streamlit as st

st.markdown("## Breeding Mechanics")

st.write(
    "To get better monsters, you can mate them at the Shrine of Starry Night "
    "at the base of the Great Tree. This area is unlocked after you clear "
    "Class F Arena battle. "
)

st.markdown(
    f"#### Conditions \n"
    "- Two parent monsters where one is male and the other is female\n"
    "- Both parent monsters must at least be level 10\n"
    "- Have at least 3 monsters in total\n"
    "The two parent monsters will leave and never return to your party but "
    "will leave behind an egg.\n\n"
    "The resulting offspring primarily depends upon family lineage or pedigree"
    " (the first monster you select), so you must be careful which monster you"
    " set as pedigree or partner (order matters). See breeding combination of "
    "each monster in the monster detail page. "
)

st.markdown(
    "#### + Value \n"
    "After you mate two monsters, you will see the offspring with something "
    "similar to '+1' by its name, which is referred to as the + value or + "
    "level.\n \n"
    "The + value affects status and the level cap of your monster. It is "
    "determined by the total level of the parent monsters noted in the "
    "following table and if the parents themselves have a + value.\n\n "
    "Total Level | + Value \n"
    "----- | --- \n"
    "20-39 | +1 \n"
    "40-59 | +2 \n"
    "60-75 | +3 \n"
    "76-99 | +4 \n"
    "above 100  | +5 \n\n"
    "When two monsters that have a plus value are mated, the higher + value is"
    " added on to the total. \n\n"
    "e.g. if you have two monsters with +10 and +8 with a total level of over "
    "100, the resulting offspring is +15. (10 + 5)"
)

st.markdown(
    "#### Level Cap Limit \n"
    "Monsters that you recruit in the wild has a level cap limit. "
    "By breeding, you can increase the level cap limit of the offspring. "
    "Level cap limit is calculated by the following:\n\n"
    "(Plus value) x 2 + (monsters base level cap)\n\n"
    "e.g. Unicorn’s base level cap is 50 so a Unicorn +6 has a level cap of "
    "62 (6 x 2 + 50). "
)

st.markdown(
    "#### Offspring stats parameter calculation \n"
    "Resulting offspring monster stat (Attack, Defense, Agility, Intelligence)"
    " is determined by the following equation.\n\n"
    "( pedigree parent monster stat + partner parent monster stat ) ÷ 4 + "
    "(offspring plus value)\n\n"
    "e.g. pedigree parent attack = 300 and partner parent attack = 500 with "
    "the offspring +1 would have a attack value of 201 [(300+500) ÷ 4 + 1]."
)

st.markdown(
    "#### Skill Inheritance \n"
    "A monster recruited in the wild usually only have the 3 skills listed in"
    " the monster detail page. However, a offspring can learn up to 8 "
    "different skills. \n\n"
    "The offspring monster can learn the 3 skills naturally learned by each "
    "parent monster, the 3 skills the offspring monster naturally learns, and "
    "any other skills the parent monsters do not naturally learn and was "
    "inherited from their parents at the time of mating.\n\n"
    "Any monster learning over 8 skills will have to 'forget' a skill to make "
    "room for any new skills."
)
