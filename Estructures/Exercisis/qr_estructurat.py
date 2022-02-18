#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import qrcode
import json
"""
Un programa que crea un menu en el terminal i et permet crear un codi qr basant-se en la informació que li dones pero esta dividit en diferents funcions.
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
def main():
    magatzem={}
    opcio=None
    while opcio !=0:
       decision(opcio,magatzem)


def decision(opcio,magatzem):
        opcio=imprimir_menu()
        if opcio=="0":
            print("Fins aviat!")
        elif opcio=="1":
            clau,valor=nou_clau_valor()
            magatzem[clau]=valor
        elif opcio=="2":
            print(magatzem)
            input("Continua... ")
        elif opcio=="3":
            crear_qr(magatzem)
        else:
            print("Opcio incorrecta!")

def imprimir_menu():
        print("|->0.Sortir")
        print("|->1.Afegir una nova parella clau-valor")
        print("|->2.Veure la llista de parelles")
        print("|->3.Crear el Codi QR")
        return input("Seleciona una opcio ")

def nou_clau_valor():
        clau = input("Quina clau vols utilitzar? ")
        valor= input("Quin valor vols utilitzar? ")
        return clau,valor

def crear_qr(magatzem):
        text=json.dumps(magatzem, indent=4)
        path= '/tmp/qr.png'
        img = qrcode.make(text)
        img.save(path)
        print(path)


if __name__=="__main__":
    main()