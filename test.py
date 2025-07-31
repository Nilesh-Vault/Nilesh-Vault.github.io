# -*- coding: utf-8 -*-
"""
Ticket Clustering Script

This script performs an end-to-end analysis of ticket data from an Excel file.
The workflow includes:
1.  Data Loading and Preparation: Reads ticket data from 'task.xlsx', focusing on
    "Description", "Work notes", and "Number" columns. It cleans the text by
    removing HTML, URLs, and extra whitespace.
2.  Text Embedding Generation: Uses a locally stored, pre-trained
    SentenceTransformer model ('paraphrase-distilroberta-base-v1-exp2') to
    convert the cleaned ticket text into meaningful numerical vectors (embeddings).
3.  Cluster Analysis: Employs the Elbow Method to find the optimal number of
    clusters for the tickets. It generates a plot ('elbow_plot.png') to help
    visualize this and prompts the user for input.
4.  Results Generation: Assigns each ticket to a cluster using KMeans, saves the
    results to a new timestamped Excel file, and prints a summary of the
    cluster distribution along with sample tickets from each group.
"""

import os
import re
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# --- Configuration & Constants ---

# File paths - adjust if your file/folder names are different.
# Using a raw string (r'...') is important for Windows paths.
INPUT_FILE = 'task.xlsx'
# Based on your screenshots, the model files are in this directory.
# SentenceTransformers will automatically look for the necessary files inside.
MODEL_PATH = r'C:\Users\kunile\SRE_Tasks\paraphrase-distilroberta-base-v1-exp2'
ELBOW_PLOT_FILE = 'elbow_plot.png'

# Columns required from the input Excel file.
REQUIRED_COLUMNS = ["Description", "Work notes", "Number"]

# Maximum number of clusters to test for the Elbow Method.
MAX_CLUSTERS_TO_TEST = 15

# --- Function Definitions ---

