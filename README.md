# ForksAndWords 🍴  
> *Turning Michelin-starred narratives into data-driven delicacies.*

---

## 📍 Project Overview

**ForksAndWords** is the flagship project of **Group K** at **Columbia University's GSAS (QMSS Program)**, developed as the final showcase for **G5063 Data Visualization** under the mentorship of **Professor Thomas Brambor**.

Much like a Michelin-starred kitchen transforms humble ingredients into haute cuisine,  
**ForksAndWords** elevates unstructured text into a layered, revealing feast through lightly processed NLP and data storytelling.

At its core, this project reimagines Michelin restaurant descriptions through:
- Tokenization & text cleaning
- Topic modeling (LDA) to uncover hidden themes
- Consumer scene tagging
- Geospatial visualization of restaurants across New York City

The result?  
A **playfully academic**, **delightfully messy**, yet **strangely addictive** journey across the culinary and textual landscapes of New York.

---

## 🥂 Key Dishes (Project Structure)

| Step | Description |
|:----|:------------|
| 1 | **Handpicked Ingredients:** Manually collected Michelin-starred restaurant info (name, stars, cuisine, description, price, coordinates). |
| 2 | **Artisan Preparation:** Cleaning, tokenization, stemming of descriptions using customized NLP pipelines. |
| 3 | **Hidden Flavors Revealed:** Applying LDA topic modeling to surface latent themes. |
| 4 | **Signature Pairings:** Assigning the most dominant topic to each restaurant, labeling consumer scenes. |
| 5 | **Cartographic Plating:** Visualizing the distribution of restaurants by star level, topic, and scene on interactive maps. |

---

## 🧰 Tech Stack

- **Python**
  - `Streamlit` for web app development
  - `NLTK` for tokenization and text preprocessing
  - `Scikit-learn` for TF-IDF vectorization and LDA modeling
  - `Pandas`, `Numpy` for data handling
  - `Pydeck` for geospatial visualization
- **GitHub** for collaboration and version control

---

## 🌎 Project Layout
```
ForksAndWords/
├── app.py                     # Main homepage (Michelin restaurant-style design)
├── pages/
│   ├── 1_Data_Process.py       # NLP Text Cleaning Walkthrough
│   ├── 2_Map.py                # Michelin Star Map Visualization
│   └── 3_Marketing_Map.py      # Consumer Scene Map Visualization
├── data/
│   ├── michelin_full.xlsx      # Original collected data
│   ├── lda_topic_keywords.csv  # Extracted LDA topics
│   └── manual_scene_labels.csv # Manually assigned consumer scenes
├── image/
│   └── banner_michelin.png     # Homepage banner image
├── README.md                   # Project introduction (this file)
└── requirements.txt            # Python package requirements
```
---

## 👨‍🍳 Chefs de Cuisine

- **Rong Xia**
- **Fung Chau**
- **Chengji Zhang**

Mentored by **Chef Thomas Brambor**  
(Columbia University | G5063 Data Visualization)

---

## 📝 A Note from the Kitchen

*"Not every dish needs to be serious to be unforgettable."*  
ForksAndWords is our greasy paper bag of insights —  
lightly processed, statistically seasoned, and best served **with a wink**. 😉

---

# 📎 [Launch the Website](https://forksandwords-4trbwiyybkvjuhdskenlzs.streamlit.app/)
