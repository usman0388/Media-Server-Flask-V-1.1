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
main_link = "https://thetvdb.com/series/"
main_link2 = "https://thetvdb.com/series/another"
main_link3 = "https://thetvdb.com/series/attack-on-titan"
main_link4 = "https://thetvdb.com/series/akame-ga-kill"

def generate_link(name,path):
    name = name.lower()
    name = name.replace(" ","-")
    new_path = path+name
    return new_path

def writeMetaCsv(title, syp):
    try:
        static_path = "static/"
        filename = "metadata.csv"
        # field names
        fields = ['title', 'sypnosis']
            
        # data rows of csv file
        rows = [title, syp]
        if not os.path.exists(static_path+"/"+filename):
            with open(static_path+"/"+filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fields)
                writer.writerow(rows)
        else:
            with open(static_path+"/"+filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(rows)
    except:
        print("Error while saving")

def get_meta(link_path,path):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options,executable_path='driver/chromedriver.exe')
        driver.get(link_path)

        title = driver.find_element_by_xpath("/html/body/div[3]/h1")
        sypnosis = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/p")
        #backgrounds = driver.find_elements_by_css_selector('.lightbox .img-responsive')
        backgrounds = driver.find_elements_by_css_selector('.row:nth-child(15) .img-responsive')
        
        count = 0
        for i in backgrounds:
            try:
                src = i.get_attribute('src')

                # download the image
                urllib.urlretrieve(src,path+str(count)+".png")
                count = count +1
            except:
                count = count +1
        writeMetaCsv(title.text,sypnosis.text)
        driver.close()  
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)


get_meta(generate_link("Fate Apocrypha",main_link),"static/")
#changeWidth("0.png",1920,1080)
