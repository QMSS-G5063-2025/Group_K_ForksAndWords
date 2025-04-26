# pages/1_Data_Process.py

import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Download required NLTK resources
nltk.download("stopwords")

# Set up Streamlit page configuration
st.set_page_config(page_title="🔤 Text Processing Journey", page_icon="📝", layout="wide")

# Sample restaurant review text
text = """
Maguy Le Coze and Eric Ripert’s icon has been entertaining the city’s movers and shakers for close to 30 years and its popularity remains undimmed. Seafood restaurants have no hiding place when it comes to cooking fish or crustaceans and this kitchen always hits its marks—whether that’s lusciously sweet, seared langoustine in a truffled broth or golden-brown fluke with a bouillabaisse enriched with sea urchin. While seafood remains Ripert's passion, his vegetarian tasting menu makes waves with dishes like the Himalayan morel, spring pea and fava bean casserole or the warm artichoke panaché with vegetable risotto and Périgord black truffle vinaigrette. Finish with purple sweet potato baba au whisky cloaked with caramelized pecan whipped cream.
"""

tokens = text.split()
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

# Session state to track processing step
if "step" not in st.session_state:
    st.session_state.step = "raw"

# Top section: Restaurant Simulation Header
st.title("🍽️ Text Processing Journey")
st.caption("ForksAndWords · Michelin Style NLP Pipeline")

st.markdown("""
---
### 📍 Sample Restaurant: **Le Bernardin** | 🗽 New York City | 💵 $$$$ | ⭐ ⭐ ⭐
---
""")

# Navigation buttons for processing steps
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("View Raw Text"):
        st.session_state.step = "raw"
with col2:
    if st.button("Step 1: Tokenization"):
        st.session_state.step = "token"
with col3:
    if st.button("Step 2: Remove Stopwords"):
        st.session_state.step = "stopwords"
with col4:
    if st.button("Step 3: Stemming"):
        st.session_state.step = "stem"
with col5:
    if st.button("Step 4: TF-IDF Conversion"):
        st.session_state.step = "conversion"

# --- Step 0: Raw Text ---
if st.session_state.step == "raw":
    st.markdown("### 📄 Raw Restaurant Description")
    st.markdown(f"""
    <div style="padding: 15px; background-color: #f9f9f9; border-left: 5px solid #ff4b4b; border-radius: 10px; font-size:16px; line-height:1.7;">
        <em>{text.strip()}</em>
    </div>
    """, unsafe_allow_html=True)


# --- Step 1: Tokenization ---
elif st.session_state.step == "token":
    st.markdown("### ✂️ Step 1: Tokenization — Splitting Text into Words")
    styled_tokens = [
        f"<span style='background-color:#89CFF0; padding:5px 10px; border-radius:8px; margin:4px; display:inline-block;'>{tok}</span>"
        for tok in tokens
    ]
    st.markdown(" ".join(styled_tokens), unsafe_allow_html=True)

# --- Step 2: Stopwords Removal ---
elif st.session_state.step == "stopwords":
    st.markdown("### 🚫 Step 2: Removing Common Stopwords")
    styled_tokens = []
    for tok in tokens:
        clean_tok = tok.lower().strip(".,!?")
        if clean_tok in stop_words:
            styled_tokens.append(f"<span style='color:#e07b39; text-decoration:line-through; margin:4px;'>{tok}</span>")
        else:
            styled_tokens.append(f"<span style='background-color:#89CFF0; color:black; padding:5px 10px; border-radius:8px; margin:4px; display:inline-block;'>{tok}</span>")
    st.markdown(" ".join(styled_tokens), unsafe_allow_html=True)

# --- Step 3: Stemming (Keep Stopwords visible) ---
elif st.session_state.step == "stem":
    st.markdown("### 🌱 Step 3: Stemming — Reducing Words to Their Base Form")
    styled_tokens = []
    for tok in tokens:
        base = tok.strip(".,!?")
        clean = base.lower()
        if clean in stop_words:
            styled_tokens.append(f"<span style='color:#e07b39; text-decoration:line-through; margin:4px;'>{tok}</span>")
        else:
            stemmed = stemmer.stem(base)
            punct = tok[len(base):] if len(base) < len(tok) else ""
            if stemmed != base:
                styled_tokens.append(
                    f"<span style='background-color:#89CFF0; font-weight:bold; padding:5px 10px; border-radius:8px; margin:4px; display:inline-block;'>"
                    f"<span style='color:white; text-decoration:line-through;'>{base}</span> "
                    f"<span style='color:black;'>{stemmed}{punct}</span></span>"
                )
            else:
                styled_tokens.append(
                    f"<span style='background-color:#89CFF0; color:black; padding:5px 10px; border-radius:8px; margin:4px; display:inline-block;'>{tok}</span>"
                )
    st.markdown(" ".join(styled_tokens), unsafe_allow_html=True)

# --- Step 4: TF-IDF Vectorization Example ---
elif st.session_state.step == "conversion":
    st.markdown("### 🔄 Step 4: Converting Text into TF-IDF Numerical Representation")
    st.markdown("""
    **Goal:** Transform words into numbers for machine learning.  
    We simulate 3 mini documents to explain:
    - **TDM**: Term-Document Matrix
    - **TF**: Term Frequency
    - **IDF**: Inverse Document Frequency
    - **TF-IDF**: Final weighted scores
    """)

    # Mini documents
    doc1 = "taste new york course mix food receiv famili great super"
    doc2 = "taste taste mix mix mix mix food food food food food receiv"
    doc3 = "york course course food famili famili famili great"
    corpus = [doc1, doc2, doc3]

    # --- Term-Document Matrix ---
    st.subheader("📒 A. Term-Document Matrix (TDM)")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    df_tdm = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out(), index=["Doc 1", "Doc 2", "Doc 3"])
    st.dataframe(df_tdm)

    # --- Term Frequency (TF) ---
    st.subheader("📘 B. Term Frequency (TF)")
    st.latex(r'''TF(t, d) = \frac{\text{count}(t,d)}{\text{total terms in }d}''')
    tf_table = df_tdm.div(df_tdm.sum(axis=1), axis=0).round(4)
    st.dataframe(tf_table)

    # --- Inverse Document Frequency (IDF) ---
    st.subheader("📗 C. Inverse Document Frequency (IDF)")
    st.latex(r'''IDF(t) = \log\left(\frac{N}{df(t)}\right)''')
    N = len(df_tdm)
    df_freq = (df_tdm > 0).sum(axis=0)
    idf_values = (N / df_freq).apply(lambda x: round(np.log(x), 4))
    st.dataframe(pd.DataFrame({"IDF": idf_values}))

    # --- TF-IDF (Manual Calculation) ---
    st.subheader("📙 D. TF-IDF Matrix (Manual Calculation)")
    st.latex(r'''TF\text{-}IDF(t, d) = TF(t,d) \times IDF(t)''')
    tfidf_manual = tf_table * idf_values
    st.dataframe(tfidf_manual.round(5))

    # --- TF-IDF (Using Scikit-Learn) ---
    st.subheader("📕 E. TF-IDF Matrix (Scikit-Learn)")
    vectorizer = TfidfVectorizer()
    tfidf_vec = vectorizer.fit_transform(corpus)
    df_tfidf = pd.DataFrame(tfidf_vec.toarray(), columns=vectorizer.get_feature_names_out(), index=["Doc 1", "Doc 2", "Doc 3"])
    st.dataframe(df_tfidf.round(5))