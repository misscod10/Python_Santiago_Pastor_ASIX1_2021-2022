#!/usr/bin/python3
# _*_ coding: utf-8 _*_
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
"""
Aquest programa té un menú que et permet canviar un string a tot majúscules, tot minúscules, invertir las majúscules i minúscules i finalment fer majúscula la primera lletra de cada paraula de la string.
"""
def main():
    parar=0
    while parar==0:
        print("--- --- --- --- --- --- --- --- --- --- --- ---\n0.- Surt del programa.\n1.- Tot amb majúscules.\n2.- Tot amb minúscules.\n3.- Inverteix l'ús de majúscules i minúscules.\n4.- Majúscula la primera lletra de cada paraula.\n--- --- --- --- --- --- --- --- --- --- --- ---",)
        opcio=int(input("Seleciona una opció: "))
        if opcio==0:
            parar=1
            print("Has triat sortir del programa, fins aviat!")
        elif opcio==1:
            print("Has triat convertir tot el text a majúscules")
            text=input("Introdueix la frase a processar: ")
            text=text.upper()
            print(f"<<< {text} >>>")
        elif opcio==2:
            print("Has triat convertir tot el text a minúscules")
            text=input("Introdueix la frase a processar: ")
            text=text.lower()
            print(f"<<< {text} >>>")
        elif opcio==3:
            print("Has triat invertir l'ús de majúscules i minúscules")
            text=input("Introdueix la frase a processar: ")
            text=text.swapcase()
            print(f"<<< {text} >>>")
        elif opcio==4:
            print("Has triat posar en majúscula la primera lletra de cada paraula")
            text=input("Introdueix la frase a processar: ")
            text=text.capitalize()
            print(f"<<< {text} >>>")
        else:
            print("Opció incorrecta, torna a provar")
if __name__=='__main__':
    main()