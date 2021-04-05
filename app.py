import os
from flask import Flask, request, render_template, send_from_directory, jsonify

import re
from control import *
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__author__ = 'AT-MOST'
root_path_image = "static/images/media/Anime test" #Path for meta
root_path_anime = "D:/Anime"#Path for media
app = Flask(__name__)
ImageDir = {}
Anime_Path = {}
withoutSpace = []

@app.route("/")
def index():

    return  render_template('home.html',data = Anime_Path)

if __name__ == "__main__":
    ImageDir = getDict(root_path_image)
    Anime_Path = getDict(root_path_anime)
    
    app.run(port=6545, debug=True)