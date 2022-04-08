#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
__author__="Santiago Pastor Serrano"
COLUMNAS=13
def main():
    simbolos={"cor":"\U00002665","diamant":"\U000025C6","pica":"\U00002660","trevol":"\U00002663"}
    ma=[]
    pal=["cor","diamant","pica","trevol"]
    n="Q"
    pq = [ 
    " ___ ", 
    "|Q  |", 
    "| " + simbolos["pica"] + " |", 
    "|__Q|" 
    ]

    As = [ 
    " ___ ", 
    "|A  |", 
    "| " + simbolos["cor"] + " |", 
    "|__A|" 
    ]
    
    ut = [ 
    " ___ ", 
    "|1  |", 
    "| " + simbolos["trevol"] + " |", 
    "|__1|" 
    ]

    cd = [ 
    " ___ ", 
    "|5  |", 
    "| " + simbolos["diamant"] + " |", 
    "|__5|" 
    ]
    carta_generada=genera_carta(n,pal[1],simbolos) 
    ma=[cd,ut,As,pq,carta_generada]
    imprimir_mano(ma)
    baralla=genera_baralla(pal,simbolos)
    imprimir_mano(baralla)
    baralla=mezclar(baralla)
    imprimir_mano(baralla)
    
def imprimir_mano(ma):
    if len(ma)>COLUMNAS:
        imprimir_mano(ma[:-COLUMNAS])
    for indice in range(4):
        linea=""
        for carta in ma[-COLUMNAS:]:
            linea+= carta[indice]
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

if __name__=="__main__":
    main()
