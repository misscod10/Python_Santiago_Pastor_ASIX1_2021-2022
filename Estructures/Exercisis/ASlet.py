#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__="Santiago Pastor Serrano"
__email__="cf19santiago.pastor@iesjoandaustria.org"

import os
import sys
"""
Aquest programa et permet introduir una paraula i després fa que la adivinis.
"""
def main():
    opcio=None
    while opcio!="0":
        mostrar_menu()
        opcio=input("Introdueix opció escollida ")
        if opcio == "1":
           paraula_secreta=entrar_paraula_secreta()
        if opcio ==  "2":
            endevinar_paraula(paraula_secreta)
def mostrar_menu():
    print("0. Sortir de la aplicació \n1. Entrar paraula secreta\n2. Endevinar paraula secreta")

def entrar_paraula_secreta():
    """
    Aquesta funció fa un input amb la paraula secreta que anem a utilitzar i comprova que sigi de 5 lletres, si no ho és et torna a demanar l'input. 
    Si si que te 5 lletres esborra la pantalla amb un clear(en linux) i retorna la paraula introduïda
    """
    correcto=0
    while correcto==0:
        paraula_posible=input("Introdueix la paraula secreta: ")
        if len(paraula_posible)==5:
            paraula_secreta=paraula_posible
            correcto=1
            os.system("clear")
        else:
            print("La paraula ha de ser de, com a minim, 5 lletres!\nTorna a intentar-ho:\n")
    return paraula_secreta

def endevinar_paraula(paraula_secreta):
    """
    Aquesta funció et demana un input per introduir una paraila per després comprobar que has encertat la paraula secreta, si es que sí t'ho diu per pantalla i et retorna al menú. 
    Si es que no comproba cada lletra per saber si esta o no en la paraula secreta,si està comprova si esta en la mateixa posicio o no. Després ho representa amb símbols 
    i imprimeix per pantalla tant la paraula com els simbols i et demana tornar a intentar-lo.
    """
    correcto=0
    while correcto==0:
        representació_símbols=("")
        paraula_posible=input("Introdueix la paraula que creus que és la paraula secreta: ")
        if len(paraula_posible)==5:
            if paraula_posible==paraula_secreta:
                print("\nHas encertat la paraula!\n")
                correcto=1
            else:
                for z in range(len(paraula_secreta)):
                    if paraula_posible[z] in paraula_secreta:
                        if paraula_posible[z]==paraula_secreta[z]:
                            representació_símbols=representació_símbols+("V")
                        else:
                            representació_símbols=representació_símbols+("O")
                    else:
                        representació_símbols=representació_símbols+("X")
                print(paraula_posible)
                print(representació_símbols)
        else:
            print("La paraula ha de ser de, com a minim, 5 lletres!\n")
if __name__=="__main__":
    main()
