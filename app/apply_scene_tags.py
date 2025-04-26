# app/apply_scene_tags.py

"""
Merge manually labeled consumer scene tags with restaurant-level topic assignments.
This script reads the LDA topic file with human-labeled consumer scene metadata,
and merges the labels back into the Michelin dataset.
"""

import os
import pandas as pd

def merge_scene_labels():
    # Paths
    PROCESSED_DIR = os.path.join("data", "processed")
    topics_path = os.path.join(PROCESSED_DIR, "lda_topic_keywords.csv")
    michelin_path = os.path.join(PROCESSED_DIR, "michelin_with_topics.xlsx")
    output_path = os.path.join(PROCESSED_DIR, "michelin_with_scene.xlsx")

    # Load manually labeled topic info
    topics_df = pd.read_csv(topics_path)

    # Check required columns
    if "consumer_type" not in topics_df.columns or "consumer_scene" not in topics_df.columns:
        raise ValueError("Missing 'consumer_type' or 'consumer_scene' column in lda_topic_keywords.csv.")

    # Fill missing consumer_type with topic_id as default
    topics_df["consumer_type"] = topics_df["consumer_type"].fillna(topics_df["topic_id"])

    # Load restaurant-level topic assignments
    michelin_df = pd.read_excel(michelin_path)

    # Merge scene labels
    merged_df = michelin_df.merge(
        topics_df[["topic_id", "consumer_type", "consumer_scene"]],
        left_on="dominant_topic",
        right_on="topic_id",
        how="left"
    )

    # Drop redundant topic_id after merge
    merged_df.drop(columns=["topic_id"], inplace=True)

    # Save final output
    merged_df.to_excel(output_path, index=False)
    print(f"Updated file saved to {output_path}")

if __name__ == "__main__":
    merge_scene_labels()