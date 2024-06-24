from flask import Flask,request,jsonify
import get_movie
app = Flask(__name__)
from flask_cors import CORS
# cors = CORS(app,origins='http://localhost:5173')
cors = CORS(app,origins='*')
@app.route('/get_movies_names', methods=['GET'])
def get_movies_names():
    # movie_names = get_movie()
    response = jsonify({
        'movie': get_movie.get_movie()
    })
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
    response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
    return response


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    firstmovie = request.json
    # firstmovie = request.form['movie']
    # location = request.form['location']
    response = jsonify({
        'recommendation': get_movie.recommend(firstmovie)
        
    })
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
    response.headers.add('Access-Control-Allow-Origin', '*')
    # response.header("Access-Control-Allow-Origin", "*");
    # response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")

    return response


