# app/stemmer_custom.py

"""
Custom stemming module for Michelin restaurant description NLP analysis.
- Uses NLTK's PorterStemmer.
- Simple function to stem a list of tokens.
- Designed for consistent token cleaning before TF-IDF/LDA modeling.
"""

import nltk
from nltk.stem import PorterStemmer

# Initialize stemmer
stemmer = PorterStemmer()

# Function to stem tokens
def stem_tokens(tokens):
    """
    Stem a list of tokens.

    Args:
        tokens (list): List of word tokens (strings).

    Returns:
        list: List of stemmed tokens.
    """
    return [stemmer.stem(token) for token in tokens]

# If running directly (testing)
if __name__ == "__main__":
    sample_tokens = ["cooking", "cooked", "dishes", "restaurants"]
    print("Original:", sample_tokens)
    print("Stemmed:", stem_tokens(sample_tokens))
