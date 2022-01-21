#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""
Enunciat:

Desenvolupa un programa que repti els usuaris a endevinar el teu nom. Sí, sí, el teu nom.
El programa demanarà noms fins que el nom introduït sigui el teu.
Quan el nom introduït no és igual al teu, el programa encara comprovarà les següents possibilitats per
si pot oferir pistes als usuaris:
• En cas que el nom introduït comenci igual que el teu nom, el programa dirà que comença igual i
passarà a demanar el següent nom.
• En cas que el nom introduït finalitzi igual que el teu, indicarà que finalitzen igual i passarà a demanar
el següent nom.
• En cas que el nom introduït tingui la mateixa longitud que el teu nom, indicarà que són de la mateixa
llargària i demanarà el següent nom
• Altrament oferirà un missatge encoratjador "Ni t'hi acostes" i demanarà el següent nom
"""
mi_nombre="Santi"
acertado=0
while acertado == 0:
    print("A que no endevines com em dic?")
    intento= input()
    if intento != mi_nombre:
        if intento[0]==mi_nombre[0]:
            print("Comencen igual")
        elif intento[len(intento)-1] == mi_nombre[len(mi_nombre)-1]:
            print("Tenen la mateixa longitud")
        elif len(intento)== len(mi_nombre):
            print("Tenen la mateixa longitud")
        else:
            print("Ni t'hi acostes")
    else:
        print("Sí!")
        break