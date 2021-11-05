#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Aquest programa en python ens serveix per girar una cadena del revés.
"""
__author__ = "Santiago"

import sys
import doctest
cadena=sys.argv[1]
frase_al_reves=str(cadena[::-1].lower())
print(frase_al_reves)
frase_al_reves=list(frase_al_reves)
for indice in range(0,len(frase_al_reves),2):
    entremedio=frase_al_reves[indice]
    if indice+1>len(frase_al_reves):
            frase_al_reves[indice]= frase_al_reves[indice+1]
            frase_al_reves[indice+1]=entremedio
print(frase_al_reves)