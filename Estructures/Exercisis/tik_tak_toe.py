#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import random, os, functools

"""
tik_tak_toe.py mostra un taulell de tik-tak-toe i comprova si te un guanyador
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"


def dibuixa_taulell(board):
    """
    >>> print(dibuixa_taulell([[1,1,1],[1,1,1],[1,1,1]]))
    |X|X|X|
    |X|X|X|
    |X|X|X|
    <BLANKLINE>
    """
    representacio_taulell = ""
    simbols = [" ", "X", "O"] 
    representacio_taulell=representar(board,simbols)
    return representacio_taulell
def representar(board,simbols):
    representació=""
    for i in board:
        for x in board[i]:
            representacio= representacio + (f"|{simbols[x]}|")
        representacio= representacio +("\n")
    return representacio
            

        

def comproba_guanyador(taulell):
    """
    # Comprova diagonal 1
    >>> print(comproba_guanyador([[1,0,2],[0,1,2],[2,0,1]]))
    Ha guanyat el jugador 1

    # Comprova diagonal 2
    >>> print(comproba_guanyador([[1,1,2],[0,2,2],[2,1,1]]))
    Ha guanyat el jugador 2

    # Comprova linia 1
    >>> print(comproba_guanyador([[1,1,1],[0,2,2],[2,0,0]]))
    Ha guanyat el jugador 1

    # Comprova linia 3
    >>> print(comproba_guanyador([[1,0,1],[0,0,1],[2,2,2]]))
    Ha guanyat el jugador 2

    # Comprova columna 1
    >>> print(comproba_guanyador([[1,0,2],[1,0,2],[1,2,0]]))
    Ha guanyat el jugador 1

    # Comprova quan no hi ha guanyador
    >>> print(comproba_guanyador([[0,0,0],[0,0,0],[1,2,0]]))
    <BLANKLINE>
    """
    # TODO implementar funcio
    return "Ha guanyat el jugador 3"    
    
def main(taulell):
    """
    Dibuixa el taulell i comprova si hi ha guanyadors
    # Comprova diagonal 1
    >>> print(main([[1,0,2],[0,1,2],[2,0,1]]))
    |X| |O|
    | |X|O|
    |O| |X|
    Ha guanyat el jugador 1

    # Comprova diagonal 2
    >>> print(main([[1,1,2],[0,2,2],[2,1,1]]))
    |X|X|O|
    | |O|O|
    |O|X|X|
    Ha guanyat el jugador 2

    # Comprova linia 1
    >>> print(main([[1,1,1],[0,2,2],[2,0,0]]))
    |X|X|X|
    | |O|O|
    |O| | |
    Ha guanyat el jugador 1

    # Comprova linia 3
    >>> print(main([[1,0,1],[0,0,1],[2,2,2]]))
    |X| |X|
    | | |X|
    |O|O|O|
    Ha guanyat el jugador 2

    # Comprova columna 1
    >>> print(main([[1,0,2],[1,0,2],[1,2,0]]))
    |X| |O|
    |X| |O|
    |X|O| |
    Ha guanyat el jugador 1

    # Comprova quan no hi ha guanyador
    >>> print(main([[0,0,0],[0,0,0],[1,2,0]]))
    | | | |
    | | | |
    |X|O| |
    <BLANKLINE>
    """
    resultat = dibuixa_taulell(taulell)
    resultat = resultat + comproba_guanyador(taulell)
    return resultat
    

if __name__=="__main__":
    taulell_tik_tak_toe = [
        [2,1,1],
        [1,2,1],
        [1,0,2]
    ]
    print(main(taulell_tik_tak_toe))