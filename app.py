import os
from flask import Flask, request, render_template, send_from_directory, jsonify
import threading
import re
from control import *
from metaDataClass import *
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
Meta_CSV = []
__author__ = 'AT-MOST'

image_path_anime = "static/images/media/Anime"
image_path_anime_movies = "static/images/media/Anime Movies"
image_path_movie = "static/images/media/movie"
image_path_show = "static/images/media/shows"

root_path_anime = "D:/Anime"
root_path_anime_movie = "D:/Anime Movies"
root_path_movie = "D:/movie"
root_path_show = "D:/shows"

app = Flask(__name__)
ImageDir = {}
Anime_Path = {}
AnimeMovie_Path = {}
TvShow_Path = {}
Movie_Path = {}
csvList = CSVData()
@app.route("/")
def index():

    return  render_template('home.html',data = Anime_Path, animemov = AnimeMovie_Path, show = TvShow_Path, movie = Movie_Path)

if __name__ == "__main__":
    #ImageDir = getDict(root_path_image)
    
    csvList.SetMetaCSV(readingMeta('static/metadata.csv')) 
    print(csvList.GetMetaCSV())
    Anime_Path = getDict(root_path_anime)
    AnimeMovie_Path = getDict(root_path_anime_movie)
    TvShow_Path = getDict(root_path_show)
    Movie_Path = getDict(root_path_movie)
    print(len(Anime_Path))
    print(len(AnimeMovie_Path))
    print(len(TvShow_Path))
    print(len(Movie_Path))

    try:
        total = len(Anime_Path)+len(AnimeMovie_Path)+len(TvShow_Path)+len(Movie_Path)
        if total > len(Meta_CSV):
            t1 = threading.Thread(target=getMetaAll, args=(root_path_anime,root_path_show,root_path_movie,root_path_anime_movie,image_path_anime,image_path_show,
            image_path_movie,image_path_anime_movies,))
            t1.start()
            print("Wroking")
    except:
        print("Error: Unable to start thread!")
    app.run(port=6545, debug=False)
    