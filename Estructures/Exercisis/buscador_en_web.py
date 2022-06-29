#!/usr/bin/python3
# _*_ coding: utf-8 _*_
from bs4 import BeautifulSoup
import requests
__author__ = "Santiago Pastor Serrano"
__email__ = "cf19santiago.pastor@iesjoandaustria.org"
__license__ = "GPL V3"
"""
Aquest programa busca en una pàgina web una informàcio específica
"""


def main():
    url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
    web = (requests.get(url))
    if web.ok:
        sopa_web = BeautifulSoup(web.text, "html.parser")
        Articulo_destacado = (sopa_web.find(id="Artículo_destacado")).parent
        Articulo_bueno = (sopa_web.find(id="Artículo_bueno")).parent
        print((Articulo_destacado.find(class_="mw-headline")).text)
        print((Articulo_bueno.find(class_="mw-headline")).text)
    else:
        print("Alguna cosa ha anat malament llegint la web." +
              str(web.status_code) + ":" + web.reason)


if __name__ == "__main__":
    main()
