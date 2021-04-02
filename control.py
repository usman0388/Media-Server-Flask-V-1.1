import os
import cv2
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
    for i in data:
        print(i)
        for j in data[i]:
            print("\t"+i+"/"+j)
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
root_path_anime = "D:/Anime"
root_path_anime_movie = "D:/Anime Movies"
root_path_movie = "D:/movie"
root_path_show = "D:/shows"
#getDict(root_path_anime)
#getDict(root_path_anime_movie)
#getDict(root_path_movie)
#getDict(root_path_show)



# path = "D:/Anime/Our Last Crusade or the Rise of a New World/Our Last Crusade or the Rise of a New World S01"
# arr = os.listdir(path)
# count = 1
# for i in arr:
#     os.rename(path+"/"+i, path+"/Our Last Crusade or the Rise of a New World E0"+str(count)+".mp4")
#     count +=1


#changeName("D:/Anime/Black Clover/Black Clover S02","Black Clover S1E",52,".mp4")


# root_path_image = "static/images/media/Anime test"
# ImageDir = getDict(root_path_image)

# for i in ImageDir:
#     data = root_path_image+"/"+i+"/display.jpg"
#     changeWidth(data)
# root_path_anime = "media/Anime"
#ImageDir = getDict(root_path_image)
# Anime_Path = getDict(root_path_anime)

# for i in Anime_Path:
#     print(i+"\t"+ImageDir[i][1])
