# Server-Flask-V-1.1 - Movie/ Show Streaming Website
This server is made using flask, reads the file from the given path, generate the links from the name of the show/ movie and gets its Meta-data from automated web scraping script running in threads using headless mode. The gathered, data that is Title, description and posters are saved in a csv file and the images are saved in file system. Sql alchemy database is implemented to save user data and password after encrypting them using passlib library.
## Installation
https://chromedriver.chromium.org/
Download chrome driver according to the installed chrome version. Go to Help -> About Google chrome to see your chrome version.


```bash
pip install passlib
pip install opencv-python
pip install flask
pip install shutil
pip install flask_restful
pip install flask_sqlalchemy
pip install selenium

```
## Login
User: dawood
pass: 9265
To register a new user go to app.py and uncomment register function
```bash
@app.route("/register/<Name>&<Password>", methods=["GET"])
 @marshal_with(resourse_fields)
 def Registering(Name, Password):
     try:
         TempUser = Name
         TempPass = sha256_crypt.encrypt(Password)
         tempModel = UserModel(UserName=TempUser, Pass = TempPass)
         SessionCommit(tempModel, db)
         return tempModel,201
     except Exception as e:
         return render_template('505.html', exp = e)
```
From your browser enter: http://127.0.0.1:6545/user&pass
and your new user and password will be registered.

## Usage
If running it locally the movie/show data should be placed in static directory. It has four categories Anime, Anime Movies, Movies and Shows. So there are four different variables which holds the path to the specific directory.
Data saved method:
Anime/91 Days/91 Days S01/

Variables that need to be given a new path:
```bash
root_path_anime = "ENTER YOUR PATH"
root_path_anime_movie = "ENTER YOUR PATH"
root_path_movie = "ENTER YOUR PATH"
root_path_show = "ENTER YOUR PATH"
```
## Limitations

The data saved in csv file, it does check for duplicate entry but if an already saved show/ movie directory is deleted form the file system. Then its data will not be deleted from the csv file nor its posters. The show/ movie name should be by the name according to https://thetvdb.com/ naming convention. As it is the website to get meta-data. 

