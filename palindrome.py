#!/bin/python3
# _*_ coding: utf-8 _*_

"""
#palindrome.py
#avalua si una cadena de text és o no un palindrome
"""
__author__ = "Xavi"
__editor__ = "Santi Pastor"

import sys
import doctest

def main(text_a_avaluar):
    """
    >>> main("radar")
    Si
    >>> main("peperoni")
    No
    >>> main("amazon")
    No
    >>> main("cucaracha")
    No
    >>> main("anna")
    Si
    >>> main("   ")
    Si
    >>> main("")
    Si
    >>> main("1221")
    Si
    >>> main("1212")
    No
    >>> main("a ti nob bonita")
    Si
    >>> main("tengo hambre")
    No
    >>> main ("a luna ese anula")
    Si
    >>> main ("amor a roma")
    Si
    >>> main ("innocentia nihil probat")
    No
    >>> main ("una araña muerta es una buena araña")
    No
    >>> main("b")
    Si
    """
    
    if text_a_avaluar.lower().replace(" ", "") == text_a_avaluar[::-1].lower().replace(" ", ""):
        print("Si")
    else:
        print("No")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Itrodueix una cadena de text per a evaluar si és o no un palíndrome")
        print("Exemple d'ús:")
        print("  $ python3 palindrome.py 'radar'")
        print("  Si")
        quit()

    main(sys.argv[1])
