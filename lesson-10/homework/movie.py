import random as r
import requests

base_url = "https://developer.themoviedb.org/docs/getting-started/"
response = requests.get(base_url)
def random_selection():
    genre = input("Enter the genre of the movie you wanna watch: >>>")
    movie_data = response.json()
    movie_genre = list(movie_data.get("genre","N/A")) 
    for genre in movie_genre:
        if movie_genre==genre:  
            print(movie_genre.get("name","N/A"))
    
random_selection()   
    