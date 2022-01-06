import sys
from pathlib import Path

ruta=str(Path(__file__).absolute())
ruta=ruta.replace("\\","/")
ruta=ruta.replace(ruta.split("/")[-2]+"/"+ruta.split("/")[-1],"")

sys.path.append(ruta)

from Global.imports import *


def extraerdatos(pagina):
    data = requests.get(pagina)
    data=data.content
    data=b(data,"lxml")
    resultado2=data.find('ol',{"class":"Breadcrumbs-module_breadcrumb__3lLwJ"})
    for navegador in resultado2.find_all("li"):
        CATEGORIA=navegador.find("a")
        CATEGORIA=CATEGORIA.text.replace(" ","%20")
    resultado=data.find('span',{"class":"jsx-3408573263"})
    ID=resultado.text.strip("Código del producto: ")

    NAME=data.find('div',{"class":"product-name"}).text
    BRAND=data.find('a',{"class":"product-brand-link"}).text
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

    url="http://villaloscisnesnavidad.epizy.com/set.php?ID="+ID+"&Marca="+BRAND+"&Nombre="+NAME.replace(" ","%20")+"&Precio="+PRECIO+"&Precio2="+PRECIO2+"&Precio3="+PRECIO3+"&Descripcion="+DESCRIPCION.replace(" ","%20")+"&Categoria="+CATEGORIA+"&Url="+pagina+"&Tienda=Falabella"
    url=url.replace("á","%C3%A1").replace("é","%C3%A9").replace("í","%C3%AD").replace("ó","%C3%B3").replace("ú","%C3%BA").replace("ñ","%C3%B1")

    #print(url)
    driver.get(url)


def extract(url):
    driver.get(url)
    WebDriverWait(driver, 2)

    #print("Entro!")

    body = driver.execute_script("return document.body")
    source = body.get_attribute('innerHTML')
    soup = b(source, "html.parser")
     
    i=0
    if soup.find_all('a',{"class":"jsx-4221770651"}) or soup.find_all('a',{"class":"jsx-3128226947"}) or soup.find_all('a',{"class":"jsx-4001457643"}) or soup.find_all('a',{"class":"jsx-2764557706"}):
        try:
            for dat in soup.find_all('a',{"class":"jsx-4221770651"}):
                i+=1
                extraerdatos(dat["href"])
                print(i)
        except Exception as e:
            print(e)
            print("Modo 1 no funciono")

        try:
            for dat in soup.find_all('a',{"class":"jsx-2764557706"}):
                i+=1
                extraerdatos(dat["href"])
                print(i)
        except Exception as e:
            print(e)
            print("Modo 2 no funciono")
        try:
            for dat in soup.find_all('a',{"class":"jsx-3128226947"}):
                i+=1
                extraerdatos(dat["href"])
                print(i)
        except Exception as e:
            print(e)
            print("Modo 3 no funciono")

        try:
            for dat in soup.find_all('a',{"class":"jsx-4001457643"}):
                i+=1
                extraerdatos(dat["href"])
                print(i)
        except Exception as e:
            print(e)
            print("Modo 4 no funciono")

        
        return True
    else:
        return False

def extraer_all(url,n):
    i=n
    try:
        for i in range(n,999):
            print(i)
            print("Categoria: "+url.strip("https://www.falabella.com/falabella-cl/category/cat")+str(i))
            url2=url+str(i)

            if not extract(url2):
                break
    finally:
        return i

def leer_ant():
    data=None
    if os.path.exists("estado.json"):
        with open("estado.json", "r") as read_file:
            data = json.load(read_file)
        #os.remove("estado.json")
    return data

def categoria(url):
    data_=leer_ant()
    try:
        for cat in ["cat","CATG"]:
            n=1
            n2=1
            if data_:
                cat=data_["CAT"]
                n=data_["N_CAT"]
                n2=data_["N_Page"]
            for i in range(n,9999999999):
                for i2 in range(4):
                    data={"CAT":cat,"N_CAT":i,"N_Page":1}
                    url2=url.format(cate=cat,categoria=i)
                    print(url2)

                    driver.get(url2+str(1))
                    WebDriverWait(driver, 2)

                    body = driver.execute_script("return document.body")
                    source = body.get_attribute('innerHTML')
                    respuesta = b(source, "html.parser")

                    

                    if respuesta.find_all('a',{"class":"jsx-4221770651"}) or respuesta.find_all('a',{"class":"jsx-3128226947"}) or respuesta.find_all('a',{"class":"jsx-4001457643"}) or respuesta.find_all('a',{"class":"jsx-2764557706"}):
                        print("Existe:",url2,"Pag",i)
                        N_page=extraer_all(url2,n2)
                        data["N_Page"]=N_page
                        n2=1
                        break
                    else:
                        print("Not Found:",cat,"Pag",i)
                delay(0.01)
            if data_:
                data_=None
            
                
    except:
        with open("estado.json", "w") as write_file:
            json.dump(data, write_file)
            


url="https://www.falabella.com/falabella-cl/category/{cate}{categoria}?page="

url = 'https://simple.ripley.cl/tecno/celulares?source=menu&s=mdco'

data = requests.get(url)
data=data.content
data=b(data,"lxml")
for product in data.find_all('a',{"class":"catalog-product-item"}):
        brand = product.find('div', {"class":"brand-logo"}).text
        name = product.find('div', {"class":"catalog-product-details__name"}).text
        link = product["href"]
        print(brand)
        print(name)
        print('https://simple.ripley.cl' + link + '?&s=mdco')

while True:
    categoria(url)

driver.close()