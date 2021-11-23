#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
lista_amb_*.py transforma els continguts de una lista en els seus equivalents en *
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"

llista=[1,5,3,7,9,4]
for i in llista:
    impressio=""
    for x in range(i):
        impressio= impressio + "*"
    print(impressio)