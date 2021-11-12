#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import doctest
__author__="Santiago Pastor Serrano"
"""
Aquest programa ens permet fer comptes de números dintre d'un cert rang i saltant-nos les posicions
"""
def main (inici,final,salt):
    """
    >>> main(10,18,2)
    10, 12, 14, 16, 18
    >>> main(10,17,2)
    10, 12, 14, 16
    >>> main(18,10,-2)
    18, 16, 14, 12, 10
    >>> main(10,18,0)
    Traceback (most recent call last):
        File "/home/santiago/Escritorio/Python_Santiago_Pastor_ASIX1_2021-2022/Estructures/salt_de_granota.py", line 37, in <module>
            main(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
        File "/home/santiago/Escritorio/Python_Santiago_Pastor_ASIX1_2021-2022/Estructures/salt_de_granota.py", line 26, in main
            raise ValueError ('El valor de salt no pot ser 0')
    ValueError: El valor de salt no pot ser 0
    """
    resultat = ""
    if salt>0:
        final=final+1
    elif salt<0:
        final=final-1
    if salt == 0:
        raise ValueError ('El valor de salt no pot ser 0')
        quit
    for index in range(inici,final,salt):
        if index!=inici:
            resultat = resultat + ", " + str(index)
        else:
            resultat = resultat + str(index)

    print(resultat)

if __name__=='__main__':
    main(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))