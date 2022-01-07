import sys
from pathlib import Path

ruta=str(Path(__file__).absolute())
ruta=ruta.replace("\\","/")
ruta=ruta.replace(ruta.split("/")[-2]+"/"+ruta.split("/")[-1],"")

sys.path.append(ruta)

from Global.imports import *

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
        for subcategories in driver.find_elements_by_xpath('//ul[@class="category-tree__expanded-category"]'):
            subcategory = subcategories.find_element_by_tag_name('a').text
            print('Subcategoría: ',subcategory)
        back = driver.find_element_by_xpath('//a[@class="tree-node-back-button"]')
        back.click()
        delay(1)
    except:
        print('done')
