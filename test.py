import pandas as pd
import numpy as np
import re
from sentence_transformers import SentenceTransformer
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore', category=FutureWarning)

def clean_ticket_text(text: str) -> str:
    """
    Cleans raw ticket text by removing boilerplate, HTML tags, and extra whitespace.
    This is a crucial step to ensure the embedding model focuses on the core issue.
    """
    if not isinstance(text, str):
        return ""

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # Remove email headers and boilerplate text (case-insensitive)
    patterns_to_remove = [
        r'From:.*', r'Sent:.*', r'To:.*', r'Subject:.*',
        r'CAUTION:.*', r'This email and any attachments.*'
    ]
    for pattern in patterns_to_remove:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def find_optimal_clusters(embeddings, max_k=20):
    """
    Analyzes embeddings to find the optimal number of clusters using the Elbow Method.
    """
    print("\n🔎 Finding optimal number of clusters using the Elbow Method...")
    sse = []
    k_range = range(2, max_k + 1)
    
    for k in k_range:
        kmeans = MiniBatchKMeans(n_clusters=k, random_state=42, n_init='auto', batch_size=256)
        kmeans.fit(embeddings)
        sse.append(kmeans.inertia_)
        print(f"  Computed SSE for k={k}")

    # Plotting the Elbow Method graph
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, sse, 'bo-')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Sum of Squared Errors (SSE)')
    plt.title('Elbow Method For Optimal k')
    plt.xticks(k_range)
    plt.grid(True)
    plt.savefig('elbow_plot.png')
    print("\n✅ Elbow method plot saved as 'elbow_plot.png'. Please review it to choose the best 'k'.")
    # You can visually inspect the plot to find the "elbow" point.
    # For this POC, we will proceed with a pre-selected value.
    
def run_ticket_analysis_poc():
    """
    Main function to execute the end-to-end ticket analysis pipeline.
    """
    print("🚀 Starting Ticket Analysis POC...")
    
    # --- 1. Load Data ---
    try:
        # Limit to the first 200 tickets for the POC as requested
        df = pd.read_excel("ServiceNow_Tickets.xlsx").head(200)
        print(f"✅ Successfully loaded {len(df)} tickets from Excel.")
    except FileNotFoundError:
        print("❌ ERROR: 'ServiceNow_Tickets.xlsx' not found. Please place the file in the same directory.")
        return

    # --- 2. Text Preparation ---
    # Based on the images, we map columns: description -> short_description, work_notes -> close_notes
    print("\n🧹 Cleaning and preparing text data...")
    df['combined_text'] = df['short_description'].fillna('') + ' ' + df['close_notes'].fillna('')
    df['cleaned_text'] = df['combined_text'].apply(clean_ticket_text)
    
    # Filter out any rows that might be empty after cleaning
    df = df[df['cleaned_text'] != '']
    print(f"Text preparation complete. {len(df)} tickets remain for analysis.")

    # --- 3. Embedding Generation ---
    print("\n🧠 Generating embeddings with 'paraphrase-distilroberta-base-v1'...")
    model = SentenceTransformer('paraphrase-distilroberta-base-v1')
    embeddings = model.encode(df['cleaned_text'].tolist(), show_progress_bar=True)

    # --- 4. Find Optimal k & Perform Clustering ---
    # This step generates the elbow_plot.png for you to analyze
    find_optimal_clusters(embeddings, max_k=15)
    
    # Based on analyzing a typical elbow plot, we'll choose a k value.
    # CHANGE THIS VALUE after inspecting your 'elbow_plot.png'
    optimal_k = 8 
    print(f"\nProceeding with k={optimal_k} for final clustering.")
    
    kmeans = MiniBatchKMeans(n_clusters=optimal_k, random_state=42, n_init='auto')
    df['cluster'] = kmeans.fit_predict(embeddings)
    
    # --- 5. Display Results ---
    print("\n--- Top 3 Tickets from Each Discovered Cluster ---")
    for i in range(optimal_k):
        cluster_df = df[df['cluster'] == i]
        if not cluster_df.empty:
            print(f"\n🔷 Cluster {i+1} ({len(cluster_df)} tickets):")
            # Display the 'short_description' for readability
            for _, row in cluster_df.head(3).iterrows():
                print(f"  - Ticket {row['number']}: {row['short_description']}")

if __name__ == '__main__':
    try:
        run_ticket_analysis_poc()
    except ImportError:
        print("\n❌ ERROR: Missing one or more required libraries.")
        print("Please install them by running: pip install pandas openpyxl scikit-learn sentence-transformers matplotlib")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
