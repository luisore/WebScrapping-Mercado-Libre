# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:21:26 2024

@author: ricar
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse



base_url = "https://listado.mercadolibre.com.ar"
busqueda_url = "/relojes-hombre#D[A:relojes hombre,L:undefined]"

item = 1
maximo = 100

while busqueda_url and item <= maximo:
    respuesta = requests.get(base_url + busqueda_url)
    data = BeautifulSoup(respuesta.content,"html.parser")
        
    buscar_resultados = data.find_all("div", class_="ui-search-result__wrapper")

    for resultado in buscar_resultados:
        texto = resultado.find("h2")
        precio = resultado.find("span", class_ = "andes-money-amount__fraction")
        print (f"Producto {item}")
        print(f"Titulo:{texto.text.strip()}")
        print(f"Precio: {precio.text.strip()}\n")
        item += 1        
    
    
    siguiente_link = data.find("a", class_ = "andes-pagination__link")
    
    print(siguiente_link)
    if siguiente_link:
        busqueda_url = urlparse(siguiente_link.get("href")).path
    else:
        busqueda_url = None



