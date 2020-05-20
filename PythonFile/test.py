from selenium import webdriver

link = "https://accounts.google.com"
driver = webdriver.Chrome(executable_path=r'C:/Users/Asdar/Desktop/chromedriver/chromedriver.exe')
driver.get(link)