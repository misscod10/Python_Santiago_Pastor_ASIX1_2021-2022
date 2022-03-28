#!/bin/python3
# -*- coding: utf-8 -*-
__author__="Santiago Pastor Serrano"
import re
def main():
    while(True):
        linia = input()
        regular="([^@]+@[^@]+\.[a-zA-Z]{2,})" 
        busqueda = re.search(regular, linia)
        if busqueda:
            print(busqueda.group(1))

if __name__=="__main__":
    try:
        main()
    except EOFError:
        pass
