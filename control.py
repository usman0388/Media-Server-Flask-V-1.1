import os
import cv2
def getDict(path):    
    data = {}
    arr = os.listdir(path)

    for i in arr:
        arr2 = os.listdir(path+"/"+i)
        data[i] = arr2
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
