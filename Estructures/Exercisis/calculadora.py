#!/usr/bin/python3
# _*_ coding: utf-8 _*_
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
"""
Aquest programa és una calculadora capaç de calcular la suma, resta, multiplicació , divisio, elevació i factorització de dos numeros (en el cas de la factorització tansols el primer numero)
"""
import sys
"""
>>> main(20, / ,5)
4.0
>>> main(5, * ,5)
25
>>> main(5, + ,5)
10
>>> main(5, ! ,5)
120
>>> main(5, ** ,5)
3125
>>> main(5, - ,5)
0
"""

def main (num1,operador,num2):
    try:    
        if operador == "+":
            Resultat = num1 + num2
            print(Resultat)
        elif operador == "-":
            Resultat = num1 - num2
            print(Resultat)
        elif operador == "*":
            Resultat = num1 * num2
            print(Resultat)
        elif operador == "/":
            Resultat = num1 / num2
            print(Resultat)
        elif operador == "**":
            Resultat = num1 ** num2
            print(Resultat)
        elif operador == "!":
            for i in range(1,num1):
                num1=num1*i
                Resultat=num1
            print(Resultat)
        
    except ValueError:
        print("Els números a operar han de ser enters")
    except ZeroDivisionError:
        print("A l'hora de fer una divisió cap dels dos números poden ser 0")
if __name__ == "__main__":
    main(int(sys.argv[1]), sys.argv[2],int(sys.argv[3]))






"""-*/**!"""   