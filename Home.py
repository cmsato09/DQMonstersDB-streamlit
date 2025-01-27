import streamlit as st

if __name__ == "__main__":
    st.set_page_config(page_title="DQMDB", layout="centered")
    st.markdown("# Dragon Quest Monsters Database")

    st.image(
        "https://store-jp.nintendo.com/dw/image/v2/BFGJ_PRD/on/demandware.static/-/Sites-all-master-catalog/ja_JP/dwfe080eff/products/D70010000019662/heroBanner/054e861d9bc2a6077e838df18a21446d87ab4d2a815fb864854cafe69be593db.jpg?sw=1368&strip=false",
        caption="Image from Nintendo Switch Japanese E-shop",
    )
    st.write(
        "Dragon Quest Monsters is a spin-off series based on the famous JRPG "
        "series, Dragon Quest."
    )
    st.write(
        "This database informs the user of game details (monsters, breeding "
        "combinations, skills, items, etc.) of Dragon Quest Monsters -- "
        "Terry's Wonderland (also known as Dragon Warrior Monsters in the US)"
        " **for the original GameBoy Color game** (not the new 3DS version)."
    )
    st.write(
        "If accessing this site on a mobile, open the collapsed sidebar by "
        "clicking the arrow on the top left. "
    )

    st.write(
        "Thank you for visiting this website, I hope this database helps you. "
        "I created a new and improved version of this website."
    )

    st.write("CHECK OUT THE NEW WEBSITE AT https://dqmonsters-db.vercel.app")

    st.write("All game images property of Square Enix")
