#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import random, os

"""
barres.py mostra gràficament els elements d'una llista 
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"

def main(llista):
    """
    Visualitza gràficament els valors de llista
    >>> main([1, 2, 3])
    * 1
    ** 2
    *** 3
    >>> main([3,1,3])
    *** 3
    * 1
    *** 3
    """
    os.system('clear')
    # El teu codi a partir d'aquí
    for i in llista:
        asteriscos=""
        for x in range(i):
            asteriscos=asteriscos+"*"
        asteriscos=asteriscos+" "+str(i)
        print(asteriscos)

    
if __name__ == "__main__":
    vector_valors = []
    for index in range(10):
        vector_valors.append(random.randrange(30) + 1)
    main(vector_valors)