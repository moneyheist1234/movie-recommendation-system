# Movie-Recommendation-System

This is a simple movie recommendation system built using Flask, Pandas, and scikit-learn. It uses a dataset of movies to recommend similar movies based on features like keywords, cast, genres, and director.

## Requirements

- Python 3.x
- Flask
- Pandas
- scikit-learn

- pip install Flask pandas scikit-learn


#Download the movies dataset:
Make sure you have a CSV file named movies.csv in the project directory. The CSV file should have the following columns:

index
title
keywords
cast
genres
director

#run this
python app.py
and open this link
http://127.0.0.1:5000/

#Project Structure
app.py: The main Flask application file.
templates/index.html: The HTML template for the web interface.
movies.csv: The dataset containing movie information.

#Usage
Home Page:

You will see an input field where you can enter the name of a movie you like.
#Get Recommendations:

After entering the movie name, submit the form to get a list of similar movies.
How It Works

#Data Loading:

The application loads the movies dataset from movies.csv.

#Feature Combination:

Selected features (keywords, cast, genres, director) are combined into a single string for each movie.
Count Matrix:

A count matrix is created from the combined feature strings using CountVectorizer.
Cosine Similarity:

Cosine similarity is calculated based on the count matrix to find similar movies.

#Recommendations:

#The application finds movies with the highest cosine similarity scores and displays them as recommendations.

#Example
If you enter the movie name "Avatar" and submit the form, you will get a list of movies similar to "Avatar" based on the combined features.

#Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

#License
This project is licensed under the MIT License.
