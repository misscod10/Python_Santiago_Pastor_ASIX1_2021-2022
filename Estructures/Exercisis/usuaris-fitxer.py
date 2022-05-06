#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import os, pandas
from textwrap import indent

from pandas.core import indexing

__author__="Santiago Pastor Serrano"
__email__="cf19santiago.pastor@iesjoandaustria.org"
PATH_DADES = "./dades.csv"

"""
Aquest programa imprimeix un menú amb les opcions per sortir del programa, escriure en un archiu .csv els usuaris amb les seves dades i imprimir per pantalla una taula amb les dades inscrites en l'archiu.
"""


def main():
    option=None
    noms=[]
    cognoms=[]
    dni=[]
    neixement=[]
    telefon=[]

    while option !=0:
        if option != None:
            os.system("clear")  
            choose(option, noms, cognoms, dni, neixement, telefon)
        option=print_menu()
    print("Sortint del programa ...")
    

def print_menu():
    option=int(input("\n0: Sortir del programa\n1: Introduir dades noves\n2: Mostrar dades guardades\n Introdueix l'opció escollida: "))
    return option


def choose(option, noms, cognoms, dni, neixement, telefon):
    options={0:"Sortir",1:"Introduir",2:"Mostrar"}
    if options[option]=="Introduir":
        noms, cognoms, dni, neixement, telefon=escriptura(noms, cognoms, dni, neixement, telefon)
    if options[option]=="Mostrar":
        mostrar()
    if options[option]=="Sortir":
        pass
    else:
        print("\nEscogeix una opció vàlida")


def escriptura(noms,cognoms,dni,neixement,telefon):
    global PATH_DADES 
    quants=int(input("Quants usuaris vol afegir? \n"))
    os.system("clear")
    for i in range(quants):
        print("------------------------------------------------------")
        noms.append(input("Nom de l'usuari: "))
        cognoms.append(input("Cognoms de l'usuari: "))
        dni.append(input("DNI de l'usuari: "))
        neixement.append(input("Data de neixement de l'usuari: "))
        telefon.append(input("Telefon de l'usuari: "))
         
    dades={"Noms":noms, "Cognoms":cognoms, "DNI":dni, "Neixement":neixement, "Telefon":telefon}
    document= pandas.DataFrame(dades, columns=["Noms","Cognoms","DNI","Neixement","Telefon"])
    document.to_csv(PATH_DADES, index=False)
    return  noms, cognoms, dni, neixement, telefon


def mostrar():
    global PATH_DADES
    archivo=pandas.read_csv(PATH_DADES)
    print(archivo)


if __name__=="__main__":
    main()
