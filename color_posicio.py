#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Aquest programa ens permet saber si el cuadrat que li donem es blanc o negre.
_author_="Santiago Pastor Serrano"
import sys
posició_escollida=sys.argv[1]
columna=posició_escollida[0]
fila=int(posició_escollida[1])
if columna=="a":
    color="negre"
    color_contrari="blanc"
elif columna=="b":
    color="blanc"
    color_contrari="negre"
elif columna=="c":
    color="negre"
    color_contrari="blanc"
elif columna=="d":
    color="blanc"
    color_contrari="negre"
elif columna=="e":
    color="negre"
    color_contrari="blanc"
elif columna=="f":
    color="blanc"
    color_contrari="negre"
elif columna=="g":
    color="negre"
    color_contrari="blanc"
elif columna=="h":
    color="blanc"
    color_contrari="negre"
else:
    print("Posició invàlida")
    exit
if (fila % 2) != 0:
    print(color)
else:
    print(color_contrari)