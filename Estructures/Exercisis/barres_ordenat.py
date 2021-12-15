#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import random, os

"""
barres_ordenat.py mostra gràficament els elements d'una llista d'una forma ordenada 
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"

def main(llista):
    os.system('clear')
    # El teu codi a partir d'aquí
    llista2=[]
    for i in llista:
        llista2.append(i)
    for x in range(len(llista2) - 1):
        for y in range(len(llista2) - 1 - x):
             if llista2[y] > llista2[y+1]:
                 llista2[y], llista2[y+1] = llista2[y+1], llista2[y]
    for z in llista2:
        print(f'{"*"*z} {z}')
if __name__ == "__main__":
    vector_valors = []
    for index in range(10):
        vector_valors.append(random.randrange(30) + 1)
    main(vector_valors)