import streamlit as st


if __name__ == "__main__":
    st.set_page_config(page_title="DQMDB", layout="centered",
                       initial_sidebar_state="collapsed")
    st.markdown("# Dragon Quest Monsters Database")
    st.markdown("[About](/About)")
    st.write(
        f"<a target='_self' href='/About'> ABOUT </a>",
        unsafe_allow_html=True
    )
