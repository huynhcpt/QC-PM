from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as BS
import pandas as pd
import re, time
import os

url="https://www.ebth.com/search?q=rolex+watch"

driver=webdriver.Chrome(executable_path='D:\Downloads\Installers\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(20)
driver.get(url)

soup=BS(driver.page_source, 'html.parser')
link=soup.find_all('a',class_="items-grid__item item")

for i in link:
    print(i['href'])

driver.quit()