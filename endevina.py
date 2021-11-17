#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import random

"""
endevina.py tria un número a l'atzar entre l'1 i el 10 i l'usuari l'ha d'endevinar.
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"

def main(numero_secret):
    """
    Dona pistes a l'usuari per a que pugui endevinar el nombre secret que la funció rep com a paràmetre.
    """
    es_endevinat = False
    suposicio_usuari = None
    while True:
        suposicio_usuari = int(input("Quin número entre 1 i 10 he pensat? "))
        if suposicio_usuari < numero_secret:
            print("El número secret és més gran que ", suposicio_usuari, ", torna a intentar-ho!")
        elif suposicio_usuari > numero_secret:
            print("El número secret és més petit que ", suposicio_usuari, ", torna a intentar-ho!")
        elif suposicio_usuari == "":
            print("Sento que t'hagis donat per vençut tan ràpid, el número secret era el ", numero_secret)
            quit
        else:
            print("Felicitats, l'has encertat era el", numero_secret,"!!!")
        # print(f"El número secret és més petit que {suposicio_usuari}, torna a intentar-ho!")
        # print(f"El número secret és més gran que {suposicio_usuari}, torna a intentar-ho!")
        # print(f"Felicitats, l'has encertat era el {numero_secret}!!!")
        # print(f"Sento que t'hagis donat per vençut tan ràpid, el número secret era el {numero_secret}")

if __name__ == "__main__":
    # Passem un nombre aleatori a la funció principal.
    main(random.randrange(1, 11, 1))