# src/recommender.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentRecommender:
    def __init__(self, df):
        """
        df: Pandas DataFrame containing Netflix data with 'title' and 'listed_in' columns
        """
        self.df = df
        self.tfidf = TfidfVectorizer(stop_words='english')
        # 'listed_in' column is genres/categories
        self.tfidf_matrix = self.tfidf.fit_transform(df['listed_in'].fillna(''))

    def recommend(self, title, n=5):
        """
        Recommend n similar titles based on genres
        """
        if title not in self.df['title'].values:
            return ["Title not found in dataset"]
        
        idx = self.df[self.df['title'] == title].index[0]
        cosine_sim = cosine_similarity(self.tfidf_matrix[idx], self.tfidf_matrix).flatten()
        similar_indices = cosine_sim.argsort()[-n-1:-1][::-1]  # exclude itself
        return self.df['title'].iloc[similar_indices].tolist()
