#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
qualitat_del_aire.py

Programa que fa consultes a l'API de mesures automàtiques de contaminants de l'aire a Catalunya

Components del grup:
    - Santiago Pastor Serrano
    - Maria Adame
    - Oscar Gonzalez

https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json
"""

import requests
import json

def getNomContaminant(contaminant):
    """
    >>> getNomContaminant("O3")
    'Ozò'
    >>> getNomContaminant("CO")
    'Monòxid de carboni'
    >>> getNomContaminant("PM3")
    ''
    """
    noms_contaminants = {"O3": "Ozò", "PM10": "Partícules menors 10 micròmetres", 
                        "NO2": "Diòxid de nitrògen", "NO": "Òxid de nitrògen", "NOX": "Òxids de nitrògen", 
                        "SO2": "Diòxid de Sofre", "CO": "Monòxid de carboni"}
    try:
        return noms_contaminants[contaminant]
    except:
        return ""


def print_dada(dada):
    print(f"|--- Estació: {dada['nom_estacio']}")
    print(f"|->    magnitud: {dada['magnitud']}")
    print(f"|->    contaminant: {dada['contaminant']}: {getNomContaminant(dada['contaminant'])}")
    print(f"|->    unitats: {dada['unitats']}")
    print(f"|->    data: {dada['data']}")
    print()

def mostra_menu():
    print(" 0.- Surt de l'aplicació \n 1.- Filtra per municipi \n 2.- Filtra per contaminant \n 3.- Mostra dades filtrades, esborra filtres i refresca dades")

def procesa_opcio(opcio,dades):
    if opcio=="1":
        municipi = input("Introdueix municipi a filtrar: ")
        dades = list(filter(lambda x: x["municipi"].lower() == municipi,dades)) 
    if opcio=="2":
        contaminant=input("Escogeix contaminant a filtrar: ")
        dades = list(filter(lambda x: x["contaminant"].lower() == contaminant,dades))
    if opcio=="3":
        for dada in dades:
            print_dada(dada)
            dades=requests.get("https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json").json()
    return dades

    
def main():
    dades = requests.get("https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json").json()
    for dada in dades:
        print_dada(dada)
    opcio=None
    while opcio !="0":
        mostra_menu()
        opcio=input("Tria una opcio: ")
        if opcio != "0":
            dades=procesa_opcio(opcio,dades)


if __name__ == "__main__":
    main()
