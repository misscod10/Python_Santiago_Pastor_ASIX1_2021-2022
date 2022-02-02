#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import qrcode
import json
"""
Un programa que crea un menu en el terminal
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"

def main():
    magatzem={}
    opcio=None
    while opcio !=0:
        print("|->0.Sortir")
        print("|->1.Afegir una nova parella clau-valor")
        print("|->2.Veure la llista de parelles")
        print("|->3.Crear el Codi QR")
        opcio=input("Seleciona una opcio ")
        if opcio=="0":
            print("Fins aviat!")
        elif opcio=="1":
            clau = input("Quina clau vols utilitzar? ")
            valor= input("Quin valor vols utilitzar? ")
            magatzem[clau]=valor
        elif opcio=="2":
            print(magatzem)
            input("Continua... ")
        elif opcio=="3":
            text=json.dumps(magatzem, indent=4)
            path= '/home/cf19santiago/Python_Santiago_Pastor_ASIX1_2021-2022/Estructures/Exercisis/qrs/qr.png'
            img = qrcode.make(text)
            img.save(path)
        else:
            print("Opcio incorrecta!")


if __name__=="__main__":
    main()