import pickle
from pickle import load
import pandas as pd
import pandas.core.indexes as i
import numpy as np
import streamlit as st
from PIL import Image


#opening the image
image = Image.open('image.jpg')

st.header('Movie Recommendation System')
#displaying the image on streamlit app
st.image(image)

# movie_content_based = pd.read_pickle('movie_content_based.pkl')
# indices = pickle.load(open('movie_content_based.pkl','rb'))
movie_content_based = pickle.load(open('movie_content_based.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_content_based = movie_content_based.reset_index()
titles = movie_content_based['title']
indices = pd.Series(movie_content_based.index, index=movie_content_based['title'])

movie_name = st.selectbox("Type or select a movie from the dropdown",
                                  movie_content_based['title'])

if st.button('Show Recommendation'):
    # titles = get_recommendations(movie_name)
    idx = indices[movie_name]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    for i in movie_content_based['title'].iloc[movie_indices].head(10):
        st.text(i)