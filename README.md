
# Media-Server-Flask-V-1.1 - Movie/ Show Streaming Website
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
Current login credentials User: dawood
pass: 9265. To register a new user go to app.py and uncomment register function
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

## Screen Shots

![media](https://user-images.githubusercontent.com/44601684/118688801-d0b5bb80-b81f-11eb-8bba-55972055827d.PNG)
![media1](https://user-images.githubusercontent.com/44601684/118695584-ccd96780-b826-11eb-9528-ff36a9c37e0d.PNG)
![media2](https://user-images.githubusercontent.com/44601684/118695593-cfd45800-b826-11eb-9b8d-2bb94973bfb5.PNG)
![media3](https://user-images.githubusercontent.com/44601684/118695601-d1058500-b826-11eb-80f2-6d3de80596dd.PNG)
![media4](https://user-images.githubusercontent.com/44601684/118695608-d236b200-b826-11eb-9d41-c0d03f24d950.PNG)
![media5](https://user-images.githubusercontent.com/44601684/118695631-d6fb6600-b826-11eb-9093-42ba2b782000.PNG)
![media6](https://user-images.githubusercontent.com/44601684/118695720-f0041700-b826-11eb-9e8f-fe8e54629426.PNG)
![media7](https://user-images.githubusercontent.com/44601684/118695775-fbefd900-b826-11eb-8f48-fe5800087325.PNG)
![media8](https://user-images.githubusercontent.com/44601684/118695791-0316e700-b827-11eb-9198-1e4963a385e9.PNG)
![media9](https://user-images.githubusercontent.com/44601684/118695800-06aa6e00-b827-11eb-9aaf-71072cc61798.PNG)
![media10](https://user-images.githubusercontent.com/44601684/118695820-0ca04f00-b827-11eb-9ddb-738cd4ee3c13.PNG)
![media11](https://user-images.githubusercontent.com/44601684/118695837-0f9b3f80-b827-11eb-90c2-811abc639061.PNG)
![media12](https://user-images.githubusercontent.com/44601684/118695848-11fd9980-b827-11eb-9728-ecd39d34bfa7.PNG)
