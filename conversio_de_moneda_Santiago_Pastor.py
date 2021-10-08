#!/usr/bin/python
moneda_desti=input("A quina moneda vols convertir el teus Euros? ")
equivalencia=float(input("Quina quantitat d'aquista moneda és equivalent a 1 EUR? "))
quantitat=float(input("Quants Euros vols canviar? "))
resultat=float(quantitat*equivalencia)
print("L'equivalent de", quantitat,"EUR, es de",resultat, moneda_desti)