import os
from flask import Flask, request, render_template, send_from_directory, jsonify, flash, url_for, redirect
import threading
import re
from control import *
from metaDataClass import *
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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
root_background = "images/Background/bg2.jpg"

@app.route("/movie/<var>", methods=["GET"])
def movie(var):
    try:
        print(var)
        syp = csvList.returnSyp(var)
        print(syp)
        newBack = "images/media/"
        type_season = ""
        flag = False
        videoCount = []
        types = ""
        for i in AnimeMovie_Path:
            if i == var:
                flag = True
                types = "Anime Movies"
                videoCount = getVideoPath(root_path_movie+"/"+i)

        if flag==True:
            newBack = newBack+"Anime Movies/"+var+"/background.jpg"
            type_season = "Anime Movies/"
        else:
            newBack = newBack+"movie/"+var+"/background.jpg"
            type_season = "movie/"
            print("else part")
            for i in Movie_Path:
                if i == var:
                    types = "movie"
                    videoCount = getVideoPath(root_path_movie+"/"+i)

        return  render_template('movies.html',TitleText = var, Syp = syp, BackImage = newBack, Type_season = type_season, seasons = seasonCount, Type = types)
    except Exception as e:
        return  render_template('movies.html',TitleText = var, Syp = syp, BackImage = newBack, Type_season = type_season, seasons = seasonCount)
        
        #return render_template('505.html', exp = e)
    

@app.route("/season/<var>", methods=["GET"])
def season(var):
    try:
        print(var)
        syp = csvList.returnSyp(var)
        print(syp)
        newBack = "images/media/"
        type_season = ""
        flag = False
        seasonCount = []
        types = ""
        for i in Anime_Path:
            if i == var:
                flag = True
                seasonCount = Anime_Path[i]
                types = "Anime"

        if flag==True:
            newBack = newBack+"Anime/"+var+"/background.jpg"
            type_season = "Anime/"
        else:
            newBack = newBack+"shows/"+var+"/background.jpg"
            type_season = "shows/"
            print("else part")
            for i in TvShow_Path:
                if i == var:
                    seasonCount = TvShow_Path[i]
                    types = "shows"
        return  render_template('shows.html',TitleText = var, Syp = syp, BackImage = newBack, Type_season = type_season, seasons = seasonCount, Type = types)
    except Exception as e:
        return render_template('505.html', exp = e)
    


@app.route("/dashboard/",methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def index():
    try:
        return  render_template('home.html',data = Anime_Path, animemov = AnimeMovie_Path, show = TvShow_Path, movie = Movie_Path, BackImage= root_background)
    except Exception as e:
        return render_template('505.html', exp = e)



@app.route("/login/", methods=["GET","POST"])
#@app.route("/", methods=["GET","POST"])
def login_page():
    error = ""
    try:
        if request.method == "POST":
            attemted_user = request.form['username']
            attemted_pass = request.form['password']

            print(attemted_user)
            print(attemted_pass)
            if attemted_user == "admin" and attemted_pass=="pass":
                return redirect(url_for('index'))
            else:
                error = "Invalid Credentials. Try again!"
        return render_template('login.html', error = error)
    except Exception as e:
        return render_template('505.html', exp = e)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
if __name__ == "__main__":
    #ImageDir = getDict(root_path_image)
    
    csvList.SetMetaCSV(readingMeta('static/metadata.csv')) 
    Anime_Path = getDict(root_path_anime)
    AnimeMovie_Path = getDict(root_path_anime_movie)
    TvShow_Path = getDict(root_path_show)
    Movie_Path = getDict(root_path_movie)

    for i in Movie_Path:
        getVideoPath(root_path_movie+"/"+i)

    try:
        total = len(Anime_Path)+len(AnimeMovie_Path)+len(TvShow_Path)+len(Movie_Path)
        if total-1 > len(csvList.GetMetaCSV()):
            t1 = threading.Thread(target=getMetaAll, args=(root_path_anime,root_path_show,root_path_movie,root_path_anime_movie,image_path_anime,image_path_show,
            image_path_movie,image_path_anime_movies,))
            t1.start()
            print("Wroking")
    except:
        print("Error: Unable to start thread!")
    app.run(port=6545, debug=False)
    