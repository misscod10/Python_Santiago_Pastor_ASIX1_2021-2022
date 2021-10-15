#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Aquest programa en python ens serveix per calcular l'edat d'un gos en anys humans.
import sys
if len(sys.argv) < 1:
    print("     >>>   Has d'introduïr com a paràmetre l'edat del gos   <<<")
    print("     >>>   Ex: python3 edat_gos.py <anys del gos>           <<<")
    print("     >>>   Torna-ho a provar d'aquesta manera               <<<")
    quit()
anys_humans=float(sys.argv[1])
if anys_humans > 2:
    anys_gos=((anys_humans-2.0) * 4.0)+ 21.0
else:
    anys_gos=anys_humans * 10.5
print(">",anys_humans,"anys humans equivalen a",anys_gos,"anys de gos")