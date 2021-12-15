#!/usr/bin/python3
# _*_ coding: utf-8 _*_
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
"""
Aquest programa agafa els números intégers que li donem a través d'un input que es repeteix fins que rep un número negatiu. Després ordena els nomeros donats de mes petit a més gran i imprimeix el resultat per pantalla.
"""
def main():
    vector_valors=[]
    nombre_usuari=0
    while(nombre_usuari >= 0):
        try:
            nombre_usuari = int(input("Introdueix un nombre natural (o negatiu per finalitzar): "))
        except:
            nombre_usuari= -1
        if nombre_usuari>=0:
            vector_valors.append(nombre_usuari)
    for i in range (len(vector_valors) - 1):
        for x in range(len(vector_valors) -1 - i):
            if vector_valors[x] > vector_valors[x +1]:
                vector_valors[x], vector_valors[x +1] = vector_valors[x +1], vector_valors[x]
    print(vector_valors)
if __name__== "__main__":
    main()