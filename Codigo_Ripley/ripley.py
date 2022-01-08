import sys
from pathlib import Path

ruta=str(Path(__file__).absolute())
ruta=ruta.replace("\\","/")
ruta=ruta.replace(ruta.split("/")[-2]+"/"+ruta.split("/")[-1],"")

sys.path.append(ruta)

from Global.imports import *

def extractData(linkProducts, brand):
    data = requests.get(linkProducts)
    data=data.content
    data=b(data,"lxml")
    send = False

    for i in range(0,4):
        try:
            categories = data.find('li', {"class":"breadcrumbs"}).text
            name=data.find('section',{"class":"product-header"}).find('h1').text
            print(categories)
            id=data.find('span',{"class":"sku"}).text
            
            normal=""
            internet=""
            ripley=""

            if data.find('div',{"class":"product-normal-price"}):
                normal = data.find('div',{"class":"product-normal-price"}).text.strip("Normal")
            else:
                normal = 0
            if data.find('div',{"class":"product-internet-price"}) or data.find('div',{"class":"product-internet-price-not-best"}):
                if data.find('div',{"class":"product-internet-price"}):
                    internet = data.find('div',{"class":"product-internet-price"}).text.strip("Internet")
                else:
                    internet = data.find('div',{"class":"product-internet-price-not-best"}).text.strip("Internet")
            else:
                internet = 0
            if data.find('div',{"class":"product-ripley-price"}):
                ripley = data.find('div',{"class":"product-ripley-price"}).text.strip("Tarjeta Ripley o Chek")
            else:
                ripley = 0
            send = True
            break
        except Exception as error:
            print(error)
            delay(1)
    print(send)
    
    """resultado=data.find('section',{"class":"jsx-1944012472"})
    i=1
    DESCRIPCION=""
    for tabla in resultado.find_all('tr',{"class":"jsx-428502957"}):
        for dato in tabla.find_all('td',{"class":"jsx-428502957"}):
            DESCRIPCION+=dato.text+" "
        DESCRIPCION+="%0A" """

    #url=SERVIDOR+"/set.php?ID="+ID+"&Marca="+BRAND+"&Nombre="+NAME.replace(" ","%20")+"&Precio="+PRECIO+"&Precio2="+PRECIO2+"&Precio3="+PRECIO3+"&Descripcion="+DESCRIPCION.replace(" ","%20")+"&Categoria="+CATEGORIA+"&Url="+pagina+"&Tienda=Falabella"
    #url=url.replace("á","%C3%A1").replace("é","%C3%A9").replace("í","%C3%AD").replace("ó","%C3%B3").replace("ú","%C3%BA").replace("ñ","%C3%B1")

    #print(url)

def changePage(links):
    n=0
    for link in links:
        print(link)
        for i in range(9,999):
            urlCategory = link + str(i)
            driver.get(urlCategory)
            WebDriverWait(driver, 2)
            print(i)
            body = driver.execute_script("return document.body")
            source = body.get_attribute('innerHTML')
            data = b(source, "html.parser")
            if data.find('section',{"class":"catalog-grid"}):
                for linkProduct in data.find_all('a',{"class":"catalog-product-item"}):
                    n+=1
                    if linkProduct:
                        brand = linkProduct.find('div', {"class":"brand-logo"}).text
                        linkProducts = 'https://simple.ripley.cl' + linkProduct["href"] + '?&s=mdco'
                        print(linkProducts)
                        extractData(linkProducts,brand)
                        print(n)
                    else:
                        print("página no encontrada")
            else:
                break


def extractCategoryLink(url):
    driver2.get(url)
    menu = driver2.find_element_by_xpath('//div[@class="menu-button"]')
    menu.click()
    delay(1)
    links = []
    categories = driver2.find_element_by_xpath('//div[@class="tree-node-items"]')
    for category in categories.find_elements_by_tag_name('a'):
        try:
            category.click()
            delay(1)
            for subcategories in driver2.find_elements_by_xpath('//ul[@class="category-tree__expanded-category"]'):
                subcategory = subcategories.find_element_by_tag_name('a').get_attribute('href') + '&page='
                links.append(subcategory)
            back = driver2.find_element_by_xpath('//a[@class="tree-node-back-button"]')
            back.click()
            delay(1)
        except:
            print('done')
    changePage(links)
    driver2.close()


url = 'https://simple.ripley.cl'

while True:
    extractCategoryLink(url)

driver.close()