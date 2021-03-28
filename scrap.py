from control import *
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
import csv
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen
import urllib.request as urllib
main_link = "https://thetvdb.com/series/my-hero-academia"
main_link1 = "https://thetvdb.com/series/91-days"
#main_link = "https://thetvdb.com/series/91-days"
main_link2 = "https://thetvdb.com/series/another"
def get_meta(link_path):
    try:
        driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        driver.get(link_path)

        title = driver.find_element_by_xpath("/html/body/div[3]/h1")
        sypnosis = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/p")
        backgrounds = driver.find_elements_by_css_selector('.lightbox .img-responsive')
        count = 0
        for i in backgrounds:
            try:
                src = i.get_attribute('src')

                # download the image
                urllib.urlretrieve(src, str(count)+".png")
                count = count +1
            except:
                count = count +1
            
        driver.close()  
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)

get_meta(main_link2)
#changeWidth("0.png",1920,1080)