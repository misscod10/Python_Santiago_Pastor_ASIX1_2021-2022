#!/usr/bin/python3        
# _*_ coding: utf-8 _*_   

"""
    Ens calcula els factors primers d'un nombre.
    Exemple d'ús:
    $ python3 factoritza.py 12
    1, 2, 2, 3
"""
'Comando para hacer test: python3 -m doctest -v factoritza.py '
__author__ = "Xavi Quesada"  #-> Qui ha creat el programa.
__editor__ = "Santi Pastor"
import sys
import doctest

if (len(sys.argv) < 2):
        print("===================================")
        print("Necessites introduïr una nombre a factoritzar.")
        print("Ex: $ python3 factoritza.py 12")
        print("1, 2, 2, 3")
        print("===================================")
        quit()

def main(str_nombre_a_factoritzar):
    """
    És el punt d'entrada al nostre programa

    >>> main(1)
    1
    >>> main(24)
    1, 2, 2, 2, 3
    >>> main(12)
    1, 2, 2, 3
    >>> main(36)
    1, 2, 2, 3, 3
    """
    nombre_a_factoritzar = int(str_nombre_a_factoritzar)
    possible_factor = 2
    factors = [1]
    while possible_factor <= nombre_a_factoritzar:
        if (nombre_a_factoritzar % possible_factor == 0):
            factors.append(possible_factor)
            nombre_a_factoritzar = nombre_a_factoritzar // possible_factor
        else:
            possible_factor += 1
    
    resultat = ""
    for index in range(len(factors)):
        resultat = resultat + str(factors[index])
        if index < len(factors) - 1:
            resultat += ", "
    print (resultat)


if __name__ == "__main__":
    main(sys.argv[1])