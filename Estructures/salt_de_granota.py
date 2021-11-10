#!/usr/bin/python3
import sys
import doctest
__author__="Santiago Pastor Serrano"

def main (inici,final,salt):
    """
    >>> main(10,18,2)
    ['10', '12', '14', '16','18']
    >>> main(10,17,2)
    ['10', '12', '14', '16']
    >>> main(18,10,-2)
    ['18', '16', '14', '12','10']
    """
    resultat=[]
    if salt == 0:
        raise ValueError('El valor de salt no pot ser 0')
        quit
    for index in range(inici,final,salt):
        resultat.append(str(index))
    print(resultat)

if __name__=='__main__':
    main(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))