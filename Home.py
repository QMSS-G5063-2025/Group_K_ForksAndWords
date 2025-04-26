import streamlit as st
import os

# --- Page Config ---
st.set_page_config(page_title="ForksAndWords", page_icon="🎖️", layout="wide")


# --- Hero Banner Image (Top) ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(CURRENT_DIR, "image", "banner_michelin.png")
st.image(IMAGE_PATH, use_container_width=True)

# Add image source line
st.markdown(
    "<div style='text-align: right; font-size: 12px; color: gray;'>"
    "Source: <a href='https://guide.michelin.com/en/new-york-state/new-york/restaurant/le-bernardin' target='_blank'>Michelin Guide - Le Bernardin</a>"
    "</div>",
    unsafe_allow_html=True
)

# --- Title Section ---
st.markdown("""
# ForksAndWords
##### 📍 1555 Broadway Ave, Columbia University, New York, NY 10027, USA  
##### $$$$ · Junk Food
""")

st.markdown("---")

# --- Star Rating Section ---
st.markdown("""
##### 🎖️🎖️🎖️ Three Stars: Exceptional cuisine
""")

# --- Project Description ---
st.markdown("""
**ForksAndWords** is the flagship kitchen of Columbia's data gastronomy.

Conceived amid the vibrant, caffeine-charged nights of **Group K** at **Columbia University GSAS (QMSS Program)**,  
this project delicately reimagines Michelin-starred restaurant descriptions through the lens of natural language processing.

Our tasting menu unfolds in five refined courses:
- **Handpicked Ingredients:** Carefully curated Michelin restaurant descriptions from New York City.
- **Artisan Preparation:** Tokenization, stopword removal, and stemming — a meticulous cleaning of every textual morsel.
- **Hidden Flavors Revealed:** LDA topic modeling to uncover the latent themes within the descriptions.
- **Signature Pairings:** Assigning each restaurant its dominant "topic dish," elegantly labeling consumer scenes.
- **Cartographic Plating:** Visualizing the landscape of stars, themes, and culinary experiences across the map of NYC.

Much like a Michelin kitchen transforms humble produce into haute cuisine,  
**ForksAndWords** elevates modest text into a layered, revealing feast — unexpected, artfully plated, and strangely unforgettable.
""")

st.markdown("---")

# --- Menu Section ---
st.markdown("## Explore Our Dishes")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Tokenization Lab"):
        st.switch_page("pages/1_Data_Process.py")

with col2:
    if st.button("Michelin Star Map"):
        st.switch_page("pages/2_Map.py")

with col3:
    if st.button("Consumer Scene Map"):
        st.switch_page("pages/3_Marketing_Map.py")

with col4:
    st.markdown("[Git Me a Table](https://github.com/QMSS-G5063-2025/Group_K_TBD)", unsafe_allow_html=True)

st.markdown("---")

# --- Team Info (Chefs Section) ---
st.markdown("""
#### 🧑‍🍳 Chefs de Cuisine
- **Rong Xia** · **Fung Chau** · **Chengji Zhang**  
- Group K · QMSS · Columbia University  
- Curated under the mentorship of **Chef Thomas Brambor** (Instructor, 5063 Data Visualization)
""")

st.markdown("---")

# --- Footer ---
st.caption("© 2025 ForksAndWords · Columbia University")

