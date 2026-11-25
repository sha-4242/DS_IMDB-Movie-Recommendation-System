import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def get_recommendations(user_query, df):
    # 1. Add .copy() to create a fresh, independent DataFrame
    # This stops the warning!
    df = df.drop_duplicates(subset=['Title'], keep='first').copy()
    
    # 2. Use .loc for safer assignment
    df.loc[:, 'clean_plot'] = df['Storyline'].str.lower().replace(r'[^a-z\s]', '', regex=True)
    
    clean_query = user_query.lower()

    # (Rest of your TF-IDF code stays the same...)
    tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    all_text = df['clean_plot'].tolist() + [clean_query]
    tfidf_matrix = tfidf.fit_transform(all_text)
    
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    top_indices = similarity_scores[0].argsort()[-5:][::-1]
    
    return df.iloc[top_indices]