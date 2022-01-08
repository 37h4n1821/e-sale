import sys
from pathlib import Path

ruta=str(Path(__file__).absolute())
ruta=ruta.replace("\\","/")
ruta=ruta.replace(ruta.split("/")[-2]+"/"+ruta.split("/")[-1],"")

sys.path.append(ruta)

from Global.imports import *

def escribir(txt):
    wr=open("falabella.html","w")
    wr.write(txt)
    wr.close()

def extraerdatos(pagina):
    data = requests.get(pagina)
    data=data.content
    data=b(data,"lxml")
    resultado2=data.find('ol',{"class":"Breadcrumbs-module_breadcrumb__3lLwJ"})
    CATEGORIA=""
    for navegador in resultado2.find_all("li"):
        texto=navegador.find("a")
        if texto.text!="Home":
            CATEGORIA+=texto.text+";"
    resultado=data.find('span',{"class":"jsx-3408573263"})
    ID=resultado.text.strip("Código del producto: ")

    Nombre=data.find('div',{"class":"product-name"}).text
    Marca=data.find('a',{"class":"product-brand-link"}).text
    print(Nombre)
    PRECIO=""
    PRECIO2=""
    PRECIO3=""

    #print(PRODUCTO)

    try:
        resultado=data.find('li',{"class":"price-2"})
        if 'data-normal-price' in str(resultado):
            PRECIO3=resultado['data-normal-price'].replace(".","")
            #print("normal",PRECIO3)

        if 'data-internet-price' in str(resultado):
            PRECIO2=resultado['data-internet-price'].replace(".","")
            #print("internet",PRECIO2)

        if 'data-cmr-price' in str(resultado):
            PRECIO=resultado['data-cmr-price'].replace(".","")
            #print("cmr",PRECIO)

    except:
        PRECIO2=""

    try:
        resultado=data.find('li',{"class":"price-1"})
        if 'data-normal-price' in str(resultado):
            PRECIO3=resultado['data-normal-price'].replace(".","")
            PRECIO=""
            #print("normal",PRECIO3)

        if 'data-internet-price' in str(resultado):
            PRECIO2=resultado['data-internet-price'].replace(".","")
            #print("internet",PRECIO2)

        if 'data-cmr-price' in str(resultado):
            PRECIO=resultado['data-cmr-price'].replace(".","")
            #print("cmr",PRECIO)

    except:
        PRECIO2=""

    try:
        resultado=data.find('li',{"class":"price-0"})
        if 'data-normal-price' in str(resultado):
            PRECIO3=resultado['data-normal-price'].replace(".","")
            PRECIO=""
            PRECIO2=""
            #print("normal",PRECIO3)

        if 'data-internet-price' in str(resultado):
            PRECIO2=resultado['data-internet-price'].replace(".","")
            PRECIO=""
            #print("internet",PRECIO2)

        if 'data-cmr-price' in str(resultado):
            PRECIO=resultado['data-cmr-price'].replace(".","")
            #print("cmr",PRECIO)

    except:
        PRECIO=""
    
    

    resultado=data.find('section',{"class":"jsx-1944012472"})
    i=1
    DESCRIPCION=""
    for tabla in resultado.find_all('tr',{"class":"jsx-428502957"}):
        for dato in tabla.find_all('td',{"class":"jsx-428502957"}):
            DESCRIPCION+=dato.text+" "
        DESCRIPCION+="%0A"

def changePage(links):
    n=0
    for link in links:
        print(link)
        for i in range(1,999):
            urlCategory = link + str(i)
            driver.get(urlCategory)
            WebDriverWait(driver, 2)
            print(i)
            body = driver.execute_script("return document.body")
            source = body.get_attribute('innerHTML')
            data = b(source, "html.parser")





def extractCategoryLink(url):
    driver2.get(url)
    menu = driver2.find_element_by_xpath('//span[@class="MarketplaceHamburgerBtn-module_title__2KG47"]')
    menu.click()
    delay(1)
    links=[]
    categories = driver2.find_elements_by_xpath('//div[@class="TaxonomyDesktop-module_categoryWrapper__3YBaF"]')
    for category in categories:
        try:
            category.click()
            delay(1)
            subcategories = driver2.find_element_by_xpath('//div[@class="SecondLevelCategories-module_secondLevelMenuItemsBox__2i00Y"]')
            for subcategory in subcategories.find_elements_by_tag_name('a'):
                if not 'collection' in subcategory.get_attribute('href'):
                    links.append(subcategory.get_attribute('href') + '?page=')
                    print(subcategory.get_attribute('href'))
            delay(1)
        except:
            print('done')
    changePage(links)
            
url = 'https://www.falabella.com/falabella-cl/category/cat2018'

while True:
    extractCategoryLink(url)

driver.close()