#!/usr/bin/python3
# _*_ coding: utf-8 _*_

"""
troba_maxim.py rep números naturals de forma seqüencial i termina al rebre un de negatiu.
Al terminar informa de quin ha estat el nombre més gran introduït.
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"

def main():
    numero_actual=0
    numeros=[]
    maxim=0
    try:
        while numero_actual>=0:
            numero_actual=(int(input("Introdueix un número natural: ")))
            numeros.append(int(numero_actual))
    
        for i in numeros:
            if i > maxim:
                maxim=i
        return maxim
    except ValueError:
        print("No pots introduïr valors buits!!!")

if __name__ == "__main__":
    print(f"El màxim ha estat: {main()}")
