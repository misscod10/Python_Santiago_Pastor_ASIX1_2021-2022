#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""
Aquest programa agafa la matrícula proporcionada i confirma si es valida o no ho és
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
def main():
    letras=[""]
    numeros=""
    matricula= input("Introdueix una matricula: ")
    letras=["A","E","I","O","U","Q"]
    numeros_p=["1","2","3","4","5","6","7","8","9"]
    try:
        for i in range(4):
            numeros= int(matricula[i])
    except:
        print("No és una mareícula valida")
    if matricula[4] != " ":
        print("No és una matricula valida")
    else:
        for x in range(5,8):
            if not matricula[x] in letras:
                    if not matricula[x] in numeros_p:
                        if x ==7:
                            print("És una matricula valida")
                    else:
                        print("No és una matricula valida")
                        break
            else:
                print("No és una matricula valida")
                break
main()