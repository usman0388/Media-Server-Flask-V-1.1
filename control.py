import os
import cv2
from scrap import *
from passlib.hash import sha256_crypt

def getDict(path):    
    data = {}
    arr = os.listdir(path)
    nested = []
    for i in arr:
        arr2 = os.listdir(path+"/"+i)
        for j in arr2:
            if os.path.isdir(path+"/"+i+"/"+j):
                nested.append(j)
        data[i] = nested
        nested = []
    return data
def changeWidth(path,width,height):

    try:
            
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        print('Original Dimensions : ',img.shape)

        #width = 640
        #height = 960
        dim = (width, height)
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(path,resized)
    except:
        print(path+" Not found!")

def getMetaAnime(path, image_save_path):
    ImageDir_Anime = getDict(path)
    flag = 1
    for i in ImageDir_Anime:
        newLink = generate_link(i,link_Anime_TV)
        get_meta_anime(newLink,image_save_path+"/"+i+"/")
        for j in ImageDir_Anime[i]:
            print(j)
            getSeasonMeta("https://www.thetvdb.com/series/"+organize_words(i)+"/seasons/official/"+str(flag),image_save_path+"/"+i+"/"+j+"/" )
            flag +=1
        flag = 1

def getMetaTVshow(path, image_save_path):
    ImageDir_Show = getDict(path)
    flag = 1
    for i in ImageDir_Show:
        newLink = generate_link(i,link_Anime_TV)
        get_meta_anime(newLink,image_save_path+"/"+i+"/")
        for j in ImageDir_Show[i]:
            print(j)
            getSeasonMeta("https://www.thetvdb.com/series/"+organize_words(i)+"/seasons/official/"+str(flag),image_save_path+"/"+i+"/"+j+"/" )
            flag +=1
        flag = 1

def getMetaMovie(path, image_save_path):
    ImageDir_movie = getDict(path)
    for i in ImageDir_movie:
        newLink = generate_link(i,link_Movie)
        get_meta_movies(newLink,image_save_path+"/"+i+"/")

def getMetaAnimeMovie(path, image_save_path):
    ImageDir_movie_anime = getDict(path)
    for i in ImageDir_movie_anime:
        newLink = generate_link(i,link_Movie)
        get_meta_movies(newLink,image_save_path+"/"+i+"/")


def getMetaAll(AnimePath, TvShowPath, MoviePath, AnimeMoviePath, Save_AnimePath, Save_TvShowPath, Save_MoviePath, Save_AnimeMoviePath):
    getMetaAnime(AnimePath, Save_AnimePath)
    getMetaTVshow(TvShowPath, Save_TvShowPath)
    getMetaMovie(MoviePath, Save_MoviePath)
    getMetaAnimeMovie(AnimeMoviePath, Save_AnimeMoviePath)

def readingMeta(path):
    structure = readCSV(path)
    return structure

def getVideoPath(pathData):
    pathList = ""
    ext = [".mp4",".mkv",".avi","mov"]
    for file in os.listdir(pathData):
        if file.endswith(tuple(ext)):
            print(os.path.join(pathData, file))
            pathList= pathData+"/"+file
    print(pathList)
    return pathList
def getEpisodeList(pathData):
    pathList = []
    ext = [".mp4",".mkv",".avi","mov"]
    for file in os.listdir(pathData):
        if file.endswith(tuple(ext)):
            print(os.path.join(pathData, file))
            pathList.append(pathData+"/"+file)
    print(pathList)
    return pathList
def getFileName(pathData):
    pathList = ""
    ext = [".mp4",".mkv",".avi","mov"]
    for file in os.listdir(pathData):
        if file.endswith(tuple(ext)):
            print(os.path.join(pathData, file))
            pathList= file
    print(pathList)
    return pathList

def checkIfExists(name, dataList):
    for i in dataList:
        if i == name:
            return True
    return False

def SessionCommit(tempModel, db):
    db.session.add(tempModel)
    db.session.commit()
def GetUserFrmDatabase(attemted_user, UserModel):
    return UserModel.query.filter_by(UserName=attemted_user).first_or_404()