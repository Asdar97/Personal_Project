import random
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

data = webdriver.Chrome('C:/Users/Asdar/Desktop/chromedriver/chromedriver.exe')
word = []
data.get('http://norvig.com/ngrams/sowpods.txt')

content = data.page_source
soup = BeautifulSoup(content)

a = soup.find('pre')
#attrs={'style':'word-wrap: break-word; white-space: pre-wrap'})
#print(a)
a = str(a)

with open ('random_word.txt','w+') as rd:
    rd.write(a)