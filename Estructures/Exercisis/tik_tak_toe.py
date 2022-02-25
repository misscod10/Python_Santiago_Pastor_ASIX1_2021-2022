#!/usr/bin/python3
# _*_ coding: utf-8 _*_
from fileinput import close
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
    for i in range(0,3):
        representacio_taulell= representacio_taulell +("|")
        for x in board[i]:
            representacio_taulell= representacio_taulell + (f"{simbols[x]}|")
        representacio_taulell= representacio_taulell +("\n")
    return representacio_taulell



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
    diagonal1=[taulell[0][0],taulell[1][1],taulell[2][2]]
    diagonal2=[taulell[0][2],taulell[1][1],taulell[2][0]]
    guanyador_lineas=comprobar_líneas(taulell)
    guanyador_columnas=comprobar_columnas(taulell)
    guanyador_diagonal1=comprobar_diagonal(diagonal1,taulell)
    guanyador_diagonal2=comprobar_diagonal(diagonal2,taulell)

    if guanyador_lineas!=None:
        return (f"Ha guanyat el jugador {guanyador_lineas}")
    if guanyador_columnas!=None:
        return (f"Ha guanyat el jugador {guanyador_columnas}")
    if guanyador_diagonal1 !=None:
        return (f"Ha guanyat el jugador {guanyador_diagonal1}")
    if guanyador_diagonal2 !=None:
        return (f"Ha guanyat el jugador {guanyador_diagonal2}")
    return ""
 
def comprobar_líneas(taulell):
    for i in range(0,3):
        linea=taulell[i]
        if linea==[1,1,1]:
            guanyador="1"
            break
        elif linea==[2,2,2]:
            guanyador="2"
            break
        else:
            guanyador=None
    return guanyador

def comprobar_columnas(taulell):
    for i in range(0,3):
        columna=[taulell[0][i],taulell[1][i],taulell[2][i]]
        if columna==[1,1,1]:
            guanyador="1"
            break
        elif columna==[2,2,2]:
            guanyador="2"
            break
        else:
            guanyador=None    
    return guanyador

def comprobar_diagonal(diagonal,taulell):
    if diagonal==[1,1,1]:
        guanyador="1"
    elif diagonal==[2,2,2]:
        guanyador="2"
    else:
        guanyador=None
    return guanyador
    
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
    print(resultat)
    

if __name__=="__main__":
    taulell_tik_tak_toe = [
        [2,1,1],
        [1,2,1],
        [1,0,2]
    ]
    print(main(taulell_tik_tak_toe))