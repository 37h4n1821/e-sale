import requests
from bs4 import BeautifulSoup as b
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import os
import sys
from time import sleep as delay


if sys.platform == "linux" or sys.platform == "linux2":
    path = './WebDrivers/linux'
elif sys.platform == "darwin":
    path = './WebDrivers/mac'
elif sys.platform == "win32":
    path = './WebDrivers/windows.exe'


SERVIDOR='http://villaloscisnesnavidad.epizy.com'

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


driver = webdriver.Chrome(options=chrome_options, executable_path= path)


def escribir(txt):
    wr=open("falabella.html","w")
    wr.write(txt)
    wr.close()