#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Aquest programa en python ens serveix per encriptar cadenes de caràcters.
"""
__author__ = "Santiago"

import sys
import doctest
def main (clau_encriptar,frase_a_encriptar): 
    """
    >>> main("'13213121','hola mundo',")
    m:ñaNvb?mjG
    """
    clau_encriptar=int(sys.argv[1])
    clau_encriptar_separat=[int(a) for a in str(clau_encriptar)]
    frase_a_encriptar=sys.argv[2]
    abecedari= [
        ["a","b","c","d"],   ["e","f","g","h"],   ["i","j","k","l"],
        ["m","n","ñ","o"],   ["p","q","r","s"],   ["t","u","v","w"],
        ["x","y","z"],       [","," ","?","!"]
    ]
    frase_al_reves=str(frase_a_encriptar[::-1].lower())
    frase_al_reves=list(frase_al_reves)
    frase_encriptada=[""]
    cicle_clave=0   
    cicle=0
    for indice in range(0,len(frase_al_reves),2):
        entremedio=frase_al_reves[indice]
        frase_al_reves[indice]= frase_al_reves[indice+1]
        frase_al_reves[indice+1]=entremedio
    posicio_correcta=0
    for i in frase_al_reves:
        if i in abecedari[cicle]:           
            posicio_a_revisar=0
            while posicio_correcta==0:
                if abecedari[cicle][posicio_a_revisar]==i:
                    posicio_correcta=posicio_a_revisar
                else:
                    posicio_a_revisar+=1
            if clau_encriptar_separat[cicle]>(len(abecedari[0]))-(posicio_correcta):
                encryptat=abecedari[cicle][0+len(abecedari[cicle])-(posicio_correcta)]
                frase_encriptada.append(encryptat)
                cicle=0
            else:
                encryptat=abecedari[cicle][clau_encriptar_separat[cicle_clave]]
                frase_encriptada.append(encryptat)
                cicle=0
        else:
            cicle+=1
        cicle_clave+=1
        posicio_correcta=0
    print(frase_encriptada)
if __name__=='__main__':
    if len(sys.argv) < 2:
        print("Introdueix una cadena de text per encriptarla")
        print("Exemple d'ús:")
        print("  $ python3 encriptacio.py '13213121' 'hola Mundo'")
        print("  ")
        quit()
    elif len(sys.argv[1]) > 8:
        print("Es necesita una clau amb 8 dígits com a màxim")
        quit()
    main(sys.argv[1],sys.argv[2])