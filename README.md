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
├── Home.py                     # Main homepage (Michelin restaurant-style design using Streamlit)
├── pages/                       # Subpages for website navigation
│   ├── 1_Data_Process.py        # NLP Text Cleaning Walkthrough (Tokenization, Stopword Removal, Stemming)
│   ├── 2_Map.py                 # Michelin Star Map Visualization (stars, locations)
│   └── 3_Marketing_Map.py       # Consumer Scene Map Visualization (based on LDA topic modeling)
├── app/                         # Backend scripts for data processing and modeling
│   ├── init.py              # Package initialization
│   ├── apply_scene_tags.py      # Merge manual consumer scene labels with restaurant data
│   ├── main.py                  # CLI-based menu for running LDA, applying scenes, and visualization
│   ├── nlp_topic_modeling.py    # LDA topic modeling and dominant topic assignment
│   └── stemmer_custom.py        # Custom stemming function for NLP preprocessing
├── data/                        # Data files used for analysis and visualization
│   ├── michelin_full.xlsx       # Original manually collected Michelin restaurant data
│   ├── lda_topic_keywords.csv   # Extracted LDA topic keywords for manual labeling
│   ├── manual_scene_labels.csv  # Manually assigned consumer scene labels
├── image/                       # Visual assets for website
│   └── banner_michelin.png      # Homepage header banner image
├── README.md                    # Project introduction, structure, and usage
└── requirements.txt             # Python package requirements for setting up the environment
```

🔹 **Notes**:
- `Home.py` serves as the main entry point, designed in the style of a Michelin restaurant page.
- `app/` contains backend scripts for text processing, LDA modeling, and merging scene tags.
- `pages/` contains individual interactive pages for website navigation.
- `data/` stores both raw and processed data files used in the project.
- `image/` contains branding assets for the homepage.
---

## 🛠️ How to Run the Data Processing Pipeline

Our project allows you to process the restaurant data step-by-step through a simple and clear workflow.

### 1. Initial Input
- Start with the file:  
  ➔ `data/michelin_full.xlsx`  
  (Includes restaurant name, stars, cuisine, description, price range, and coordinates.)

### 2. LDA Topic Modeling
- Run the pipeline, which will automatically generate:
  - `data/michelin_with_topics.xlsx` → Restaurant data with assigned **dominant topics**.
  - `data/lda_topic_keywords.csv` → Extracted **top keywords** per topic for manual interpretation.

### 3. Manual Scene Labeling
- Open and manually interpret `lda_topic_keywords.csv`.
- Create and save your marketing-style labels in a new file:  
  ➔ `data/manual_scene_labels.csv`  
  (Fill in `consumer_scene` and `theme` columns based on topic keywords.)

### 4. Merging the Final Dataset
- Merge your marketing labels back into the restaurant dataset.
- This will produce:  
  ➔ `data/michelin_with_scene.xlsx`  
  (Fully labeled and ready for website visualization.)

---

## 🚀 How to Operate via CLI Menu

To make running the steps even easier, you can simply run the `main.py` file.  
You will see a menu like this:

```python
def main():
    while True:
        print_menu()
        choice = input("\nEnter your choice (0-3): ").strip()

        if choice == "1":
            nlp_topic_modeling.run_lda_on_descriptions()

        elif choice == "2":
            apply_scene_tags.merge_scene_labels()

        elif choice == "3":
            visualization.create_spatial_map()

        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 3.")
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
