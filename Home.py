import streamlit as st


if __name__ == "__main__":
    st.set_page_config(page_title="DQMDB", layout="centered",
                       initial_sidebar_state="collapsed")
    st.markdown("# Dragon Quest Monsters Database")
    st.write(
        f"<a target='_self' href='/About'> ABOUT </a>",
        unsafe_allow_html=True
    )
    st.write(
        f"<a target='_self' href='/monster_list'> Monster List </a>",
        unsafe_allow_html=True
    )
    st.write(
        f"<a target='_self' href='/skills_list'> Skills List </a>",
        unsafe_allow_html=True
    )
    st.write(
        f"<a target='_self' href='/item_list'> Item List </a>",
        unsafe_allow_html=True
    )
