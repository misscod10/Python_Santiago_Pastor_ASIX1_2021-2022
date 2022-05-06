#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import os, pandas

__author__="Santiago Pastor Serrano"
__email__="cf19santiago.pastor@iesjoandaustria.org"
PATH_DADES = "./dades.csv"

"""
Aquest programa imprimeix un menú amb les opcions per sortir del programa, escriure en un archiu .csv els usuaris amb les seves dades i imprimir per pantalla una taula amb les dades inscrites en l'archiu.
He escollit utilitzar un archiu .csv perqué hem sembla el més 'Natural' per guardar aquestos tipus de dades i perqué vaig descobrir la llibreria pandas que m'ho imprimia d'una manera més estètica.
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


def escriptura(noms,cognoms,dni,neixement,telefon):
    global PATH_DADES 
    quants=int(input("Quants usuaris vol afegir? \n"))
    os.system("clear")
    for i in range(quants):
        print("------------------------------------------------------")
        dni_user=input("DNI de l'usuari: ")
        if dni_user in dni:
            print("\nJa hi ha un usuari amb el mateix DNI, sobrescribint les dades de l'usuari...\n")
            dni[dni.index(dni_user)]=dni_user
            noms[dni.index(dni_user)]=input("Nom de l'usuari: ")
            cognoms[dni.index(dni_user)]=input("Cognoms de l'usuari: ")
            neixement[dni.index(dni_user)]=input("Data de neixement de l'usuari: ")
            telefon[dni.index(dni_user)]=input("Telefon de l'usuari: ")
        else:
            dni.append(dni_user)
            noms.append(input("Nom de l'usuari: "))
            cognoms.append(input("Cognoms de l'usuari: ")) 
            neixement.append(input("Data de neixement de l'usuari: "))
            telefon.append(input("Telefon de l'usuari: "))
         
    dades={"Noms":noms, "Cognoms":cognoms, "DNI":dni, "Neixement":neixement, "Telefon":telefon}
    document= pandas.DataFrame(dades)
    document.to_csv(PATH_DADES, index=False)
    return  noms, cognoms, dni, neixement, telefon


def mostrar():
    global PATH_DADES
    archivo=pandas.read_csv(PATH_DADES)
    print(archivo)


if __name__=="__main__":
    main()
