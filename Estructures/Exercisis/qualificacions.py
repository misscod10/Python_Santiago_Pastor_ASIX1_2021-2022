#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys

"""
qualificacions.py demana noms de mòduls i nota. Al final calcula nota mitja de cicle.
"""
__author__   = "Santiago Pastor Serrano"

def main():
    """
    Funció principal: rep els noms i les qualificacions dels mòduls i 
    retorna la nota mitja.
    """
    nom_modul = None
    nota_acumulada = 0
    comptador_de_moduls = 0
    while nom_modul != "":
        nom_modul=input("Nom del mòdul: ")
        if nom_modul!="":
            comptador_de_moduls+=1
            nota_acumulada=nota_acumulada+float(input("Nota del mòdul: "))


    """
    Amb les següents líneas el programa calcula la mitjana
    """
    

    if comptador_de_moduls != 0:
        return nota_acumulada / comptador_de_moduls
    return None

if __name__ == "__main__":
    print(main())