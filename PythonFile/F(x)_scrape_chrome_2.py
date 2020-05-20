from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
import pandas as pd

#url
driver = webdriver.Chrome("C:/Users/Asdar/Desktop/chromedriver/chromedriver.exe")

prices=[]
products=[]
ratings=[]
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")

#scrape data
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_6BWGkk'})
    rating=a.find('div', attrs={'class':'niH0FQ'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

print(products)
'''
df = pd.DataFrame({'Product Name':products, 'product price':prices,'product rating':ratings})
df.to_csv('produst_details.csv', index = False, encoding='utf-8')
'''