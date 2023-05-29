# import pickle
# import requests
# import pandas as pd
# import streamlit as st 

# st.header("Movies recommendation")
# movies = pd.read_pickle('artifacts/movie_list.pkl')
# similarity = pd.read_pickle('artifacts/similarity.pkl')

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}/images".format(movie_id)
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTZjNDUxMTI1MGRhY2MzOTRjYjNhODQ5ZGJkMDY0ZSIsInN1YiI6IjY0NzQ0YTNiZGQ3MzFiMmQ3YjY2MjYxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NnBTCHh77ikr4QlraGKnfTXqnuX_IIt3sAPd_85i1lM"
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     poster_path = data['backdrops'][0]['file_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters


# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )

# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
        
        
import pickle
import requests
import pandas as pd
import streamlit as st 

def download_pkl_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as f:
        f.write(response.content)

pkl_file_url1 = "https://drive.google.com/file/d/1ZiyIPOnAsCnCbwi3ltvBorsXgg8MpYZF/view?usp=drive_link"
pkl_file_url2 = "https://drive.google.com/file/d/1ICnGsc5mx6ArS09O9sxJrLEhEaIf5jtk/view?usp=drive_link"


st.header("Movies recommendation")

# Download the pkl file
with st.spinner("Downloading the pkl file..."):
    download_pkl_file(pkl_file_url1, "your_pkl_file1.pkl")

# Load the pkl file
with open("your_pkl_file.pkl1", "rb") as f:
    movies = pd.read_pickle(f)
    
# Download the pkl file
with st.spinner("Downloading the pkl file..."):
    download_pkl_file(pkl_file_url2, "your_pkl_file2.pkl")

# Load the pkl file
with open("your_pk2_file.pkl1", "rb") as f:
    similarity = pd.read_pickle(f)


# movies = pd.read_pickle('artifacts/movie_list.pkl')
# similarity = pd.read_pickle('artifacts/similarity.pkl')

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