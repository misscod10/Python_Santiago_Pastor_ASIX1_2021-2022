#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
__author__="Santiago Pastor Serrano"
"""
Aquest programa ens pregunta inputs i ens retorna el mateix que li escribim sense parar fins que l'usuari fa un input buit
"""
def main():
    frase_de_l_usuari = None
    while frase_de_l_usuari!="":
        frase_de_l_usuari=input("L'usuari diu: ") 
        if frase_de_l_usuari !="":
            print("El lloro repeteix: ",frase_de_l_usuari)
if __name__=='__main__':
    main()