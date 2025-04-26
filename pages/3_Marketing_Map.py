# pages/3_Marketing_Map.py

import streamlit as st
import pandas as pd
import pydeck as pdk
import os

# ---------------- Setup ----------------
st.set_page_config(page_title="🍽️ Consumer Scenes Map", layout="wide")
st.title("🎯 Scene-Based Map of Michelin Restaurants")

# ---------------- Load Data ----------------
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, '..', 'data')

df = pd.read_csv(os.path.join(DATA_PATH, 'merged_michelin_data.csv'))
topics_df = pd.read_csv(os.path.join(DATA_PATH, 'LDA_topics.csv'))
manual_labels_df = pd.read_csv(os.path.join(DATA_PATH, 'manual_scene_labels.csv'))

# ---------------- Section 1: LDA Topics ----------------
st.markdown("## 📚 Step 1: LDA Topics Summary")

def highlight_first_row(row):
    return ['background-color: #f0f0f0; font-weight: bold' if row.name == 0 else '' for _ in row]

st.table(topics_df.style.apply(highlight_first_row, axis=1))

# ---------------- Section 2: Manual Scene Labels ----------------
st.markdown("## 🧾 Step 2: Manual Scene Labeling")

scene_colors_hex = {
    "Business Fine Dining (Elegant, Secure, Executive Atmosphere)": "#c6f0f0",
    "Romantic & Intimate Dining (Calm, Private, Ambience-Focused)": "#ffd6dd",
    "Gourmet Exploration (Curated, Inventive, Detail-Oriented Culinary Experiences)": "#cce6ff",
    "Social Dining with Friends (Lively, Relaxed, Fun)": "#fff4cc"
}

def style_scene(row):
    scene = row.get("consumer_scene", "")
    color = scene_colors_hex.get(scene, "")
    return [f"background-color: {color}" if color else "" for _ in row]

st.table(manual_labels_df.style.apply(style_scene, axis=1))

# ---------------- Section 3: Consumer Scene Map ----------------
st.markdown("## 🗺️ Step 3: Map by Consumer Scene")

# A. Scene simplification for map legend
df["clean_scene"] = df["consumer_scene"].str.extract(r"^(.*?)\s*\(")[0].fillna(df["consumer_scene"])

# B. Color mapping
scene_colors_rgb = {
    "Business Fine Dining": [75, 192, 192],
    "Romantic & Intimate Dining": [255, 99, 132],
    "Gourmet Exploration": [54, 162, 235],
    "Social Dining with Friends": [255, 205, 86]
}

df = df[df["clean_scene"].isin(scene_colors_rgb)].copy()
df["price_display"] = df["price($)"].apply(lambda x: "$100+" if x == 4 else "$50–99")
df["color"] = df["clean_scene"].map(scene_colors_rgb)

# C. Filter UI
with st.expander("🎛️ Filter by Scene", expanded=True):
    selected = st.multiselect("Select Scenes:", list(scene_colors_rgb.keys()), default=list(scene_colors_rgb.keys()))
filtered_df = df[df["clean_scene"].isin(selected)]

st.markdown(f"Showing **{len(filtered_df)}** restaurants.")

# D. Map Layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_df,
    get_position='[lon, lat]',
    get_fill_color='color',
    get_radius=100,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=filtered_df["lat"].mean() if not filtered_df.empty else 40.73,
    longitude=filtered_df["lon"].mean() if not filtered_df.empty else -73.93,
    zoom=11
)

tooltip = {
    "html": """
        <b>{restaurant}</b><br/>
        Price: {price_display}<br/>
        ⭐ Stars: {star}<br/>
        Cuisine: {tag}<br/>
        <i>Scene: {clean_scene}</i>
    """,
    "style": {
        "backgroundColor": "white",
        "color": "black",
        "padding": "10px",
        "fontSize": "12px"
    }
}

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip,
    map_style="mapbox://styles/mapbox/light-v9"
)

st.pydeck_chart(deck)

# Optional: raw data view
with st.expander("🧾 Show Data Table"):
    st.dataframe(filtered_df)