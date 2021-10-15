#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
#Missatge d'error si es donen menys arguments dels necessaris.
if len(sys.argv) < 3:
    print("     >>>   Has d'introduïr com a paràmetres l'import pagat i el valor del ticket.   <<<")
    print("     >>>   Ex: python3 canvi_compra.py <pagat> <import del ticket>                  <<<")
    print("     >>>   Torna-ho a provar                                                        <<<")
    quit()
Entregat=float(sys.argv[1])
Total_Ticket=float(sys.argv[2])
print("Entregat: ", Entregat)
print("Total ticket: ", Total_Ticket)
A_Retornar=Entregat-Total_Ticket
Retorn=A_Retornar
Billets_de_10=0
Billets_de_5=0
Moneda_de_1=0
Moneda_de_05=0
while A_Retornar>=0.5:
    if A_Retornar >= 10.0:
        Billets_de_10+=1
        A_Retornar-=10
        
    elif A_Retornar >= 5.0:
        Billets_de_5+=1
        A_Retornar-=5
        
    elif A_Retornar >= 1.0:
        Moneda_de_1+=1
        A_Retornar-=1
        
    elif A_Retornar >= 0.5:
        Moneda_de_05+=1
        A_Retornar-=0.5
print(    )
if Billets_de_10 >=1:
    print(Billets_de_10 ," x billet de 10€")
if Billets_de_5 >=1:
    print(Billets_de_5 ," x billet de 5€")
if Moneda_de_1 >=1:
    print(Moneda_de_1 ," x moneda de 1€")
if Moneda_de_05 >=1:
    print(Moneda_de_05 ," x moneda de 0.5€")

print("---------------------------------")
print("Total canvi ", Retorn,"€")