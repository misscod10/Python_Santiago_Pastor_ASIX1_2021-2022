#!/bin/python3
import os, pandas
__author__="Santiago Pastor Serrano"

PATH_DADES = "./dades.csv"


def main():
    option=None
    while option !=0:
        if option != None:
            os.system("clear")  
            choose(option)
        option=print_menu()
    print("Sortint del programa ...")
    

def print_menu():
    option=int(input("\n0: Sortir del programa\n1: Introduir dades noves\n2: Mostrar dades guardades\n Introdueix l'opció escollida: "))
    return option


def choose(option):
    options={0:"Sortir",1:"Introduir",2:"Mostrar"}
    if options[option]=="Introduir":
        escriptura()
    if options[option]=="Mostrar":
        mostrar()
    if options[option]=="Sortir":
        pass
    else:
        print("Escogeix una opció vàlida")


def escriptura():
    global PATH_DADES
    noms=[]
    cognoms=[]
    dni=[]
    neixement=[]
    telefon=[]
    quants=int(input("Quants usuaris vol afegir? \n"))
    for i in range(quants):
        print("------------------------------------------------------")
        noms.append(input("Nom de l'usuari: "))
        cognoms.append(input("Cognoms de l'usuari: "))
        dni.append(input("DNI de l'usuari: "))
        neixement.append(input("Data de neixement de l'usuari: "))
        telefon.append(input("Telefon de l'usuari: "))
         
    dades={"Noms":noms, "Cognoms":cognoms, "DNI":dni, "Neixement":neixement, "Telefon":telefon}
    document= pandas.DataFrame(dades, columns=["Noms","Cognoms","DNI","Neixement","Telefon"])
    document.to_csv(PATH_DADES)

def mostrar():
    global PATH_DADES
    archivo=pandas.read_csv(PATH_DADES)
    print(archivo)

if __name__=="__main__":
    main()
