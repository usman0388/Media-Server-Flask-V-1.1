import os
from flask import Flask, request, render_template, send_from_directory, jsonify, flash, url_for, redirect, session
from flask_restful import fields, marshal_with
import threading
import re
from control import *
from metaDataClass import *
import shutil
from flask_sqlalchemy import SQLAlchemy
from functools import wraps


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__author__ = 'AT-MOST'

image_path_anime = "static/images/media/Anime"
image_path_anime_movies = "static/images/media/Anime Movies"
image_path_movie = "static/images/media/movie"
image_path_show = "static/images/media/shows"

root_path_anime = "static/movie data/Anime"
root_path_anime_movie = "static/movie data/Anime Movies"
root_path_movie = "static/movie data/movie"
root_path_show = "static/movie data/shows"

app = Flask(__name__)
app.secret_key = "ATMOST"  
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
db = SQLAlchemy(app)
from database import resourse_fields, UserModel


ImageDir = {}
Anime_Path = {}
AnimeMovie_Path = {}
TvShow_Path = {}
Movie_Path = {}
csvList = CSVData()
root_background = "images/Background/bg2.jpg"



def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login_page'))
    return wrap

@app.route("/season/watch/<TitleName>/season/<SeasonName>/<EpNum>", methods=["GET","POST"])
@login_required
def EpisodesWatch(TitleName,SeasonName,EpNum):
    try:
        newBack = "images/media/"
        EpisodesList = []
        if checkIfExists(TitleName, Anime_Path):
            type_season = "Anime/"
            newBack = newBack+"Anime/"+TitleName+"/background.jpg"
            EpisodesList = getEpisodeList(root_path_anime+"/"+TitleName+"/"+SeasonName)            
        elif checkIfExists(TitleName,TvShow_Path):
            type_season = "shows/"
            newBack = newBack+"Anime/"+TitleName+"/background.jpg"
            EpisodesList = getEpisodeList(root_path_show+"/"+TitleName+"/"+SeasonName)
        count = int(EpNum)-1
        if len(EpisodesList) > count:
            EpisodesList[count] = EpisodesList[count].replace("static/","")
            return render_template('WatchEpisodes.html',TitleText=TitleName, Syp=SeasonName, Episodes= EpisodesList,EpisodeCount= len(EpisodesList)+1, BackImage = newBack,VPath = EpisodesList[count])
    except Exception as e:
        return render_template('505.html', exp = e)



@app.route("/movie/<var>", methods=["GET"])
@login_required
def movie(var):
    try:
        syp = csvList.returnSyp(var)
        newBack = "images/media/"
        flag = False
        videoCount = ""

        for i in AnimeMovie_Path:
            if i == var:
                flag = True
                videoCount = getVideoPath(root_path_anime_movie+"/"+i)
                break

        if flag==True:
            newBack = newBack+"Anime Movies/"+var+"/background.jpg"
        else:
            newBack = newBack+"movie/"+var+"/background.jpg"
            print("else part")
            for i in Movie_Path:
                if i == var:
                    videoCount = getVideoPath(root_path_movie+"/"+i)
                    break
        videoCount = videoCount.replace("static/","")
        return  render_template('MovieWatch.html',VPath = videoCount, BackImage = newBack)
    except Exception as e:
        return render_template('505.html', exp = e)
    
@app.route("/season/watch/<TitleName>/season/<SeasonName>", methods=["GET"])
@login_required
def Episodes(TitleName,SeasonName):
    try:
        newBack = "images/media/"
        type_season = ""
        EpisodesList = []
        if checkIfExists(TitleName, Anime_Path):
            type_season = "Anime/"
            newBack = newBack+"Anime/"+TitleName+"/background.jpg"
            EpisodesList = getEpisodeList(root_path_anime+"/"+TitleName+"/"+SeasonName)            
        elif checkIfExists(TitleName,TvShow_Path):
            type_season = "shows/"
            newBack = newBack+"Anime/"+TitleName+"/background.jpg"
            EpisodesList = getEpisodeList(root_path_show+"/"+TitleName+"/"+SeasonName)
        return render_template('SeasonEpisodes.html',TitleText=TitleName, Syp=SeasonName,EpisodeCount= len(EpisodesList)+1, BackImage = newBack,Type_season = type_season)            
    except Exception as e:
        return render_template('505.html', exp = e)
        
@app.route("/season/<var>", methods=["GET"])
@login_required
def season(var):
    try:
        syp = csvList.returnSyp(var)
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
                break

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
                    break
        return  render_template('shows.html',TitleText = var, Syp = syp, BackImage = newBack, Type_season = type_season, seasons = seasonCount, Type = types)
    except Exception as e:
        return render_template('505.html', exp = e)
    


@app.route("/dashboard/",methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
@login_required
def index():
    try:
        return  render_template('home.html',data = Anime_Path, animemov = AnimeMovie_Path, show = TvShow_Path, movie = Movie_Path, BackImage= root_background)
    except Exception as e:
        return render_template('505.html', exp = e)





@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



# @app.route("/register/<Name>&<Password>", methods=["GET"])
# @marshal_with(resourse_fields)
# def Registering(Name, Password):
#     try:
#         TempUser = Name
#         TempPass = sha256_crypt.encrypt(Password)
#         tempModel = UserModel(UserName=TempUser, Pass = TempPass)
#         SessionCommit(tempModel, db)
#         return tempModel,201
#     except Exception as e:
#         return render_template('505.html', exp = e)

@app.route("/login/", methods=["GET","POST"])
def login_page():
    error = ""
    try:
        if 'logged_in' in session:
            return redirect(url_for('index'))
        if request.method == "POST":
            attemted_user = request.form['username']
            attemted_pass = request.form['password']

            print(attemted_user)
            print(attemted_pass)
            dUser = GetUserFrmDatabase(attemted_user, UserModel)
            print(dUser.UserName)
            print(dUser.Pass)
            if attemted_user == dUser.UserName:
                if sha256_crypt.verify(attemted_pass,dUser.Pass):
                    session['username'] = request.form['username']
                    session['logged_in'] = True
                    return redirect(url_for('index'))
            else:
                error = "Invalid Credentials. Try again!"
        return render_template('login.html', error = error)
    except Exception as e:
        return render_template('505.html', exp = e)


@app.route("/logout/")
@login_required
def logout():
    session.clear()
    return redirect(url_for('login_page'))
    
if __name__ == "__main__":
    
    csvList.SetMetaCSV(readingMeta('static/metadata.csv')) 
    Anime_Path = getDict(root_path_anime)
    AnimeMovie_Path = getDict(root_path_anime_movie)
    TvShow_Path = getDict(root_path_show)
    Movie_Path = getDict(root_path_movie)

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
    