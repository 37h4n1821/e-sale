import sys
from pathlib import Path

ruta=str(Path(__file__).absolute())
ruta=ruta.replace("\\","/")
ruta=ruta.replace(ruta.split("/")[-2]+"/"+ruta.split("/")[-1],"")

sys.path.append(ruta)

from Global.imports import *

def extractData(linkProduct, brand):
    data = requests.get(linkProduct)
    data=data.content
    data=b(data,"lxml")
    
    categories = data.find('div', {"class":"container"}).text
    print(categories)
    name=data.find('section',{"class":"product-header"}).find('h1').text
    print(brand)
    print(name)
    id=data.find('span',{"class":"sku"}).text
    print(id)
    
    normal=""
    internet=""
    ripley=""

    if data.find('div',{"class":"product-normal-price"}):
        normal = data.find('div',{"class":"product-normal-price"}).text.strip("Normal")
    else:
        normal = 0
    print(normal)
    if data.find('div',{"class":"product-internet-price"}) or data.find('div',{"class":"product-internet-price-not-best"}):
        internet = data.find('div',{"class":"product-internet-price"}).text.strip("Internet") or data.find('div',{"class":"product-internet-price-not-best"}).text.strip("Internet")
    else:
        internet = 0
    print(internet)
    if data.find('div',{"class":"product-ripley-price"}):
        ripley = data.find('div',{"class":"product-ripley-price"}).text.strip("Tarjeta Ripley o Chek")
    else:
        ripley = 0
    print(ripley)

linkProduct = 'https://simple.ripley.cl/taste-of-the-wild-prey-turkey-formula-for-dogs-1136-kgs-mpm00018161064?s=mdco'
brand = "Hola"