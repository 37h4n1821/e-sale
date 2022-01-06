import sys

sys.path.insert(0, 'Global/')

from imports import *

url="https://www.paris.cl/"

driver.get(url)
WebDriverWait(driver, 2)

body = driver.execute_script("return document.body")
source = body.get_attribute('innerHTML')
soup = b(source, "html.parser")

CATEGORIAS=[]
for i in soup.find_all('li',{'class':'js-hamburger-top-element-li'}):
    if i.find('a')["data-category"]!="Nuevas Categorías" and i.find('a')["data-category"]!="Conciencia Celeste" and i.find('a')["data-category"]!="Moda Circular":
        CATEGORIAS.append(i.find('a')["data-category"].replace(" ","-").replace("í","i").replace("ñ","n"))

print(CATEGORIAS)

for categoria in CATEGORIAS:
    Productos=[]
    for n in range(5000,999999999,40):
        driver.get(url+categoria+'/?start='+str(n)+'&sz=40')
        print(url+categoria+'/?start='+str(n)+'&sz=40')
        WebDriverWait(driver, 2)
        body = driver.execute_script("return document.body")
        source = body.get_attribute('innerHTML')
        soup = b(source, "html.parser")
        if len(soup.find_all('a',{'class':'js-product-layer'}))>0:
            for i in soup.find_all('a',{'class':'js-product-layer'}):
                if not i['href'] in Productos:
                    Productos.append(i['href'])
        else:
            break
    print(len(Productos))

