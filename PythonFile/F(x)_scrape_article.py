import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
'''
url_link = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url_link)
soup = BeautifulSoup(r)
'''
driver = webdriver.Chrome("C:/Users/Asdar/Desktop/chromedriver/chromedriver.exe")
driver.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
content = driver.page_source
soup = BeautifulSoup(content)

article=[]
a = soup.find('article',href=False, attrs=({'class':'article main-content'}))
name = a.text
#article.append(name)

#with-open method
with open ("article bodo.txt", 'w+') as ar:
    ar.write(name)


