# app/main.py

"""
Main entry point for the NYC Michelin Restaurants NLP and Mapping project (Manual Data Version).

This script allows you to:
- Run LDA topic modeling on Michelin restaurant descriptions.
- Save topic keywords for manual labeling.
- Manually assign consumer scenes (by editing a CSV).
- Merge consumer scene labels back to the restaurant-level dataset.
- Visualize spatial patterns by topic and Michelin stars.

Instructions:
- This script does NOT execute all steps automatically.
- Please select a task from the menu to run it explicitly.
"""

import os
from app import nlp_topic_modeling, apply_scene_tags, visualization

def print_menu():
    print("\nSelect a task to perform:")
    print("1. Run LDA Topic Modeling on Descriptions")
    print("2. Apply Manually Labeled Consumer Scene Tags")
    print("3. Visualize Restaurant Distributions on Map")
    print("0. Exit")

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

if __name__ == "__main__":
    main()
