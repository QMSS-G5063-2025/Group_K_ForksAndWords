# pages/2_Map.py

import streamlit as st
import pandas as pd
import pydeck as pdk
import os

# ---------------------- Setup ----------------------
st.set_page_config(page_title="Michelin Restaurants Map", layout="wide")
st.title("📍 Michelin-Starred Restaurants in NYC")

# ---------------------- Load Data ----------------------
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "michelin_full.xlsx")
df = pd.read_excel(DATA_PATH)

# Price formatting for display
def format_price(p):
    return {1: "Under $25", 2: "$25–49", 3: "$50–99", 4: "$100+"}.get(p, "N/A")

df["price_display"] = df["price($)"].apply(format_price)

# Extract unique cuisines
all_cuisines = sorted({c.strip() for tags in df["tag"].dropna() for c in tags.split(",")})
all_cuisines.insert(0, "ALL")

# ---------------------- Sidebar Filters ----------------------
with st.sidebar:
    st.header("🎛️ Filters")
    stars = st.multiselect("Michelin Stars ⭐", options=[1, 2, 3], default=[1, 2, 3])
    prices = st.multiselect("Price Range 💵", options=[1, 2, 3, 4], default=[3, 4])
    cuisines = st.multiselect("Cuisine 🍽️", options=all_cuisines, default=["ALL"])
    map_style = st.selectbox("Map Style 🗺️", options=[
        "mapbox://styles/mapbox/light-v9",
        "mapbox://styles/mapbox/dark-v9",
        "mapbox://styles/mapbox/outdoors-v11",
        "mapbox://styles/mapbox/streets-v11"
    ], index=0)

# ---------------------- Filtering Logic ----------------------
filtered_df = df.copy()
if stars:
    filtered_df = filtered_df[filtered_df["star"].isin(stars)]
if prices:
    filtered_df = filtered_df[filtered_df["price($)"].isin(prices)]
if "ALL" not in cuisines:
    filtered_df = filtered_df[filtered_df["tag"].apply(
        lambda t: any(c in [x.strip() for x in str(t).split(",")] for c in cuisines)
    )]

# ---------------------- Display Map ----------------------
st.markdown(f"### 📌 {len(filtered_df)} restaurants match your selection.")

if not filtered_df.empty:
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=filtered_df,
        get_position='[lon, lat]',
        get_fill_color='[255, 0, 0, 160]',
        get_radius=100,
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=filtered_df['lat'].mean(),
        longitude=filtered_df['lon'].mean(),
        zoom=11,
        pitch=0,
    )

    tooltip = {
        "html": "<b>{restaurant}</b><br/>💰 {price_display}<br/>⭐ {star} Stars<br/><i>{tag}</i>",
        "style": {"backgroundColor": "white", "color": "black", "fontSize": "12px"}
    }

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip,
        map_style=map_style
    )
    st.pydeck_chart(deck)

else:
    st.warning("😕 No restaurants match your filters. Try adjusting the options.")

# ---------------------- Optional Raw Data ----------------------
with st.expander("🔍 See Filtered Raw Data"):
    st.dataframe(filtered_df)