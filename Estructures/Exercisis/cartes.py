#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
__author__="Santiago Pastor Serrano"

def main():
    simbolos={"cor":"\U00002665","diamant":"\U000025C6","pica":"\U00002660","trevol":"\U00002663"}
    ma=[]
    pal="cor"
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
    carta_generada=genera_carta(n,pal,simbolos) 
    ma=[cd,ut,As,pq,carta_generada]
    imprimir_mano(ma)

def imprimir_mano(ma):
    for indice in range(4):
        linea=""
        for carta in ma:
            linea+= carta[indice]
        print(linea)


def genera_carta(n, pal, simbolos):
    carta_generada=[ 
    " ___ ", 
    "|"+ n.ljust(3," ") +  "|", 
    "| " + simbolos[pal] + " |", 
    "|"+ n.rjust(3,"_")+"|" 
    ]  
    return carta_generada

if __name__=="__main__":
    main()
