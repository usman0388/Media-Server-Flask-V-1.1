from control import *
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import csv
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen
import urllib.request as urllib
import csv

main_link = "https://thetvdb.com/series/my-hero-academia"
main_link1 = "https://thetvdb.com/series/91-days"
main_link = "https://thetvdb.com/series/demon-slayer"
main_link2 = "https://thetvdb.com/series/another"
main_link3 = "https://thetvdb.com/series/attack-on-titan"
main_link4 = "https://thetvdb.com/series/akame-ga-kill"
link_Anime_TV = "https://thetvdb.com/series/"
link_Anime_MOV = "https://thetvdb.com/movies/"
link_Movie = "https://thetvdb.com/movies/"

Meta_CSV = []
def generate_link(name,path):
    name = name.lower()
    name = name.replace(" ","-")
    new_path = path+name
    return new_path

def checkIfExistInList(title):
    if len(Meta_CSV) == 0:
        return -1
    else:
        count = 0
        for i in Meta_CSV:
            if title == i[0]:
                return count
            else:
                count +=1
    return -1
def updateIfFound(title, syp, itr):
    if Meta_CSV[itr][1] != syp:
        Meta_CSV[itr][1] = syp
    return True
        
def writeMetaCsv(title, syp, filename):
    try:
        num = checkIfExistInList(title)
        if num != -1:
            if updateIfFound(title,syp,num):
                return      
        static_path = "static/"
        #filename = "metadata.csv"
        # field names
        fields = ['title', 'sypnosis']
            
        # data rows of csv file
        rows = [title, syp]
        if not os.path.exists(static_path+"/"+filename):
            with open(static_path+"/"+filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fields)
                writer.writerow(rows)
                Meta_CSV.append(rows)
        else:
            with open(static_path+"/"+filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(rows)
                Meta_CSV.append(rows)
    except:
        print("Error while saving")

def get_meta_anime(link_path,path):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options,executable_path='driver/chromedriver.exe')
        #driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        
        driver.get(link_path)

        title = driver.find_element_by_xpath("/html/body/div[3]/h1")
        sypnosis = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/p")
        backgrounds = driver.find_elements_by_css_selector('.row:nth-child(15) .img-responsive')
        if len(backgrounds) == 0:
            backgrounds = driver.find_elements_by_css_selector('.row:nth-child(16) .img-responsive')
        if len(backgrounds) == 0:
            backgrounds = driver.find_elements_by_css_selector('.row:nth-child(12) .img-responsive')
        if len(backgrounds) == 0:
            backgrounds = driver.find_elements_by_css_selector('.row:nth-child(17) .img-responsive')

        count = 0
        for i in backgrounds:
            try:
                src = i.get_attribute('src')

                # download the image
                urllib.urlretrieve(src,path+str(count)+".png")
                count = count +1
            except:
                count = count +1
        writeMetaCsv(title.text,sypnosis.text,"metadata.csv")
        driver.close()  
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    except:
        print(link_path)

def get_meta_anime_movie(link_path,path):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options,executable_path='driver/chromedriver.exe')
        driver.get(link_path)

        title = driver.find_element_by_xpath("/html/body/div[3]/h1")
        sypnosis = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/p")
        #backgrounds = driver.find_elements_by_css_selector('.lightbox .img-responsive')
        backgrounds = driver.find_elements_by_css_selector('.row:nth-child(13) .img-responsive')
        
        count = 0
        for i in backgrounds:
            try:
                src = i.get_attribute('src')

                # download the image
                urllib.urlretrieve(src,path+str(count)+".png")
                count = count +1
            except:
                count = count +1
        writeMetaCsv(title.text,sypnosis.text,"metadata.csv")
        driver.close()  
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)




def get_meta_movies(link_path,path):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options,executable_path='driver/chromedriver.exe')
        driver.get(link_path)

        title = driver.find_element_by_xpath("/html/body/div[3]/h1")
        sypnosis = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/p")
        #backgrounds = driver.find_elements_by_css_selector('.lightbox .img-responsive')
        backgrounds = driver.find_elements_by_css_selector('.row:nth-child(11) .img-responsive')
        
        count = 0
        for i in backgrounds:
            try:
                src = i.get_attribute('src')

                # download the image
                urllib.urlretrieve(src,path+str(count)+".png")
                count = count +1
            except:
                count = count +1
        writeMetaCsv(title.text,sypnosis.text,"metadata.csv")
        driver.close()  
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)

def get_meta_TV(link_path,path):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options,executable_path='driver/chromedriver.exe')
        driver.get(link_path)

        title = driver.find_element_by_xpath("/html/body/div[3]/h1")
        sypnosis = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/p")
        #backgrounds = driver.find_elements_by_css_selector('.lightbox .img-responsive')
        backgrounds = driver.find_elements_by_css_selector('.row:nth-child(16) .img-responsive')
        
        count = 0
        for i in backgrounds:
            try:
                src = i.get_attribute('src')

                # download the image
                urllib.urlretrieve(src,path+str(count)+".png")
                count = count +1
            except:
                count = count +1
        writeMetaCsv(title.text,sypnosis.text,"metadata.csv")
        driver.close()  
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)

def readCSV(path, list_data):
    if not os.path.exists(path):
        print("FILE NOT EXISTS.")
    else:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    list_data.append(row)
                    line_count += 1
    return list_data

#get_meta_anime(generate_link("Fate Apocrypha",main_link),"static/")
#changeWidth("0.png",1920,1080)
Meta_CSV=readCSV('static/metadata.csv',Meta_CSV)
root_path_image = "static/images/media/Anime test"
ImageDir = getDict(root_path_image)

for i in ImageDir:
    get_meta_anime(generate_link(i,link_Anime_TV),root_path_image+"/"+i+"/")
