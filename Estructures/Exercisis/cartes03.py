#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import doctest
import random
__author__="Santiago Pastor Serrano"
COLUMNAS=13


def main():
    simbolos={"cor":"\U00002665","diamant":"\U000025C6","pica":"\U00002660","trevol":"\U00002663"}
    pal=["cor","diamant","pica","trevol"]
    baralla=genera_baralla(pal,simbolos)
    baralla=especial(baralla) 
    imprimir_menu(baralla)



def imprimir_mano(ma):
    if len(ma)>COLUMNAS:
        imprimir_mano(ma[:-COLUMNAS])
    for indice in range(4):
        linea=""
        for carta in ma[-COLUMNAS:]:
            linea+=carta[indice]
        print(linea)


def genera_carta(n, pal, simbolos):
    carta_generada=[ 
    " ___ ", 
    "|"+ str(n).ljust(3," ") +  "|", 
    "| " + simbolos[pal] + " |", 
    "|"+ str(n).rjust(3,"_")+"|" 
    ] 
    return carta_generada


def genera_baralla(pal,simbolos):
    baralla=[]
    for i in pal:
        for x in range(2,11):
            carta_generada=genera_carta(x,i,simbolos)
            baralla.append(carta_generada)
        for y in ("J","Q","K","A"):
            carta_generada=genera_carta(y,i,simbolos)
            baralla.append(carta_generada)
    return baralla
        
def mezclar(baralla):
    metodos={1:lambda x:randomizar(x), 2:lambda x:mitades(x), 3:lambda x:especial(x)}
    metodo=int(input("Con que método quieres mezclar las cartas?\n\n1. Todo random\n2. Por mitades\n3. Especial\n"))
    resultat=metodos.get(metodo, lambda x : None)(baralla)
    return resultat


def randomizar(baralla):
     resultat=[] 
     for i in range(len(baralla)):
          resultat.append(baralla[i])
     for i in range(len(resultat)):
        origen=random.randint(0,len(resultat)-1)
        destí=random.randint(0,len(resultat)-1)
        resultat[origen], resultat[destí]= resultat[destí], resultat[origen]
     return resultat


def mitades(baralla):
    resultat=[]
    meitat1=[]
    meitat2=[]
    for i in range(0,len(baralla)//2):
        meitat1.append(baralla[i])
    for x in range(len(baralla)//2,len(baralla)):
        meitat2.append(baralla[x])
    meitat1=randomizar(meitat1)
    meitat2=randomizar(meitat2)
    for z in range(len(baralla)//2):
        resultat.append(meitat1[z])
        resultat.append(meitat2[z])
    return resultat


def especial(baralla):
    resultat=baralla
    for i in range(3):
        paso1=mitades(resultat)
        resultat=randomizar(paso1)
    return resultat



def get_valor_carta(carta):
    valor=carta[1].strip("|")
    valor=valor.strip()
    if valor.isdigit()==True:
        return int(valor)
    if valor=="A":
        return 11
    else:
        return 10

def get_valors_ma(ma):
    valors=[]
    for b in ma:
        valors.append(get_valor_carta(b))
    valor_cartas=suma_valors_ma(valors)
    return valor_cartas

def suma_valors_ma(valors):
    """
    · Utilitzar la funció reduce.
    · No modificar el contingut del paràmetre d'entrada valors.
    >>> suma_valors_ma([2, 10, 5])
    17
    >>> suma_valors_ma([2, 10, 11])
    13
    >>> suma_valors_ma([11, 10, 2])
    13
    >>> suma_valors_ma([11, 10])
    21
    >>> suma_valors_ma([10, 11])
    21
    >>> suma_valors_ma([11, 11])
    2
    """
    suma=sum(valors)
    if suma > 21:
        for r in range(len(valors)):
            if valors[r] == 11:
                valors[r] = 1
        suma=sum(valors)
        return suma
    return suma


def imprimir_menu(baralla):
    opciones={"0":"Sortir","1":"Demana","2":"Plantarse","3":"Reinicia"}
    respuesta=None
    ma=[] 
    guanyador=None
    while respuesta != "0":
        if respuesta=="3":
            guanyador=None
        imprimir_mano(ma)
        valors=get_valors_ma(ma)
        print(valors)
        if guanyador !=None:
            escollir_guanyador(guanyador)
        respuesta=input("\n0. Sortir\n1. Demanar més cartes\n2. Plantarse\n3. Reinicia el joc\n\n")
        if opciones[respuesta]=="Demana":
            os.system("clear")
            demanar_carta(ma,valors,baralla)
        if opciones[respuesta]=="Plantarse":
            os.system("clear") 
            guanyador=plantarse(valors,baralla)
        if opciones[respuesta]=="Reinicia":
            os.system("clear")
            ma=[]
    print("\nSortint del programa...\n")


def demanar_carta(ma,valors,baralla):
    if valors<21:
        ma.append(baralla.pop())
    else:
        print("No és poden demanar més cartes!")
    return ma


def plantarse(valors,baralla):
   #Maquina=1 Jugador=0 
    if valors==21:
        guanyador=0
        return guanyador
    if valors>21:
        guanyador=1
        return guanyador
    ma_maquina,valors_maquina=banca(baralla)
    imprimir_mano(ma_maquina)
    print(valors_maquina)
    if valors>21:
        guanyador=1
        return guanyador
    if valors_maquina>21:
        guanyador=0
        return guanyador
    else:
        if valors_maquina > valors:
            guanyador=1
            return guanyador
        if valors > valors_maquina:
            guanyador=0
            return guanyador


def banca(baralla):
    ma=[]
    valors=0
    while valors < 17:
        ma=(demanar_carta(ma,valors,baralla))
        valors=get_valors_ma(ma)
    return ma, valors

def escollir_guanyador(guanyador):
    if guanyador==0:
        print("\nHas guanyat!\nFelicitats")
    else:
        print("Guanya la Banca!")

if __name__=="__main__":
    main()
