import json
import numpy as np
import pandas as pd
import pickle
from flask import Flask, jsonify, request
# from flask_cors import CORS
from flask_cors import CORS

movie_list = pickle.load(open('./newmovie.pkl','rb'))
movies = pd.DataFrame(movie_list)

similarity = pickle.load(open('./similarity.pkl','rb'))
# movies = pd.DataFrame(movie_list)

def get_movie():
    # print(movies['title'].values)
    return movies['title'].tolist()

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    recommended_movie = []
    recommended_movie_id = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        print(movie_id)
        # recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie.append((movies.iloc[i[0]].title,str(movie_id)))
    return recommended_movie

my_movies =  get_movie()
# print(my_movies)

recomendation = recommend('Avatar')
# print(recomendation)

    

if __name__ == '__main__':
    print("We are in get movies name")
    