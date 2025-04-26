# app/nlp_topic_modeling.py

"""
NLP Topic Modeling for Michelin Restaurant Descriptions
- Tokenization with custom stopwords
- Stemming with custom stemmer
- TF-IDF vectorization
- LDA topic modeling
- Assign dominant topic back to each restaurant
"""

import os
import pandas as pd
import numpy as np
import re
import nltk
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from app.stemmer_custom import stem_tokens

def run_lda_on_descriptions():
    nltk.download('punkt')
    nltk.download('punkt_tab')

    # Paths
    RAW_DATA_PATH = os.path.join("data", "michelin_full.xlsx")
    STOPWORDS_PATH = os.path.join("data", "stopwords_custom.txt")
    os.makedirs("data", exist_ok=True)

    # Load data
    df = pd.read_excel(RAW_DATA_PATH)

    # Load custom stopwords
    with open(STOPWORDS_PATH, "r") as f:
        stopwords_custom = set(word.strip() for word in f.readlines())

    # Tokenizer function
    def custom_tokenizer(text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        tokens = nltk.word_tokenize(text)
        tokens = [t for t in tokens if t not in stopwords_custom and len(t) > 2]
        tokens = stem_tokens(tokens)
        return tokens

    # Tokenize descriptions
    print("Tokenizing and stemming descriptions...")
    df["tokens"] = df["description"].apply(custom_tokenizer)

    # Join tokens back to text for TF-IDF
    texts_for_tfidf = df["tokens"].apply(lambda x: " ".join(x))

    # TF-IDF Vectorization
    print("Vectorizing with TF-IDF...")
    tfidf_vectorizer = TfidfVectorizer()
    X = tfidf_vectorizer.fit_transform(texts_for_tfidf)

    # LDA Modeling
    NUM_TOPICS = 8
    print(f"Training LDA model with {NUM_TOPICS} topics...")
    lda = LatentDirichletAllocation(n_components=NUM_TOPICS, random_state=42)
    lda.fit(X)

    # Show topics
    def display_topics(model, feature_names, no_top_words):
        for topic_idx, topic in enumerate(model.components_):
            message = f"Topic {topic_idx}: "
            message += " ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]])
            print(message)

    print("\nTop words per topic:")
    display_topics(lda, tfidf_vectorizer.get_feature_names_out(), 10)

    # Assign dominant topic back to each restaurant
    print("Assigning dominant topic to each description...")
    X_topics = lda.transform(X)
    df["dominant_topic"] = np.argmax(X_topics, axis=1)

    # Save processed file
    output_path = os.path.join("data", "michelin_with_topics.xlsx")
    df.to_excel(output_path, index=False)
    print(f"Saved processed data with topics to {output_path}")

    # Save topics to CSV for manual labeling
    topics_out_path = os.path.join("data", "lda_topic_keywords.csv")
    topic_keywords = []
    for topic_idx, topic in enumerate(lda.components_):
        top_words = [tfidf_vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-11:-1]]
        topic_keywords.append({
            "topic_id": topic_idx,
            "top_words": ", ".join(top_words),
            "consumer_type": topic_idx,
            "consumer_scene": ""
        })

    pd.DataFrame(topic_keywords).to_csv(topics_out_path, index=False)
    print(f"Saved topic keywords to {topics_out_path}")
