import sys
from pathlib import Path

ruta=str(Path(__file__).absolute())
ruta=ruta.replace("\\","/")
ruta=ruta.replace(ruta.split("/")[-2]+"/"+ruta.split("/")[-1],"")

sys.path.append(ruta)

from Global.imports import *



url="https://www.falabella.com/falabella-cl/category/{cate}{categoria}?page="