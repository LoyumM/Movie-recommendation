import pickle
import streamlit as st 
import requests

st.header("Movies recommendation")
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)