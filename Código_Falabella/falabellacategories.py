import requests
from bs4 import BeautifulSoup as b
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import os
from time import sleep as delay

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-crash-reporter")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-in-process-stack-traces")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--silent")
chrome_options.add_argument("--output=/dev/null")

path = './chromedriver'
#options=chrome_options, 
driver = webdriver.Chrome(executable_path= path)

url = 'https://www.falabella.com/falabella-cl/category/cat2018/Celulares-y-Telefonos'

driver.get(url)
menu = driver.find_element_by_xpath('//span[@class="MarketplaceHamburgerBtn-module_title__2KG47"]')
menu.click()
delay(1)
#<div class="MediaComponent-module_tablet-desktop__3xCIl"><span class="MarketplaceHamburgerBtn-module_title__2KG47">

categories = driver.find_elements_by_xpath('//div[@class="TaxonomyDesktop-module_categoryWrapper__3YBaF"]')
for category in categories:
    print(category.text)
    category.click()
    delay(1)
    links = driver.find_element_by_xpath('//div[@class="SecondLevelCategories-module_secondLevelMenuItemsBox__2i00Y"]')
    for link in links.find_elements_by_tag_name('a'):
        print(link.get_attribute('href'))
    delay(1)