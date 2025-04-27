# app/visualization.py

"""
Visualization module.

When triggered, this module will launch the Streamlit web application (Home.py).
"""

import subprocess
import sys
import os

def create_spatial_map():
    print("Launching Streamlit app...")

    # Get the path to Home.py
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    app_path = os.path.join(project_root, "Home.py")

    # Call streamlit run Home.py
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to launch Streamlit app: {e}")
