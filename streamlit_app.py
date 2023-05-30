import pickle
import requests
import pandas as pd
import gdown
import streamlit as st 


movies_file_id = "1ZiyIPOnAsCnCbwi3ltvBorsXgg8MpYZF"
similarity_file_id = "1ICnGsc5mx6ArS09O9sxJrLEhEaIf5jtk"
movies_download_url = f"https://drive.google.com/uc?export=download&id={movies_file_id}"
similarity_download_url = f"https://drive.google.com/uc?export=download&id={similarity_file_id}"


def download_file(url, output_path):
    gdown.download(url, output_path, quiet=False)


@st.cache_data     
def load_pickle_files(url, filename):
    download_file(url, filename)
    data = pd.read_pickle(filename)
    return data

movies = load_pickle_files(movies_download_url, "movies.pkl")
similarity = load_pickle_files(similarity_download_url, "similarity.pkl")

st.header("Movies recommendation")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}/images".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTZjNDUxMTI1MGRhY2MzOTRjYjNhODQ5ZGJkMDY0ZSIsInN1YiI6IjY0NzQ0YTNiZGQ3MzFiMmQ3YjY2MjYxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NnBTCHh77ikr4QlraGKnfTXqnuX_IIt3sAPd_85i1lM"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    poster_path = data['backdrops'][0]['file_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
