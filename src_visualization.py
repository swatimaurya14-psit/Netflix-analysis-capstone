# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_genre_count(df):
    """
    Plot the count of each genre in the dataset
    """
    genre_counts = df['listed_in'].str.split(',').explode().str.strip().value_counts()
    sns.barplot(x=genre_counts.values, y=genre_counts.index)
    plt.xlabel("Count")
    plt.ylabel("Genre")
    plt.title("Count of Movies/Shows by Genre")
