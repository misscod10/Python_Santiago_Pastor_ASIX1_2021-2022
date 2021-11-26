#!/usr/bin/python3
# _*_ coding: utf-8 _*_
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
"""
Aquest programa imprimeixi els nombres del 1 al 110 en ordre per pantalla, però els que siguin múltiples de 3 s'han de substituir per Blass, els que siguin múltiples de 5 per Tizz i els que siguin múltiples de 7 per Zaff. Els que siguin alhora múltiples de 3 i de 5 han de ser substituits per BlassTizz, els que siguin múltiples de 3 i de 7 per BlassZaff, els que siguin múltiples de 5 i de 7 per TizzZaff i els que siguin múltiples de 3, 5 i 7 per BlasTizzZaff.
"""
for i in range(1,111):
    if i%3 == 0:
        if i%5 == 0:
            print("BlassTizz")
            if i%7 == 0:
                print("BlassTizzZaff")
        elif i%7 == 0:
            print("BlassZaff")
        else:
            print("Blass")        
    elif i%5 == 0:
        if i%7 == 0:
            print("TizzZaff")
        else:
            print("Tizz")
    elif i%7 == 0:
        print("Zaff")
    else:
        print(i)