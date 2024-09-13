import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Example movie data with genres
movies = pd.DataFrame({
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'genres': ['Action|Adventure', 'Romance|Drama', 'Action|Sci-Fi', 'Drama', 'Adventure|Romance']
})

# Example user ratings for movies (NaN means the user hasn't rated that movie)
ratings = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3],
    'movie_id': [1, 2, 3, 1, 4, 2, 5],
    'rating': [5, 3, 4, 4, 5, 2, 4]
})

# Content-Based Filtering: Recommending movies based on genres

def content_based_recommend(user_id, num_recommendations=2):
    # Merge movies and ratings data
    user_ratings = ratings[ratings['user_id'] == user_id].merge(movies, on='movie_id')
    
    # Create a TF-IDF matrix for genres
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    
    # Get similarity matrix based on cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Get indices of movies rated by the user
    rated_movies_indices = user_ratings['movie_id'].apply(lambda x: movies[movies['movie_id'] == x].index[0])
    
    # Get similarity scores for the movies rated by the user
    sim_scores = cosine_sim[rated_movies_indices].mean(axis=0)
    
    # Sort the movies based on similarity scores
    movie_indices = np.argsort(sim_scores)[::-1]
    
    # Recommend movies that the user hasn't rated yet
    recommendations = []
    for idx in movie_indices:
        movie_id = movies.iloc[idx]['movie_id']
        if movie_id not in user_ratings['movie_id'].values:
            recommendations.append(movies.iloc[idx]['title'])
        if len(recommendations) == num_recommendations:
            break

    return recommendations

# Collaborative Filtering: Recommending movies based on similar users

def collaborative_filtering(user_id, num_recommendations=2):
    # Create a user-item matrix
    user_movie_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating')
    
    # Fill NaN with 0 for cosine similarity calculation
    user_movie_matrix_filled = user_movie_matrix.fillna(0)
    
    # Compute cosine similarity between users
    user_sim = cosine_similarity(user_movie_matrix_filled)
    
    # Get the index of the target user
    user_idx = user_movie_matrix.index.get_loc(user_id)
    
    # Get similarity scores for the target user
    sim_scores = user_sim[user_idx]
    
    # Find the most similar user
    most_similar_user_idx = sim_scores.argsort()[-2]  # -2 because -1 will be the user itself
    similar_user_id = user_movie_matrix.index[most_similar_user_idx]
    
    # Get movies rated by the most similar user but not by the target user
    similar_user_ratings = user_movie_matrix.loc[similar_user_id]
    target_user_ratings = user_movie_matrix.loc[user_id]
    
    # Recommend movies rated highly by the similar user that the target user hasn't rated
    recommendations = similar_user_ratings[similar_user_ratings.notna() & target_user_ratings.isna()].sort_values(ascending=False)
    
    # Return top recommendations
    recommended_movie_ids = recommendations.index[:num_recommendations]
    recommended_movies = movies[movies['movie_id'].isin(recommended_movie_ids)]['title'].tolist()
    
    return recommended_movies

# Example usage:

# Content-based recommendations for User 1
print("Content-Based Recommendations for User 1:", content_based_recommend(1))

# Collaborative filtering recommendations for User 2
print("Collaborative Filtering Recommendations for User 2:", collaborative_filtering(2))
