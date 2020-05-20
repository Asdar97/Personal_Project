from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:/Users/Asdar/Desktop/chromedriver/chromedriver.exe")
titles = []
driver.get("https://www.nytimes.com/")

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('div', attrs={'class':'css-6p6lnl'}):
    title = a.find('div', attrs={'class':'css-1ez5fsm esl82me1'})
    name = title.text
    '''
    with open ('title news.txt', 'a') as new:
        new.write(name+'\n',)
    '''
    titles.append(name)
'''
#css-5b6thp esl82me0
a = soup.find('div', href=False, attrs={'class':'css-1ez5fsm esl82me1'})
b = soup.findAll('span', attrs={'class':'balancedHeadline'})
#a = list(a)
'''
#print(titles)
'''
df = pd.DataFrame({"Title":titles})
df.to_csv("NEWS_TITLE_IN_NEW_YORK.csv", index=False, encoding='utf-8')
'''
