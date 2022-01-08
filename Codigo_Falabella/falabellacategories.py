import sys
from pathlib import Path

ruta=str(Path(__file__).absolute())
ruta=ruta.replace("\\","/")
ruta=ruta.replace(ruta.split("/")[-2]+"/"+ruta.split("/")[-1],"")

sys.path.append(ruta)

from Global.imports import *

url = 'https://www.falabella.com/falabella-cl/category/cat2018/Celulares-y-Telefonos'

driver2.get(url)
menu = driver2.find_element_by_xpath('//span[@class="MarketplaceHamburgerBtn-module_title__2KG47"]')
menu.click()
delay(1)
#<div class="MediaComponent-module_tablet-desktop__3xCIl"><span class="MarketplaceHamburgerBtn-module_title__2KG47">

categories = driver2.find_elements_by_xpath('//div[@class="TaxonomyDesktop-module_categoryWrapper__3YBaF"]')
for category in categories:
    print(category.text)
    category.click()
    delay(1)
    links = driver2.find_element_by_xpath('//div[@class="SecondLevelCategories-module_secondLevelMenuItemsBox__2i00Y"]')
    for link in links.find_elements_by_tag_name('a'):
        print(link.get_attribute('href'))
    delay(1)