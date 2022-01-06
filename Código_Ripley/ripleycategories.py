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

driver = webdriver.Chrome(options=chrome_options, executable_path= path)

url = 'https://simple.ripley.cl'

driver.get(url)
menu = driver.find_element_by_xpath('//div[@class="menu-button"]')
menu.click()
delay(1)

categories = driver.find_element_by_xpath('//div[@class="tree-node-items"]')
for category in categories.find_elements_by_tag_name('a'):
    try:
        print('Categoría: ',category.get_attribute('aria-label'))
        category.click()
        delay(1)
        subcategories = driver.find_element_by_xpath('//div[@class="category-tree__expanded-categories"]').text
        print('Subcategoría: ',subcategories)
        back = driver.find_element_by_xpath('//a[@class="tree-node-back-button"]')
        back.click()
        delay(1)
    except:
        print('done')
