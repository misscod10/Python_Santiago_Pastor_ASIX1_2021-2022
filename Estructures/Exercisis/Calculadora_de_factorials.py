#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""
Aquest programa agafa un número enter que li proporcionis i calcula el seu factorial
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
def main():
    numero_a_factorizar=int(input("Introdueix un número enter per calcular el seu factorial: "))
    numero_factorial=0
    if numero_a_factorizar<0:
        raise Exception ("No puc calcular el factorial de un número negatiu")
    elif numero_a_factorizar== 0:
        print(1)
    else:
        for i in range (1,numero_a_factorizar + 1):
            if numero_factorial == 0:
                numero_factorial = i
            numero_factorial = numero_factorial * i
        print(numero_factorial)
main()