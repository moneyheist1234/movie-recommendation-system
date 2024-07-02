from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

app = Flask(__name__)

# Load the data
movies_data = pd.read_csv('movies.csv')

# Function to combine features for the movie
def combine_features(row):
    try:
        return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
    except:
        print("Error:", row)

# Fill all NaNs with empty string
for feature in ['keywords', 'cast', 'genres', 'director']:
    movies_data[feature] = movies_data[feature].fillna('')

# Create a column in the DataFrame that combines all selected features
movies_data["combined_features"] = movies_data.apply(combine_features, axis=1)

# Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(movies_data["combined_features"])

# Compute the cosine similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)

# Function to get title from index
def get_title_from_index(index):
    return movies_data[movies_data.index == index]["title"].values[0]

# Function to get index from title
def get_index_from_title(title):
    # Find the closest match for the title
    closest_match = difflib.get_close_matches(title, movies_data['title'], n=1)
    if closest_match:
        return movies_data[movies_data.title == closest_match[0]]['index'].values[0]
    else:
        return None

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    movie_user_likes = request.form['movie_name']
    movie_index = get_index_from_title(movie_user_likes)
    if movie_index is not None:
        similar_movies = list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

        recommendations = []
        i = 1
        for movie in sorted_similar_movies:
            index = movie[0]
            title_from_index = get_title_from_index(index)
            if i < 10:
                recommendations.append(title_from_index)
                i += 1

        return render_template('index.html', movie_user_likes=movie_user_likes, recommendations=recommendations)
    else:
        return render_template('index.html', movie_user_likes=movie_user_likes, recommendations=[])

if __name__ == '__main__':
    app.run(debug=True)
