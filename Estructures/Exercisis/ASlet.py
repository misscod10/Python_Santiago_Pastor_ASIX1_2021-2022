#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__="Santiago Pastor Serrano"
__email__="cf19santiago.pastor@iesjoandaustria.org"

import os
import sys
"""
heu de programar una aplicació que mostri el següent menu:

0. Sortir de la aplicació

1. Entrar paraula secreta

2. Endevinar paraula secreta

Amb entrar paraula secreta la aplicació demanarà una paraula de 5 lletres i ha de comprovar que la paraula és de 5 lletres, ni menys ni més.
Desprès de demanar la paraula ha d'esborrar la terminal per a que no es vegi quina paraula hem proporcionat.
Un cop que tenim la paraula secreta si triem la opció 2 (Endevinar paraula secreta), li demanarem al usuari que endevini la paraula secreta.
Si la paraula introduïda per l'usuari té més de 5 o menys de 5 lletres, li hem de recordar que ha d'introduïr paraules de exactament 5 lletress.
Si la paraula introduïda és la paraula secreta li hem de comunicar que l'ha endevinat.
En altre cas, has de mostrar la paraula introduïda per l'usuari i just a sota d'aquesta paraula heu de escriure 5 símbols, un per cada lletra:
V si la lletra que coincideix en posició coincideix amb la de la paraula secreta.
X si la lletra que coincideix en posició no es troba a la paraula secreta.
O si la lletra que coincideix en posició és a la paraula secreta, però no en aquella posició.
Exemple:
Si la paraula secreta és: GRUTA i l'usuari entra GATET, el programa ha d'escriure:

G A T E T
V O O X O
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
