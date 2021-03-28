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
try:
    driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
    driver.get(main_link)

    title = driver.find_element_by_xpath("/html/body/div[3]/h1")
    sypnosis = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]/p")
    backgrounds = driver.find_elements_by_css_selector('.lightbox .img-responsive')
    count = 0
    for i in backgrounds:
        src = i.get_attribute('img')

        # download the image
        urllib.urlretrieve(src, str(count)+".png")

        # f = open('pics2/','w')
        # print("I am ahere")
        # f.write(i.get_screenshot_as_file())
        # f.close()
    # banners = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[7]")
    # posters = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[9]")
    # for x in range(2):
    #     price = driver.find_elements_by_css_selector('.keMYfJ')
    #     bedsInfo = driver.find_elements_by_css_selector('.bjqKkI')
    #     area = driver.find_elements_by_css_selector('.qjlKt .dZyoXR')
    #     address = driver.find_elements_by_css_selector('.eCjeDf+ .dZyoXR')
    #     address2 = driver.find_elements_by_css_selector('.dZyoXR+ .dZyoXR')
    #     for i in range(len(price)):
    #         print(str(i+1))
    #         print(price[i].text)
    #         for j in range(2):
    #             print(bedsInfo[count].text)
    #             count +=1            
    #         print(area[i].text)
    #         print(address[i].text)
    #         print(address2[i].text)
    #         print("\n*************New Address******\n")
    #     saveInCsv(price,bedsInfo,area,address,address2)
    #     driver.find_element_by_xpath('//*[@id="resultsColumn"]/div[2]/ul/li[8]/a').click()    
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
