#!/usr/bin/python3
#  coding: utf-8 

import clipboard
import json
import sys

"""
clipboard.py jugant amb el clipboard
"""

__author__   = "Oscar Gonzalez"
__email__    = "oscar.gonzalez@iesjoandaustria.org"
__license__  = "GPL V3"

RUTA_FITXER = "/tmp/org.joandaustria.json"

def recupera_valors():
    try:
        with open(RUTA_FITXER, "r") as fitxer:
            valors = json.loads(fitxer.read())
            return valors
    except:
        with open(RUTA_FITXER, "w") as fitxer:
            fitxer.write('{}')
            return {}

def desa(clau, valor):
    historic_de_valors = recupera_valors()
    historic_de_valors[clau] = valor
    with open(RUTA_FITXER, "w") as f:
        f.write(json.dumps(historic_de_valors))
def main(comand, key):
    if comand == 'save':
        desa(key, clipboard.paste())
        return "Objecte desat amb contingut: " + clipboard.paste()
    elif comand == 'restore':
        valor_desat = recupera_valors[key]
        clipboard.copy(valor_desat)
        return "Objecte recuperat amb contingut: " + valor_desat
    else:
        return json.dumps(recupera_valors, sort_keys=True, indent=4)

    valors = ()

if __name__ == "__main__":
    # python3 mi_clipboard [save|restore|list] [clau]
    comnada = None
    clau = None
    try:
        comanda = sys.argv[1]
        if not (comanda == "list"):
            clau = sys.argv[2]
        print(main(comanda, clau))
    except Exception as e:
        print("Mode d'us:")
        print("\tpython3 mi_clipboard [save|restore|list] [clau]")

