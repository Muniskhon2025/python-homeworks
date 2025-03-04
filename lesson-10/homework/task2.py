import requests
import random


BASE_URL = "https://api.themoviedb.org/3"

# Step 1: Fetch available genres
genre_url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
genre_response = requests.get(genre_url).json()

if "genres" in genre_response:
    genres = {genre["name"].lower(): genre["id"] for genre in genre_response["genres"]}
else:
    print("Error fetching genres.")
    exit()

# Step 2: Ask user for a genre
user_genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip().lower()

if user_genre not in genres:
    print("Sorry, that genre is not available.")
    exit()

genre_id = genres[user_genre]

# Step 3: Fetch movies from the selected genre
movie_url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
movie_response = requests.get(movie_url).json()

if "results" in movie_response and movie_response["results"]:
    random_movie = random.choice(movie_response["results"])
    print(f"\nRecommended Movie: {random_movie['title']}")
    print(f"Overview: {random_movie['overview']}")
    print(f"Release Date: {random_movie['release_date']}")
else:
    print("No movies found for this genre.")
