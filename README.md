# [🍴ForksAndWords](https://forksandwords-4trbwiyybkvjuhdskenlzs.streamlit.app/) 
> *Turning Michelin-starred narratives into data-driven delicacies.*

---

## 📍 Project Overview

**ForksAndWords** is the flagship project of **Group K** at **Columbia University's GSAS (QMSS Program)**, developed as the [final showcase for **G5063 Data Visualization**](https://github.com/QMSS-G5063-2025/course_content/blob/main/Exercises/final_project/proposal/final_project.md) under the mentorship of **Professor Thomas Brambor**.

Much like a Michelin-starred kitchen transforms humble ingredients into haute cuisine,  
**ForksAndWords** elevates unstructured text into a layered, revealing feast through lightly processed NLP and data storytelling.

At its core, this project reimagines Michelin restaurant descriptions through:
- Tokenization & text cleaning
- Topic modeling (LDA) to uncover hidden themes
- Consumer scene tagging
- Geospatial visualization of restaurants across New York City

The result?  
A **playfully academic**, **delightfully messy**, yet **strangely addictive** journey across the culinary and textual landscapes of New York.

<img width="976" alt="image" src="https://github.com/user-attachments/assets/f2708d92-ea89-4944-86fb-a8f306323387" />

---

## 🥂 Key Dishes (Project Structure)

| Step | Description |
|:----|:------------|
| 1 | **Handpicked Ingredients:** Initially attempted to scrape data from Yelp and TripAdvisor, but due to anti-scraping protections, we pivoted to manual collection. Gathered Michelin-starred restaurant information (name, stars, cuisine, description, price range, and coordinates) to ensure clean, copyright-respectful data. |
| 2 | **Artisan Preparation:** Cleaned, tokenized, and stemmed the restaurant descriptions using a customized NLP pipeline to prepare for further modeling. |
| 3 | **Hidden Flavors Revealed:** Applied Latent Dirichlet Allocation (LDA) to uncover underlying thematic structures within the text corpus. |
| 4 | **Signature Pairings:** Assigned each restaurant its most dominant topic, crafting consumer scene labels that describe the thematic dining experience. |
| 5 | **Cartographic Plating:** Mapped the restaurants interactively, visualizing distributions by Michelin stars, dominant topics, and consumer scenes across New York City. |
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
├── Home.py                     # Main homepage (Michelin restaurant-style design)
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
