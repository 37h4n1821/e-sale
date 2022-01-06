import sys
from pathlib import Path

ruta=str(Path(__file__).absolute())
ruta=ruta.replace("\\","/")
ruta=ruta.replace(ruta.split("/")[-2]+"/"+ruta.split("/")[-1],"")

sys.path.append(ruta)

from Global.imports import *

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

def Get_Producto(url):
    driver.get(url)
    WebDriverWait(driver, 5)
    print(url)
    body = driver.execute_script("return document.body")
    source = body.get_attribute('innerHTML')
    soup = b(source, "html.parser")
    ID=soup.find('div',{'class':'pdp-sku'}).text.replace("SKU ","").strip('\n')

    PRECIOS=[]
    for precio in soup.find('div',{'class':'price'}):
        PRECIOS.append(precio.text.replace('\n',''))
    
    NOMBRE=soup.find('h1',{'class':'no-pb js-product-name'}).text.strip('\n')

    CATEGORIAS=soup.find_all('a',{'class':'breadcrumb-element'})
    print(CATEGORIAS)

    print(PRECIOS)
    print(ID)
    print(NOMBRE)




for categoria in CATEGORIAS:
    Productos=[]
    for n in range(5000,999999999,40):
        driver.get(url+categoria+'/?start='+str(n)+'&sz=40')
        WebDriverWait(driver, 5)
        body = driver.execute_script("return document.body")
        source = body.get_attribute('innerHTML')
        soup = b(source, "html.parser")
        if len(soup.find_all('a',{'class':'js-product-layer'}))>0:
            for i in soup.find_all('a',{'class':'js-product-layer'}):
                if not i['href'] in Productos:
                    if not "https://www.paris.cl/" in i['href']:
                        Productos.append('https://www.paris.cl/'+i['href'])
                    else:
                        Productos.append(i['href'])
        else:
            break
        break

    Productos=list(set(Productos))
    print(len(Productos))
    for producto in Productos:
        Get_Producto(producto)
        continue
    print(len(Productos))