def clean_text(text: str) -> str:
    """
    Cleans a string by removing HTML tags, URLs, and extra whitespace.

    Args:
        text: The input string to clean.

    Returns:
        The cleaned string.
    """
    if not isinstance(text, str):
        return ""
    # Remove HTML tags
    text = re.sub(r'<.*?>', ' ', text)
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    # Remove extra whitespace, newlines, and tabs
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Loads ticket data from an Excel file and prepares it for analysis.

    Args:
        file_path: The path to the input Excel file.

    Returns:
        A pandas DataFrame with cleaned and combined text data.
    """
    print(f"Loading data from '{file_path}'...")
    if not os.path.exists(file_path):
        print(f"--- ERROR: Input file not found at '{file_path}' ---")
        print("Please make sure 'task.xlsx' is in the same directory as the script.")
        exit()

    df = pd.read_excel(file_path)
    print("Data loaded successfully.")

    # Verify that all required columns exist
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            print(f"--- ERROR: Missing required column in Excel file: '{col}' ---")
            print(f"Please ensure the file contains the columns: {', '.join(REQUIRED_COLUMNS)}")
            exit()

    # Combine 'Description' and 'Work notes' into a single text field for analysis.
    # Fill NaN (empty) cells with an empty string to prevent errors.
    df['combined_text'] = df['Description'].fillna('') + ' ' + df['Work notes'].fillna('')

    print("Cleaning text data (removing HTML, URLs, extra whitespace)...")
    df['cleaned_text'] = df['combined_text'].apply(clean_text)

    # Drop rows where the cleaned text is empty, as they cannot be clustered.
    df = df[df['cleaned_text'] != ''].copy()
    return df

def generate_embeddings(texts: list, model_path: str) -> np.ndarray:
    """
    Generates sentence embeddings for a list of texts using a local model.

    Args:
        texts: A list of strings to be encoded.
        model_path: The file path to the local SentenceTransformer model.

    Returns:
        A numpy array of text embeddings.
    """
    print(f"\nLoading SentenceTransformer model from '{model_path}'...")
    if not os.path.exists(model_path):
        print(f"--- ERROR: Model directory not found at '{model_path}' ---")
        print("Please verify the path to the pre-trained model.")
        exit()
        
    try:
        model = SentenceTransformer(model_path)
    except Exception as e:
        print(f"--- ERROR: Failed to load the model. ---")
        print(f"Error details: {e}")
        print("Please ensure the model directory is correct and contains all necessary files (e.g., pytorch_model.bin, config.json).")
        exit()

    print("Model loaded. Generating text embeddings...")
    print("This may take some time depending on the number of tickets and your hardware.")
    
    # Use model.encode with a progress bar (via tqdm)
    embeddings = model.encode(texts, show_progress_bar=True)
    
    print("Embeddings generated successfully.")
    return embeddings

def find_optimal_clusters(embeddings: np.ndarray):
    """
    Calculates and plots the Elbow Method curve to help determine the
    optimal number of clusters.

    Args:
        embeddings: The text embeddings to be clustered.
    """
    print("\nCalculating Elbow Method curve to find optimal number of clusters...")
    inertias = []
    k_range = range(2, MAX_CLUSTERS_TO_TEST + 1)

    for k in tqdm(k_range, desc="Testing cluster counts"):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(embeddings)
        inertias.append(kmeans.inertia_)

    # Plotting the Elbow Curve
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, inertias, 'bo-')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia (Sum of squared distances)')
    plt.title('Elbow Method for Optimal k')
    plt.grid(True)
    plt.xticks(k_range)
    plt.savefig(ELBOW_PLOT_FILE)
    print(f"Elbow plot has been saved as '{ELBOW_PLOT_FILE}'.")
    print("Please view the plot to determine the 'elbow point'.")
    # To automatically open the plot:
    try:
        os.startfile(ELBOW_PLOT_FILE)
    except AttributeError:
        # os.startfile is Windows-only. For macOS/Linux, you might use 'open' or 'xdg-open'.
        print("(On Windows, the plot should open automatically. On other systems, please open the file manually.)")


def main():
    """
    Main function to execute the entire ticket clustering workflow.
    """
    # 1. Data Loading and Preparation
    df = load_and_clean_data(INPUT_FILE)
    if df.empty:
        print("No data to process after cleaning. Exiting.")
        return

    # 2. Text Embedding Generation
    embeddings = generate_embeddings(df['cleaned_text'].tolist(), MODEL_PATH)

    # 3. Cluster Analysis
    find_optimal_clusters(embeddings)

    # Get user input for the number of clusters
    num_clusters = 0
    while True:
        try:
            user_input = input(f"\nEnter the desired number of clusters (e.g., 3, 4, 5...): ")
            num_clusters = int(user_input)
            if num_clusters > 1:
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"Proceeding with {num_clusters} clusters.")

    # 4. Results Generation
    print("\nPerforming final clustering...")
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(embeddings)
    print("Clustering complete.")

    # Display summary
    print("\n--- Cluster Analysis Summary ---")
    print("Number of tickets per cluster:")
    print(df['cluster'].value_counts().sort_index())
    print("\n--- Sample Tickets from Each Cluster ---")

    for i in range(num_clusters):
        print(f"\n--- Cluster {i} Samples ---")
        sample_df = df[df['cluster'] == i].sample(min(3, len(df[df['cluster'] == i])), random_state=42)
        for index, row in sample_df.iterrows():
            print(f"  Ticket Number: {row['Number']}")
            # Print a snippet of the text
            print(f"  Text: {row['cleaned_text'][:200]}...")

    # Save results to a new Excel file with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"clustered_tickets_{timestamp}.xlsx"
    
    # Select columns to save
    output_df = df[['Number', 'Description', 'Work notes', 'cluster']]
    output_df.to_excel(output_filename, index=False)

    print("\n--- Process Complete ---")
    print(f"Results have been saved to '{output_filename}'")


# --- Script Execution ---
if __name__ == "__main__":
    main()
